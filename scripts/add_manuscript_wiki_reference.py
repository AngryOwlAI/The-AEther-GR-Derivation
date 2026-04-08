#!/usr/bin/env python3

"""Add or refresh supplemental external-reference PDFs in the local Manuscript Wiki."""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

from manuscript_wiki_lib import (
    MANUAL_BLOCK_END,
    MANUAL_BLOCK_START,
    REFERENCE_LIBRARY_RELATIVE,
    REFERENCE_MANIFEST_RELATIVE,
    REFERENCE_RAW_RELATIVE,
    ensure_directory,
    extract_manual_block,
    file_sha256,
    now_iso,
    read_text_if_exists,
    reference_note_relative_path,
    render_manual_block,
    repo_root,
    resolve_vault_path,
    slugify,
    wiki_link,
    write_json,
    write_text,
)


REFERENCE_KINDS = (
    "reference_paper",
    "benchmark_gr_reference",
    "methodological_paper",
    "project_adjacent_literature",
)

REFERENCE_FRONTMATTER_ORDER = (
    "reference_id",
    "title",
    "authors",
    "year",
    "literature_kind",
    "source_file_name",
    "relative_vault_pdf_path",
    "source_url",
    "doi",
    "citation_key",
    "project_relevance",
    "summary",
    "tags",
    "sha256",
    "added_at",
    "last_synced",
)

GENERATED_NOTICE = (
    "> Generated from the external reference manifest. Treat this note as "
    "supplemental literature only: it does not determine manuscript routing, "
    "front-line status, or the benchmark claim boundary."
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Add a supplemental external-reference PDF to the local Manuscript Wiki "
            "or rebuild the external-reference library page."
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
        "--pdf",
        help="Path to a local external-reference PDF to ingest.",
    )
    parser.add_argument(
        "--title",
        help="Reference title. Required when --pdf is provided.",
    )
    parser.add_argument(
        "--authors",
        default="",
        help="Author string for the reference note.",
    )
    parser.add_argument(
        "--year",
        default="",
        help="Publication year for the reference note.",
    )
    parser.add_argument(
        "--kind",
        choices=REFERENCE_KINDS,
        default="reference_paper",
        help="Reference classification inside the wiki.",
    )
    parser.add_argument(
        "--slug",
        help="Optional stable note/pdf slug. Defaults to a slugified title.",
    )
    parser.add_argument(
        "--source-url",
        default="",
        help="Optional canonical source URL for the reference.",
    )
    parser.add_argument(
        "--doi",
        default="",
        help="Optional DOI string.",
    )
    parser.add_argument(
        "--citation-key",
        default="",
        help="Optional citation key for local referencing.",
    )
    parser.add_argument(
        "--project-relevance",
        default="",
        help="Short explanation of why the reference matters to this project.",
    )
    parser.add_argument(
        "--summary",
        default="",
        help="Short note-level summary of the reference.",
    )
    parser.add_argument(
        "--tags",
        default="",
        help="Comma-separated local tags for the reference note.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite an existing external-reference PDF entry even if the file hash changes.",
    )
    parser.add_argument(
        "--rebuild-index-only",
        action="store_true",
        help="Refresh the external-reference library note from the current manifest without ingesting a PDF.",
    )
    args = parser.parse_args()
    if args.rebuild_index_only:
        return args
    if not args.pdf:
        raise SystemExit("Provide --pdf to ingest a reference, or use --rebuild-index-only.")
    if not args.title:
        raise SystemExit("Provide --title when ingesting a reference PDF.")
    return args


def render_frontmatter(values: dict[str, str]) -> str:
    lines = ["---"]
    for key in REFERENCE_FRONTMATTER_ORDER:
        lines.append(f"{key}: {json.dumps(values.get(key, ''), ensure_ascii=False)}")
    lines.append("---")
    return "\n".join(lines)


def table_escape(value: str) -> str:
    return value.replace("|", r"\|").replace("\n", " ").strip()


