#!/usr/bin/env python3

"""Lint the local Manuscript Wiki for drift, missing files, and stale metadata."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from manuscript_wiki_lib import (
    CONCEPT_DEFINITIONS,
    FAMILY_NAMES,
    PROJECT_ROLES,
    ROUTING_STATUSES,
    concept_relative_path,
    deterministic_vault_pdf_relative_path,
    family_relative_path,
    file_sha256,
    iso_from_timestamp,
    line_relative_path,
    load_file_map_rows,
    load_manifest,
    manifest_index,
    parse_frontmatter,
    priority_relative_path,
    read_text_if_exists,
    repo_root,
    resolve_vault_path,
    routing_relative_path,
    source_note_relative_path,
)


WIKI_LINK_PATTERN = re.compile(r"\[\[([^\]]+)\]\]")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Check the local Manuscript Wiki for missing PDFs, missing notes, stale "
            "frontmatter, duplicate notes, and broken internal links."
        )
    )
    parser.add_argument(
        "--vault",
        help=(
            "Vault path to lint. Defaults to "
            ".local/obsidian/aether-manuscripts-wiki inside the repository."
        ),
    )
    return parser.parse_args()


def resolve_wiki_link(current_file: Path, vault_root: Path, raw_target: str) -> bool:
    target = raw_target.split("|", 1)[0].split("#", 1)[0].strip()
    if not target:
        return True

    path_target = Path(target)
    candidates: list[Path] = []
    if path_target.suffix:
        candidates.extend([vault_root / path_target, current_file.parent / path_target])
    else:
        bases = [vault_root / path_target, current_file.parent / path_target]
        for base in bases:
            candidates.extend([base, base.with_suffix(".md"), base.with_suffix(".pdf")])

    return any(candidate.exists() for candidate in candidates)


def main() -> int:
    args = parse_args()
    root = repo_root()
    vault = resolve_vault_path(args.vault, root)
    if not vault.exists():
        raise SystemExit(f"Vault does not exist: {vault}")

    rows = load_file_map_rows(root)
    manifest_lookup = manifest_index(load_manifest(vault))
    issues: list[str] = []

    note_texts: dict[str, str] = {}
    note_paths: dict[str, Path] = {}

    for row in rows:
        expected_vault_pdf_relative = deterministic_vault_pdf_relative_path(row["pdf_path"])
        expected_vault_pdf = vault / expected_vault_pdf_relative
        if not expected_vault_pdf.exists():
            issues.append(
                f"Missing vault PDF copy for {row['file_name']}: {expected_vault_pdf_relative}"
            )

        note_path = vault / source_note_relative_path(row["file_name"])
        if not note_path.exists():
            issues.append(f"Missing manuscript source note for {row['file_name']}")
            continue

        note_text = read_text_if_exists(note_path)
        note_texts[row["file_name"]] = note_text
        note_paths[row["file_name"]] = note_path
        frontmatter = parse_frontmatter(note_text)

        expected_pairs = {
            "file_name": row["file_name"],
            "title": row["title"],
            "family": row["family"],
            "document_type": row["document_type"],
            "project_role": row["project_role"],
            "line_name": row["line_name"],
            "frontline_status": row["frontline_status"],
            "reading_priority": row["reading_priority"],
            "sequence_stage": row["sequence_stage"],
            "status_reason": row["status_reason"],
            "benchmark_effect": row["benchmark_effect"],
            "short_description": row["short_description"],
            "current_use_rule": row["current_use_rule"],
            "upstream_dependency": row["upstream_dependency"],
            "downstream_target": row["downstream_target"],
            "relative_tex_path": row["relative_path"],
            "relative_repo_pdf_path": row["pdf_path"],
            "relative_vault_pdf_path": expected_vault_pdf_relative,
            "map_last_known_relevance": row["last_known_relevance"],
        }

        for key, expected_value in expected_pairs.items():
            actual_value = frontmatter.get(key, "")
            if actual_value != expected_value:
                issues.append(
                    f"{row['file_name']}: frontmatter mismatch for {key}: "
                    f"expected {expected_value!r}, found {actual_value!r}"
                )

        repo_pdf_path = root / row["pdf_path"]
        if repo_pdf_path.exists():
            expected_repo_modified = iso_from_timestamp(repo_pdf_path.stat().st_mtime)
            if frontmatter.get("repo_last_modified", "") != expected_repo_modified:
                issues.append(
                    f"{row['file_name']}: stale repo_last_modified frontmatter"
                )

        manifest_entry = manifest_lookup.get(row["pdf_path"])
        if expected_vault_pdf.exists() and not manifest_entry:
            issues.append(
                f"{row['file_name']}: missing sync manifest entry for {row['pdf_path']}"
            )
        elif manifest_entry:
            expected_hash = str(manifest_entry.get("sha256", ""))
            expected_synced_at = str(manifest_entry.get("synced_at", ""))
            if frontmatter.get("sha256", "") != expected_hash:
                issues.append(f"{row['file_name']}: sha256 frontmatter is stale")
            if frontmatter.get("vault_last_synced", "") != expected_synced_at:
                issues.append(f"{row['file_name']}: vault_last_synced frontmatter is stale")
            if expected_vault_pdf.exists():
                actual_hash = file_sha256(expected_vault_pdf)
                if actual_hash != expected_hash:
                    issues.append(
                        f"{row['file_name']}: manifest hash does not match the vault PDF copy"
                    )

    duplicate_note_map: dict[str, list[Path]] = {}
    source_note_dir = vault / "02_sources/manuscripts"
    if source_note_dir.exists():
        for note_path in sorted(source_note_dir.glob("*.md")):
            frontmatter = parse_frontmatter(read_text_if_exists(note_path))
            file_name = frontmatter.get("file_name", note_path.stem)
            duplicate_note_map.setdefault(file_name, []).append(note_path)
    for file_name, paths in duplicate_note_map.items():
        if len(paths) > 1:
            issues.append(
                f"Duplicate manuscript notes for {file_name}: "
                + ", ".join(str(path) for path in paths)
            )

    for markdown_file in sorted(vault.rglob("*.md")):
        text = read_text_if_exists(markdown_file)
        for match in WIKI_LINK_PATTERN.findall(text):
            if not resolve_wiki_link(markdown_file, vault, match):
                issues.append(
                    f"Broken internal wiki link in {markdown_file.relative_to(vault)}: [[{match}]]"
                )

    for status in ROUTING_STATUSES:
        page_path = vault / routing_relative_path(status)
        if not page_path.exists():
            issues.append(f"Missing routing index page: {page_path.relative_to(vault)}")

    for family in FAMILY_NAMES:
        page_path = vault / family_relative_path(family)
        if not page_path.exists():
            issues.append(f"Missing family index page: {page_path.relative_to(vault)}")

    for role in PROJECT_ROLES:
        page_path = vault / priority_relative_path(role)
        if not page_path.exists():
            issues.append(f"Missing project-role index page: {page_path.relative_to(vault)}")

    for line_name in sorted({row["line_name"] for row in rows}):
        page_path = vault / line_relative_path(line_name)
        if not page_path.exists():
            issues.append(f"Missing line page: {page_path.relative_to(vault)}")

    for row in rows:
        note_reference = source_note_relative_path(row["file_name"]).as_posix()
        routing_text = read_text_if_exists(vault / routing_relative_path(row["frontline_status"]))
        family_text = read_text_if_exists(vault / family_relative_path(row["family"]))
        role_text = read_text_if_exists(vault / priority_relative_path(row["project_role"]))
        line_text = read_text_if_exists(vault / line_relative_path(row["line_name"]))
        if note_reference not in routing_text:
            issues.append(f"{row['file_name']}: routing index is missing the current note link")
        if note_reference not in family_text:
            issues.append(f"{row['file_name']}: family index is missing the current note link")
        if note_reference not in role_text:
            issues.append(f"{row['file_name']}: project-role index is missing the current note link")
        if note_reference not in line_text:
            issues.append(f"{row['file_name']}: line page is missing the current note link")

    for concept in CONCEPT_DEFINITIONS:
        concept_path = vault / concept_relative_path(str(concept["title"]))
        if not concept_path.exists():
            issues.append(f"Missing concept page: {concept_path.relative_to(vault)}")
            continue
        link_prefix = f"[[{concept_relative_path(str(concept['title'])).as_posix()}"
        if not any(link_prefix in note_text for note_text in note_texts.values()):
            issues.append(
                f"Concept page {concept['title']} has no backlinks from generated manuscript notes"
            )

    if issues:
        print("Manuscript Wiki lint failed.")
        for issue in issues:
            print(f"- {issue}")
        return 1

    print(
        "Manuscript Wiki lint passed: "
        f"{len(rows)} manuscript notes, {len(CONCEPT_DEFINITIONS)} concept pages, "
        "and the routing/index pages are in sync."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
