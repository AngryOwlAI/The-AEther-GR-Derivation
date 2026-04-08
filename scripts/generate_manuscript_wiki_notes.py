#!/usr/bin/env python3

"""Generate Manuscript Wiki source notes, indexes, line pages, and concept seeds."""

from __future__ import annotations

import argparse
from pathlib import Path

from manuscript_wiki_lib import (
    CONCEPT_DEFINITIONS,
    FAMILY_NAMES,
    FAMILY_INDEX_RELATIVE,
    LINES_RELATIVE,
    MANUAL_BLOCK_END,
    MANUAL_BLOCK_START,
    MANIFEST_RELATIVE,
    PRIORITY_INDEX_RELATIVE,
    PROJECT_ROLES,
    ROUTING_INDEX_RELATIVE,
    ROUTING_STATUSES,
    concept_link,
    concept_relative_path,
    deterministic_vault_pdf_relative_path,
    ensure_directory,
    extract_manual_block,
    family_relative_path,
    file_map_index,
    iso_from_timestamp,
    line_relative_path,
    load_file_map_rows,
    load_manifest,
    manifest_index,
    markdown_link,
    parse_frontmatter,
    priority_relative_path,
    read_text_if_exists,
    render_frontmatter,
    render_manual_block,
    repo_root,
    resolve_vault_path,
    routing_relative_path,
    source_note_relative_path,
    wiki_link,
    write_text,
)


GENERATED_NOTICE = (
    "> Generated from `docs/ACTIVE_MANUSCRIPT_FILE_MAP.csv` and the local sync "
    "manifest. Treat this note as a retrieval layer and verify scientific claims "
    "in the active `.tex` source."
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Generate Manuscript Wiki source notes, routing indexes, family pages, "
            "line pages, and concept seed pages."
        )
    )
    parser.add_argument(
        "--vault",
        help=(
            "Vault path to generate into. Defaults to "
            ".local/obsidian/aether-manuscripts-wiki inside the repository."
        ),
    )
    parser.add_argument(
        "--one",
        metavar="IDENTIFIER",
        help=(
            "Refresh one manuscript note by file name, relative path, PDF path, or stem. "
            "Index and concept pages are still regenerated."
        ),
    )
    return parser.parse_args()


def select_rows(rows: list[dict[str, str]], identifier: str | None) -> list[dict[str, str]]:
    if not identifier:
        return rows

    needle = identifier.strip()
    stem = Path(needle).stem
    matches = [
        row
        for row in rows
        if needle in {row["file_name"], row["relative_path"], row["pdf_path"]}
        or stem == Path(row["file_name"]).stem
    ]
    if not matches:
        raise SystemExit(f"Could not match manuscript row for --one {identifier}")
    if len(matches) > 1:
        raise SystemExit(
            "Ambiguous --one identifier. Pass a full file name or repository-relative path."
        )
    return matches


def table_escape(value: str) -> str:
    return value.replace("|", r"\|").replace("\n", " ").strip()


def render_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> str:
    header_line = "| " + " | ".join(headers) + " |"
    divider_line = "| " + " | ".join(["---"] * len(headers)) + " |"
    body_lines = [
        "| " + " | ".join(table_escape(cell) for cell in row) + " |" for row in rows
    ]
    return "\n".join([header_line, divider_line, *body_lines])


def build_note_frontmatter(
    row: dict[str, str],
    root: Path,
    vault: Path,
    manifest_lookup: dict[str, dict[str, object]],
) -> dict[str, str]:
    repo_pdf_path = root / row["pdf_path"]
    expected_vault_pdf_path = deterministic_vault_pdf_relative_path(row["pdf_path"])
    manifest_entry = manifest_lookup.get(row["pdf_path"], {})

    frontmatter = {
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
        "relative_vault_pdf_path": expected_vault_pdf_path,
        "sha256": str(manifest_entry.get("sha256", "")),
        "repo_last_modified": (
            iso_from_timestamp(repo_pdf_path.stat().st_mtime) if repo_pdf_path.exists() else ""
        ),
        "vault_last_synced": str(manifest_entry.get("synced_at", "")),
        "map_last_known_relevance": row["last_known_relevance"],
    }
    return frontmatter