def render_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> str:
    header_line = "| " + " | ".join(headers) + " |"
    divider_line = "| " + " | ".join(["---"] * len(headers)) + " |"
    body_lines = [
        "| " + " | ".join(table_escape(cell) for cell in row) + " |" for row in rows
    ]
    return "\n".join([header_line, divider_line, *body_lines])


def load_reference_manifest(vault: Path) -> dict[str, object]:
    manifest_path = vault / REFERENCE_MANIFEST_RELATIVE
    if not manifest_path.exists():
        return {"updated_at": "", "vault_root": str(vault), "entries": []}
    return json.loads(manifest_path.read_text(encoding="utf-8"))


def reference_manifest_index(manifest: dict[str, object]) -> dict[str, dict[str, object]]:
    entries = manifest.get("entries", [])
    index: dict[str, dict[str, object]] = {}
    if isinstance(entries, list):
        for entry in entries:
            if isinstance(entry, dict):
                key = str(entry.get("reference_id", ""))
                if key:
                    index[key] = entry
    return index


def render_reference_note(entry: dict[str, str], vault: Path) -> str:
    note_path = vault / reference_note_relative_path(entry["reference_id"])
    existing_text = read_text_if_exists(note_path)
    manual_block = extract_manual_block(
        existing_text,
        "## Manual Notes\n\n- Add project-specific excerpts, PDF++ links, or comparison notes here.",
    )

    status_table = render_table(
        ("Field", "Value"),
        [
            ("Literature kind", f"`{entry['literature_kind']}`"),
            ("Authors", entry["authors"] or "(not provided)"),
            ("Year", entry["year"] or "(not provided)"),
            ("Citation key", entry["citation_key"] or "(not provided)"),
        ],
    )
    metadata_table = render_table(
        ("Field", "Value"),
        [
            ("Local PDF", wiki_link(entry["relative_vault_pdf_path"])),
            ("Source URL", entry["source_url"] or "(not provided)"),
            ("DOI", entry["doi"] or "(not provided)"),
            ("Tags", entry["tags"] or "(not provided)"),
            ("SHA-256", entry["sha256"]),
            ("Added", entry["added_at"]),
            ("Last synced", entry["last_synced"]),
        ],
    )

    summary = entry["summary"] or "No reference summary has been added yet."
    relevance = (
        entry["project_relevance"]
        or "Supplemental literature only. Use it to support reading, comparison, or context, not to set repository routing."
    )

    return "\n\n".join(
        [
            render_frontmatter(entry),
            f"# {entry['title']}",
            GENERATED_NOTICE,
            "## Reference Status\n\n" + status_table,
            "## Project Relevance\n\n" + relevance,
            "## Summary\n\n" + summary,
            "## Access\n\n"
            + "\n".join(
                [
                    f"- Local PDF: {wiki_link(entry['relative_vault_pdf_path'])}",
                    f"- Library index: {wiki_link(REFERENCE_LIBRARY_RELATIVE)}",
                    f"- Source URL: {entry['source_url'] or '(not provided)'}",
                    f"- DOI: {entry['doi'] or '(not provided)'}",
                ]
            ),
            "## Separation Rule\n\n"
            + "This note is supplemental external literature. It does not change any "
            + "project manuscript `frontline_status`, `project_role`, benchmark-routing claim, or active burden statement.",
            "## Build And Sync Metadata\n\n" + metadata_table,
            render_manual_block(manual_block),
        ]
    )


def render_reference_library(entries: list[dict[str, str]], vault: Path) -> str:
    library_path = vault / REFERENCE_LIBRARY_RELATIVE
    existing_text = read_text_if_exists(library_path)
    manual_block = extract_manual_block(
        existing_text,
        "## Manual Notes\n\n- Record curation priorities, reading queues, or literature clustering notes here.",
    )

    rows = [
        (
            wiki_link(reference_note_relative_path(entry["reference_id"]), entry["title"]),
            f"`{entry['literature_kind']}`",
            entry["authors"] or "(not provided)",
            entry["year"] or "(not provided)",
            entry["project_relevance"] or "(not provided)",
        )
        for entry in entries
    ]
    body = (
        "No external references have been ingested yet."
        if not rows
        else render_table(
            ("Reference", "Kind", "Authors", "Year", "Project Relevance"),
            rows,
        )
    )

    return "\n\n".join(
        [
            "# External Reference Library",
            GENERATED_NOTICE,
            "This page tracks supplemental external literature only. Project routing remains controlled by `docs/ACTIVE_MANUSCRIPT_FILE_MAP.csv` and the project manuscript notes generated from it.",
            "## Entries\n\n" + body,
            render_manual_block(manual_block),
        ]
    )


