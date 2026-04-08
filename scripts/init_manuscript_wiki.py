#!/usr/bin/env python3

"""Initialize a local Obsidian vault for the Manuscript Wiki."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

from manuscript_wiki_lib import (
    VAULT_DIRECTORIES,
    ensure_directory,
    repo_root,
    resolve_vault_path,
    template_root,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Create the local Manuscript Wiki vault layout and copy the tracked "
            "template and schema files into place."
        )
    )
    parser.add_argument(
        "--vault",
        help=(
            "Vault path to initialize. Defaults to "
            ".local/obsidian/aether-manuscripts-wiki inside the repository."
        ),
    )
    parser.set_defaults(write_obsidian_stubs=True)
    parser.add_argument(
        "--write-obsidian-stubs",
        dest="write_obsidian_stubs",
        action="store_true",
        help="Copy the tracked Obsidian config stubs into .obsidian/ (default).",
    )
    parser.add_argument(
        "--no-obsidian-stubs",
        dest="write_obsidian_stubs",
        action="store_false",
        help="Skip copying the tracked Obsidian config stubs into .obsidian/.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite tracked template files if they already exist in the vault.",
    )
    parser.add_argument(
        "--no-next-steps",
        action="store_true",
        help="Skip the printed next-step instructions.",
    )
    return parser.parse_args()


def copy_tree(source_root: Path, destination_root: Path, overwrite: bool) -> list[Path]:
    copied: list[Path] = []
    if not source_root.exists():
        return copied
    for source in sorted(source_root.rglob("*")):
        if source.is_dir():
            continue
        destination = destination_root / source.relative_to(source_root)
        ensure_directory(destination.parent)
        if destination.exists() and not overwrite:
            continue
        shutil.copy2(source, destination)
        copied.append(destination)
    return copied


def main() -> int:
    args = parse_args()
    root = repo_root()
    vault = resolve_vault_path(args.vault, root)
    tracked_templates = template_root(root)

    if not tracked_templates.exists():
        raise SystemExit(f"Missing tracked template tree: {tracked_templates}")

    ensure_directory(vault)
    for relative_path in VAULT_DIRECTORIES:
        ensure_directory(vault / relative_path)

    copied = copy_tree(tracked_templates / "vault", vault, args.force)
    if args.write_obsidian_stubs:
        copied.extend(
            copy_tree(
                tracked_templates / "obsidian-stubs",
                vault / ".obsidian",
                args.force,
            )
        )

    print(f"Initialized Manuscript Wiki vault at {vault}")
    print(f"Created {len(VAULT_DIRECTORIES)} core directories")
    if copied:
        print(f"Copied {len(copied)} tracked template files")
    else:
        print("No tracked template files needed updating")

    if not args.no_next_steps:
        steps = ["Open the vault in Obsidian."]
        if args.write_obsidian_stubs:
            steps.append("Verify that the seeded core-plugin and Files & Links settings are present.")
        steps.extend(
            [
                f"Run `python3 scripts/install_obsidian_pdf_plus.py --vault {vault} --enable`.",
                f"Run `python3 scripts/sync_manuscript_wiki_pdfs.py --all --vault {vault}`.",
                f"Run `python3 scripts/generate_manuscript_wiki_notes.py --vault {vault}`.",
                f"Run `python3 scripts/lint_manuscript_wiki.py --vault {vault}`.",
            ]
        )
        print("\nNext steps:")
        for index, step in enumerate(steps, start=1):
            print(f"{index}. {step}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