def render_source_note(
    row: dict[str, str],
    frontmatter: dict[str, str],
    root: Path,
    vault: Path,
) -> str:
    note_path = vault / source_note_relative_path(row["file_name"])
    existing_text = read_text_if_exists(note_path)
    manual_block = extract_manual_block(
        existing_text,
        "## Manual Notes\n\n- Add local PDF++ links, excerpt notes, or routing questions here.",
    )

    tex_link = markdown_link(note_path, root / row["relative_path"], "Active TeX source")
    repo_pdf_link = markdown_link(note_path, root / row["pdf_path"], "Repository PDF")
    local_pdf_link = wiki_link(Path(frontmatter["relative_vault_pdf_path"]))
    routing_link = wiki_link(routing_relative_path(row["frontline_status"]))
    family_link = wiki_link(family_relative_path(row["family"]))
    priority_link = wiki_link(priority_relative_path(row["project_role"]))
    line_link = wiki_link(line_relative_path(row["line_name"]))

    if row["frontline_status"] in {"active_primary", "active_supporting"}:
        open_burden = row["downstream_target"]
    else:
        open_burden = (
            "This note preserves routing context rather than setting the live burden by "
            f"itself. Current handoff: {row['downstream_target']}"
        )

    routing_table = render_table(
        ("Field", "Value"),
        [
            ("Front-line status", f"`{row['frontline_status']}`"),
            ("Project role", f"`{row['project_role']}`"),
            ("Family", f"`{row['family']}`"),
            ("Line", f"`{row['line_name']}`"),
            ("Reading priority", f"`{row['reading_priority']}`"),
            ("Sequence stage", f"`{row['sequence_stage']}`"),
        ],
    )

    metadata_table = render_table(
        ("Field", "Value"),
        [
            ("Repo PDF hash", frontmatter["sha256"] or "(not yet synced)"),
            ("Repo PDF modified", frontmatter["repo_last_modified"] or "(missing)"),
            ("Vault last synced", frontmatter["vault_last_synced"] or "(not yet synced)"),
            ("Repository PDF path", frontmatter["relative_repo_pdf_path"]),
            ("Vault PDF path", frontmatter["relative_vault_pdf_path"]),
            ("Routing audit", frontmatter["map_last_known_relevance"]),
        ],
    )

    concept_lines = "\n".join(
        f"- {concept_link(concept['title'])}" for concept in CONCEPT_DEFINITIONS
    )

    content = "\n\n".join(
        [
            render_frontmatter(frontmatter),
            f"# {row['title']}",
            GENERATED_NOTICE,
            "## Routing Status\n\n" + routing_table,
            "## Short Summary\n\n" + row["short_description"],
            "## Benchmark Effect\n\n" + row["benchmark_effect"],
            "## Current Use Rule\n\n" + row["current_use_rule"],
            "## Upstream Dependency\n\n" + row["upstream_dependency"],
            "## Downstream Target\n\n" + row["downstream_target"],
            "## Open Burden\n\n" + open_burden,
            "## Related Manuscripts\n\n"
            + "\n".join(
                [
                    f"- {tex_link}",
                    f"- {repo_pdf_link}",
                    f"- Local vault PDF: {local_pdf_link}",
                    f"- Routing index: {routing_link}",
                    f"- Project-role index: {priority_link}",
                    f"- Family index: {family_link}",
                    f"- Line page: {line_link}",
                ]
            ),
            "## Related Concepts\n\n" + concept_lines,
            "## PDF Deep Links\n\n"
            + "\n".join(
                [
                    f"- Local PDF: {local_pdf_link}",
                    "- Add page-level or selection-level PDF++ links in the manual block below when needed.",
                ]
            ),
            "## Build And Sync Metadata\n\n" + metadata_table,
            render_manual_block(manual_block),
        ]
    )
    return content


def render_index_page(
    title: str,
    intro: str,
    rows: list[dict[str, str]],
    page_path: Path,
    vault: Path,
) -> str:
    table_rows = [
        (
            markdown_link(
                page_path,
                vault / source_note_relative_path(row["file_name"]),
                row["title"],
            ),
            f"`{row['frontline_status']}`",
            f"`{row['project_role']}`",
            f"`{row['line_name']}`",
            f"`{row['sequence_stage']}`",
            row["short_description"],
        )
        for row in rows
    ]
    body = (
        "No entries currently map to this index page."
        if not table_rows
        else render_table(
            ("Manuscript", "Status", "Role", "Line", "Sequence", "Summary"),
            table_rows,
        )
    )
    return "\n\n".join(
        [
            f"# {title}",
            GENERATED_NOTICE,
            intro,
            "## Entries\n\n" + body,
        ]
    )