def main() -> int:
    args = parse_args()
    root = repo_root()
    vault = resolve_vault_path(args.vault, root)
    ensure_directory(vault)
    ensure_directory(vault / REFERENCE_RAW_RELATIVE)
    ensure_directory(vault / reference_note_relative_path("placeholder").parent)

    manifest = load_reference_manifest(vault)
    entry_lookup = reference_manifest_index(manifest)
    updated_at = now_iso()

    if not args.rebuild_index_only:
        source_pdf = Path(args.pdf).expanduser()
        if not source_pdf.is_absolute():
            source_pdf = (root / source_pdf).resolve()
        if not source_pdf.exists():
            raise SystemExit(f"Missing reference PDF: {source_pdf}")
        if source_pdf.suffix.lower() != ".pdf":
            raise SystemExit(f"Expected a PDF file, got: {source_pdf}")

        reference_id = args.slug or slugify(args.title)
        destination_pdf = vault / REFERENCE_RAW_RELATIVE / f"{reference_id}.pdf"
        source_hash = file_sha256(source_pdf)
        existing_entry = entry_lookup.get(reference_id, {})

        if destination_pdf.exists():
            existing_hash = file_sha256(destination_pdf)
            if existing_hash != source_hash and not args.force:
                raise SystemExit(
                    f"External reference already exists with a different PDF hash: {destination_pdf}. "
                    "Pass --force to replace it."
                )
        if args.force or not destination_pdf.exists() or file_sha256(destination_pdf) != source_hash:
            shutil.copy2(source_pdf, destination_pdf)

        entry = {
            "reference_id": reference_id,
            "title": args.title,
            "authors": args.authors.strip(),
            "year": args.year.strip(),
            "literature_kind": args.kind,
            "source_file_name": source_pdf.name,
            "relative_vault_pdf_path": (REFERENCE_RAW_RELATIVE / f"{reference_id}.pdf").as_posix(),
            "source_url": args.source_url.strip(),
            "doi": args.doi.strip(),
            "citation_key": args.citation_key.strip(),
            "project_relevance": args.project_relevance.strip(),
            "summary": args.summary.strip(),
            "tags": args.tags.strip(),
            "sha256": file_sha256(destination_pdf),
            "added_at": str(existing_entry.get("added_at", updated_at)),
            "last_synced": updated_at,
        }
        entry_lookup[reference_id] = entry
        write_text(vault / reference_note_relative_path(reference_id), render_reference_note(entry, vault))
        print(f"Ingested external reference PDF into {destination_pdf}")
        print(f"Wrote reference note {vault / reference_note_relative_path(reference_id)}")

    entries = sorted(
        (
            {key: str(value) for key, value in entry.items()}
            for entry in entry_lookup.values()
        ),
        key=lambda item: (item["literature_kind"], item["year"], item["title"].lower()),
    )
    manifest_payload = {
        "updated_at": updated_at,
        "vault_root": str(vault),
        "entries": entries,
    }
    write_json(vault / REFERENCE_MANIFEST_RELATIVE, manifest_payload)
    write_text(vault / REFERENCE_LIBRARY_RELATIVE, render_reference_library(entries, vault))

    print(f"External reference manifest: {vault / REFERENCE_MANIFEST_RELATIVE}")
    print(f"External reference library: {vault / REFERENCE_LIBRARY_RELATIVE}")
    print(f"Reference entries: {len(entries)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
