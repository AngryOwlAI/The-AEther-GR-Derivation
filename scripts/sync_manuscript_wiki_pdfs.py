#!/usr/bin/env python3

"""Sync repository PDF corpora into the local Manuscript Wiki vault."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

from manuscript_wiki_lib import (
    MANIFEST_RELATIVE,
    ensure_directory,
    file_sha256,
    iso_from_timestamp,
    list_pdf_sources,
    load_manifest,
    manifest_index,
    now_iso,
    repo_root,
    resolve_vault_path,
    write_json,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Copy repository-owned PDFs into the local Manuscript Wiki vault and "
            "refresh the sync manifest."
        )
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--all",
        action="store_true",
        help="Re-copy every supported PDF into the vault.",
    )
    mode.add_argument(
        "--changed",
        action="store_true",
        help="Copy only PDFs whose vault copies are missing or stale.",
    )
    mode.add_argument(
        "--one",
        metavar="PATH",
        help="Copy exactly one repository PDF (relative or absolute path).",
    )
    parser.add_argument(
        "--vault",
        help=(
            "Vault path to update. Defaults to "
            ".local/obsidian/aether-manuscripts-wiki inside the repository."
        ),
    )
    parser.add_argument(
        "--quarantine-stale",
        action="store_true",
        help="Move stale vault PDFs into 07_logs/stale_pdfs/ instead of deleting them.",
    )
    args = parser.parse_args()
    if not args.all and not args.changed and not args.one:
        args.changed = True
    return args


def resolve_one_target(target: str, root: Path) -> Path:
    candidate = Path(target).expanduser()
    if candidate.is_absolute():
        return candidate.resolve()
    return (root / candidate).resolve()


def match_one_source(target: str, root: Path):
    resolved_target = resolve_one_target(target, root)
    sources = list_pdf_sources(root)

    exact_matches = [source for source in sources if source.source_path.resolve() == resolved_target]
    if len(exact_matches) == 1:
        return exact_matches[0]
    if len(exact_matches) > 1:
        raise SystemExit(f"Ambiguous --one target: {target}")

    relative_target = target.strip().lstrip("./")
    path_matches = [source for source in sources if source.relative_repo_path == relative_target]
    if len(path_matches) == 1:
        return path_matches[0]
    if len(path_matches) > 1:
        raise SystemExit(f"Ambiguous --one target: {target}")

    name_matches = [source for source in sources if source.source_path.name == target]
    if len(name_matches) == 1:
        return name_matches[0]
    if len(name_matches) > 1:
        raise SystemExit(
            "Ambiguous --one target by filename. Pass a repository-relative PDF path instead."
        )

    raise SystemExit(f"Could not resolve --one target to a supported repository PDF: {target}")


def should_copy(source_path: Path, destination_path: Path, force: bool) -> bool:
    if force or not destination_path.exists():
        return True
    source_stat = source_path.stat()
    destination_stat = destination_path.stat()
    return (
        source_stat.st_size != destination_stat.st_size
        or int(source_stat.st_mtime) != int(destination_stat.st_mtime)
    )


def cleanup_stale_files(
    vault_root: Path,
    expected_relative_paths: set[str],
    quarantine: bool,
    generated_at: str,
) -> list[dict[str, str]]:
    stale_actions: list[dict[str, str]] = []
    expected_absolute_paths = {
        (vault_root / relative_path).resolve() for relative_path in expected_relative_paths
    }

    scan_roots = [
        vault_root / "01_raw/project_pdfs/active",
        vault_root / "01_raw/project_pdfs/retired",
        vault_root / "01_raw/project_pdfs/public_bundle",
    ]

    for scan_root in scan_roots:
        if not scan_root.exists():
            continue
        for candidate in sorted(scan_root.rglob("*.pdf")):
            if candidate.resolve() in expected_absolute_paths:
                continue

            if quarantine:
                quarantine_root = (
                    vault_root
                    / "07_logs/stale_pdfs"
                    / generated_at.replace(":", "-")
                    / candidate.relative_to(vault_root).parent
                )
                ensure_directory(quarantine_root)
                quarantine_target = quarantine_root / candidate.name
                shutil.move(str(candidate), quarantine_target)
                stale_actions.append(
                    {
                        "action": "quarantined",
                        "stale_vault_path": str(candidate),
                        "quarantine_path": str(quarantine_target),
                    }
                )
            else:
                candidate.unlink()
                stale_actions.append(
                    {
                        "action": "deleted",
                        "stale_vault_path": str(candidate),
                    }
                )

    return stale_actions


def main() -> int:
    args = parse_args()
    root = repo_root()
    vault = resolve_vault_path(args.vault, root)
    ensure_directory(vault)

    all_sources = list_pdf_sources(root)
    selected_sources = (
        all_sources
        if args.all or args.changed
        else [match_one_source(args.one, root)]
    )

    previous_manifest = load_manifest(vault)
    previous_index = manifest_index(previous_manifest)
    generated_at = now_iso()

    actions: dict[str, str] = {}
    copied = 0
    updated = 0
    unchanged = 0

    force_copy = bool(args.all)
    for source in selected_sources:
        destination = vault / source.relative_vault_path
        action = "unchanged"
        if should_copy(source.source_path, destination, force_copy):
            ensure_directory(destination.parent)
            existed = destination.exists()
            shutil.copy2(source.source_path, destination)
            action = "updated" if existed else "copied"
        actions[source.relative_repo_path] = action
        if action == "copied":
            copied += 1
        elif action == "updated":
            updated += 1
        else:
            unchanged += 1

    expected_relative_paths = {source.relative_vault_path for source in all_sources}
    stale_actions = cleanup_stale_files(
        vault_root=vault,
        expected_relative_paths=expected_relative_paths,
        quarantine=args.quarantine_stale,
        generated_at=generated_at,
    )

    entries = []
    for source in all_sources:
        destination = vault / source.relative_vault_path
        if not destination.exists():
            continue
        previous_entry = previous_index.get(source.relative_repo_path, {})
        synced_at = str(previous_entry.get("synced_at", ""))
        if actions.get(source.relative_repo_path) in {"copied", "updated"} or not synced_at:
            synced_at = generated_at

        entries.append(
            {
                "category": source.category,
                "file_name": source.source_path.name,
                "source_repo_path": str(source.source_path),
                "vault_destination_path": str(destination),
                "relative_repo_path": source.relative_repo_path,
                "relative_vault_path": source.relative_vault_path,
                "file_size": destination.stat().st_size,
                "sha256": file_sha256(destination),
                "repo_last_modified": iso_from_timestamp(source.source_path.stat().st_mtime),
                "synced_at": synced_at,
            }
        )

    manifest_payload = {
        "generated_at": generated_at,
        "vault_root": str(vault),
        "selected_mode": "all" if args.all else "changed" if args.changed else "one",
        "entries": entries,
        "stale_actions": stale_actions,
        "summary": {
            "total_repo_pdfs": len(all_sources),
            "selected_pdfs": len(selected_sources),
            "copied": copied,
            "updated": updated,
            "unchanged": unchanged,
            "manifest_entries": len(entries),
            "stale_actions": len(stale_actions),
        },
    }
    write_json(vault / MANIFEST_RELATIVE, manifest_payload)

    print(f"Synced Manuscript Wiki PDFs into {vault}")
    print(
        f"Selected {len(selected_sources)} PDF(s): "
        f"{copied} copied, {updated} updated, {unchanged} unchanged"
    )
    print(f"Manifest entries: {len(entries)}")
    if stale_actions:
        action_label = "quarantined/deleted"
        print(f"Stale vault PDFs {action_label}: {len(stale_actions)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