def render_concept_page(concept: dict[str, object], vault: Path) -> str:
    concept_path = vault / concept_relative_path(str(concept["title"]))
    existing_text = read_text_if_exists(concept_path)
    manual_block = extract_manual_block(
        existing_text,
        "## Manual Notes\n\n- Add local cross-links, PDF++ references, or manuscript-specific annotations here.",
    )
    source_refs = "\n".join(
        f"- `{source_doc}`" for source_doc in concept.get("source_docs", [])
    )
    return "\n\n".join(
        [
            f"# {concept['title']}",
            GENERATED_NOTICE,
            "## Canonical Meaning\n\n" + str(concept["summary"]),
            "## Usage Notes\n\n" + str(concept["use_notes"]),
            "## Source References\n\n" + source_refs,
            render_manual_block(manual_block),
        ]
    )


def write_index_pages(rows: list[dict[str, str]], vault: Path) -> int:
    written = 0

    for status in ROUTING_STATUSES:
        page_rows = [row for row in rows if row["frontline_status"] == status]
        page_path = vault / routing_relative_path(status)
        content = render_index_page(
            title=f"Routing Index: {status}",
            intro=(
                "Generated directly from the routing layer. Use this page to locate "
                "manuscripts, then verify routing claims against the file map."
            ),
            rows=page_rows,
            page_path=page_path,
            vault=vault,
        )
        write_text(page_path, content)
        written += 1

    for family in FAMILY_NAMES:
        page_rows = [row for row in rows if row["family"] == family]
        page_path = vault / family_relative_path(family)
        content = render_index_page(
            title=f"Family Index: {family}",
            intro=(
                "This page groups manuscripts by lineage family, not by present-day "
                "routing priority."
            ),
            rows=page_rows,
            page_path=page_path,
            vault=vault,
        )
        write_text(page_path, content)
        written += 1

    for role in PROJECT_ROLES:
        page_rows = [row for row in rows if row["project_role"] == role]
        page_path = vault / priority_relative_path(role)
        content = render_index_page(
            title=f"Project-Role Index: {role}",
            intro=(
                "This page groups manuscripts by repository job so benchmark package, "
                "routing, and main-line roles stay distinct."
            ),
            rows=page_rows,
            page_path=page_path,
            vault=vault,
        )
        write_text(page_path, content)
        written += 1

    for line_name in sorted({row["line_name"] for row in rows}):
        page_rows = [row for row in rows if row["line_name"] == line_name]
        page_path = vault / line_relative_path(line_name)
        content = render_index_page(
            title=f"Line Page: {line_name}",
            intro=(
                "This page follows one manuscript line. Use the routing status column to "
                "distinguish the live frontier from preserved history."
            ),
            rows=page_rows,
            page_path=page_path,
            vault=vault,
        )
        write_text(page_path, content)
        written += 1

    return written


def main() -> int:
    args = parse_args()
    root = repo_root()
    vault = resolve_vault_path(args.vault, root)
    ensure_directory(vault)

    rows = load_file_map_rows(root)
    selected_rows = select_rows(rows, args.one)
    manifest_lookup = manifest_index(load_manifest(vault))

    notes_written = 0
    for row in selected_rows:
        frontmatter = build_note_frontmatter(row, root, vault, manifest_lookup)
        note_path = vault / source_note_relative_path(row["file_name"])
        write_text(note_path, render_source_note(row, frontmatter, root, vault))
        notes_written += 1

    index_pages_written = write_index_pages(rows, vault)

    concept_pages_written = 0
    for concept in CONCEPT_DEFINITIONS:
        concept_path = vault / concept_relative_path(str(concept["title"]))
        write_text(concept_path, render_concept_page(concept, vault))
        concept_pages_written += 1

    print(f"Generated {notes_written} manuscript note(s) in {vault}")
    print(f"Generated {index_pages_written} index/line page(s)")
    print(f"Generated {concept_pages_written} concept page(s)")
    print(f"Manifest source: {vault / MANIFEST_RELATIVE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
