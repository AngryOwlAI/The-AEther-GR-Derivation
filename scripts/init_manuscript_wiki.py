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
    parser.add_argument(
        "--write-obsidian-stubs",
        action="store_true",
        help="Copy the tracked Obsidian config stubs into .obsidian/.",
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
        print("\nNext steps:")
        print("1. Open the vault in Obsidian.")
        print("2. Install the PDF++ community plugin.")
        print(
            "3. Run `python3 scripts/sync_manuscript_wiki_pdfs.py --all"
            f" --vault {vault}`."
        )
        print(
            "4. Run `python3 scripts/generate_manuscript_wiki_notes.py"
            f" --vault {vault}`."
        )
        print(
            "5. Run `python3 scripts/lint_manuscript_wiki.py"
            f" --vault {vault}`."
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
