#!/usr/bin/env python3

"""Install the PDF++ Obsidian community plugin into a local vault."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from urllib.request import Request, urlopen

from manuscript_wiki_lib import ensure_directory, repo_root, resolve_vault_path, write_text


PLUGIN_ID = "pdf-plus"
PLUGIN_FILES = ("manifest.json", "main.js", "styles.css")
LATEST_RELEASE_BASE = (
    "https://github.com/RyotaUshio/obsidian-pdf-plus/releases/latest/download"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Download the PDF++ community plugin into a local Obsidian vault and "
            "optionally enable it in community-plugins.json."
        )
    )
    parser.add_argument(
        "--vault",
        help=(
            "Vault path to update. Defaults to "
            ".local/obsidian/aether-manuscripts-wiki inside the repository."
        ),
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite any existing plugin files.",
    )
    parser.add_argument(
        "--enable",
        action="store_true",
        help="Add PDF++ to .obsidian/community-plugins.json after download.",
    )
    return parser.parse_args()


def download_text(url: str) -> bytes:
    request = Request(url, headers={"User-Agent": "manuscript-wiki-bootstrap/1.0"})
    with urlopen(request) as response:
        return response.read()


def load_enabled_plugins(path: Path) -> list[str]:
    if not path.exists():
        return []
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON in {path}: {exc}") from exc
    if not isinstance(payload, list) or not all(isinstance(item, str) for item in payload):
        raise SystemExit(f"Expected a JSON string array in {path}")
    return payload


def main() -> int:
    args = parse_args()
    root = repo_root()
    vault = resolve_vault_path(args.vault, root)

    if not vault.exists():
        raise SystemExit(f"Vault does not exist: {vault}")
    plugin_dir = ensure_directory(vault / ".obsidian" / "plugins" / PLUGIN_ID)

    downloaded = 0
    for file_name in PLUGIN_FILES:
        target = plugin_dir / file_name
        if target.exists() and not args.force:
            continue
        payload = download_text(f"{LATEST_RELEASE_BASE}/{file_name}")
        target.write_bytes(payload)
        downloaded += 1

    manifest_path = plugin_dir / "manifest.json"
    if not manifest_path.exists():
        raise SystemExit(f"PDF++ install did not produce {manifest_path}")

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("id") != PLUGIN_ID:
        raise SystemExit(
            "Downloaded manifest did not match the expected plugin id "
            f"{PLUGIN_ID!r}: {manifest.get('id')!r}"
        )

    enabled = False
    if args.enable:
        community_plugins_path = vault / ".obsidian" / "community-plugins.json"
        plugins = load_enabled_plugins(community_plugins_path)
        if PLUGIN_ID not in plugins:
            plugins.append(PLUGIN_ID)
            plugins.sort()
            write_text(
                community_plugins_path,
                json.dumps(plugins, indent=2, ensure_ascii=False),
            )
        enabled = True

    print(f"Installed PDF++ into {plugin_dir}")
    print(f"Plugin version: {manifest.get('version', '(unknown)')}")
    print(f"Downloaded {downloaded} file(s)")
    if enabled:
        print(f"Enabled {PLUGIN_ID} in {vault / '.obsidian' / 'community-plugins.json'}")
    else:
        print(
            "Plugin files were downloaded but not auto-enabled. "
            "Use --enable to add PDF++ to community-plugins.json."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
