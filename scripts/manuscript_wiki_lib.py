#!/usr/bin/env python3

"""Shared helpers for the local Manuscript Wiki tooling."""

from __future__ import annotations

import csv
import hashlib
import json
import os
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


DEFAULT_VAULT_RELATIVE = Path(".local/obsidian/aether-manuscripts-wiki")
TEMPLATE_ROOT_RELATIVE = Path("tools/manuscript_wiki_template")
MANIFEST_RELATIVE = Path("07_logs/pdf_sync_manifest.json")
SOURCE_NOTE_RELATIVE = Path("02_sources/manuscripts")
REFERENCE_SOURCE_RELATIVE = Path("02_sources/references")
REFERENCE_RAW_RELATIVE = Path("01_raw/references/external")
REFERENCE_MANIFEST_RELATIVE = Path("07_logs/external_references_manifest.json")
REFERENCE_LIBRARY_RELATIVE = REFERENCE_SOURCE_RELATIVE / "external_reference_library.md"
ROUTING_INDEX_RELATIVE = Path("03_indexes/routing")
FAMILY_INDEX_RELATIVE = Path("03_indexes/families")
PRIORITY_INDEX_RELATIVE = Path("03_indexes/priorities")
LINES_RELATIVE = Path("04_lines")
CONCEPTS_RELATIVE = Path("05_concepts")

MANUAL_BLOCK_START = "<!-- MANUAL CONTENT START -->"
MANUAL_BLOCK_END = "<!-- MANUAL CONTENT END -->"

VAULT_DIRECTORIES = tuple(
    Path(path)
    for path in (
        ".obsidian",
        "01_raw/project_pdfs/active",
        "01_raw/project_pdfs/retired",
        "01_raw/project_pdfs/public_bundle",
        "01_raw/references/external",
        "01_raw/attachments",
        "02_sources/manuscripts",
        "02_sources/references",
        "03_indexes/routing",
        "03_indexes/families",
        "03_indexes/priorities",
        "04_lines",
        "05_concepts",
        "06_queries",
        "07_logs",
        "08_templates",
        "09_schema",
    )
)

PDF_SOURCE_BUCKETS = (
    {
        "category": "active",
        "repo_dir": Path("manuscripts/active/pdf"),
        "vault_dir": Path("01_raw/project_pdfs/active"),
    },
    {
        "category": "retired",
        "repo_dir": Path("manuscripts/retired/pdf"),
        "vault_dir": Path("01_raw/project_pdfs/retired"),
    },
    {
        "category": "public_bundle",
        "repo_dir": Path("docs/assets/pdfs"),
        "vault_dir": Path("01_raw/project_pdfs/public_bundle"),
    },
)

ROUTING_STATUSES = (
    "front_door",
    "active_primary",
    "active_supporting",
    "historical_but_kept_active",
    "screened_out",
    "side_work",
)

PROJECT_ROLES = (
    "flagship_package",
    "benchmark_gate",
    "benchmark_routing",
    "current_primary_chain",
    "supporting_main_chain",
    "screened_historical_branch",
    "side_continuation",
    "background_support",
)

FAMILY_NAMES = (
    "exact_closure",
    "benchmark_gatekeeping",
    "primitive_reservoir",
    "charge_polarization_exact_preservation",
    "higher_derivative",
    "general_substrate",
    "public_facing",
)

NOTE_FRONTMATTER_ORDER = (
    "file_name",
    "title",
    "family",
    "document_type",
    "project_role",
    "line_name",
    "frontline_status",
    "reading_priority",
    "sequence_stage",
    "status_reason",
    "benchmark_effect",
    "short_description",
    "current_use_rule",
    "upstream_dependency",
    "downstream_target",
    "relative_tex_path",
    "relative_repo_pdf_path",
    "relative_vault_pdf_path",
    "sha256",
    "repo_last_modified",
    "vault_last_synced",
    "map_last_known_relevance",
)

CONCEPT_DEFINITIONS = (
    {
        "title": "Æther",
        "slug": "aether",
        "summary": "The underlying four-dimensional substrate of reality.",
        "use_notes": "Use the active term `Æther` and verify manuscript-specific scientific claims in the active `.tex` source.",
        "source_docs": (
            "docs/AETHER_FLOW_NAMING_AND_VOCABULARY.md",
            "docs/AETHER_FLOW_CLAIM_BOUNDARY.md",
        ),
    },
    {
        "title": "Æther-flow",
        "slug": "aether-flow",
        "summary": "The intrinsic ordered motion of the Æther.",
        "use_notes": "Keep this term distinct from observed three-dimensional space and from any claim of completed substrate derivation.",
        "source_docs": (
            "docs/AETHER_FLOW_NAMING_AND_VOCABULARY.md",
            "docs/AETHER_FLOW_CLAIM_BOUNDARY.md",
        ),
    },
    {
        "title": "S-time",
        "slug": "s-time",
        "summary": "The experienced order of change arising from matter, light, and the Æther-flow.",
        "use_notes": "Treat this as approved vocabulary rather than a shortcut for a stronger physical claim.",
        "source_docs": (
            "docs/AETHER_FLOW_NAMING_AND_VOCABULARY.md",
            "docs/AETHER_FLOW_CLAIM_BOUNDARY.md",
        ),
    },
    {
        "title": "observed three-dimensional space",
        "slug": "observed-three-dimensional-space",
        "summary": "The observer-level local experiential slice of the deeper substrate.",
        "use_notes": "Use this wording in active notes instead of retired space-language variants.",
        "source_docs": (
            "docs/AETHER_FLOW_NAMING_AND_VOCABULARY.md",
        ),
    },
    {
        "title": "local experiential slice",
        "slug": "local-experiential-slice",
        "summary": "The slice language used for observer-level space within the deeper substrate picture.",
        "use_notes": "Preserve the distinction between the slice language and claims about the underlying four-dimensional substrate.",
        "source_docs": (
            "docs/AETHER_FLOW_NAMING_AND_VOCABULARY.md",
        ),
    },
    {
        "title": "exact closure",
        "slug": "exact-closure",
        "summary": "The benchmark stance in which the operational relativistic sector agrees exactly with GR.",
        "use_notes": "This is part of the benchmark package and does not by itself imply a first-principles substrate derivation.",
        "source_docs": (
            "docs/AETHER_FLOW_NAMING_AND_VOCABULARY.md",
            "docs/AETHER_FLOW_CLAIM_BOUNDARY.md",
        ),
    },
    {
        "title": "adoption",
        "slug": "adoption",
        "summary": "Use of established relativistic dynamics without claiming first-principles substrate recovery.",
        "use_notes": "Keep `adoption` sharply separated from `derivation` in generated notes and indexes.",
        "source_docs": (
            "docs/AETHER_FLOW_NAMING_AND_VOCABULARY.md",
        ),
    },
    {
        "title": "derivation",
        "slug": "derivation",
        "summary": "First-principles recovery of the relativistic sector from explicit substrate structure.",
        "use_notes": "Do not let a wiki summary promote adoption-level results into derivation-level claims.",
        "source_docs": (
            "docs/AETHER_FLOW_NAMING_AND_VOCABULARY.md",
            "docs/AETHER_FLOW_CLAIM_BOUNDARY.md",
        ),
    },
    {
        "title": "benchmark exact-closure package",
        "slug": "benchmark-exact-closure-package",
        "summary": "The overview-first benchmark package that fixes the public exact relativistic theory statement.",
        "use_notes": "Read this package before derivational routing and treat it as the automatic reversion point if a later bridge candidate fails.",
        "source_docs": (
            "docs/AETHER_FLOW_CLAIM_BOUNDARY.md",
        ),
    },
    {
        "title": "benchmark gatekeeping",
        "slug": "benchmark-gatekeeping",
        "summary": "The routing layer that determines whether a manuscript changes benchmark-facing status.",
        "use_notes": "Consult the file map and the benchmark-routing notes before naming the current main line or next honest burden.",
        "source_docs": (
            "docs/ACTIVE_MANUSCRIPT_FILE_MAP_GUIDE.md",
            "docs/AETHER_FLOW_CLAIM_BOUNDARY.md",
        ),
    },
    {
        "title": "current primary burden",
        "slug": "current-primary-burden",
        "summary": "The current open derivational burden identified by the routing layer and the current `active_primary` manuscript.",
        "use_notes": "Do not read this from stale prose summaries; resolve it from `docs/ACTIVE_MANUSCRIPT_FILE_MAP.csv`, the routing indexes, and the current `active_primary` source note.",
        "source_docs": (
            "docs/ACTIVE_MANUSCRIPT_FILE_MAP.csv",
            "docs/ACTIVE_MANUSCRIPT_FILE_MAP_GUIDE.md",
        ),
    },
)

CONCEPT_BY_TITLE = {concept["title"]: concept for concept in CONCEPT_DEFINITIONS}


@dataclass(frozen=True)
class PdfSource:
    category: str
    source_path: Path
    relative_repo_path: str
    relative_vault_path: str


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def template_root(root: Path | None = None) -> Path:
    base = root or repo_root()
    return base / TEMPLATE_ROOT_RELATIVE


def default_vault_path(root: Path | None = None) -> Path:
    base = root or repo_root()
    return base / DEFAULT_VAULT_RELATIVE


def resolve_vault_path(vault_arg: str | None, root: Path | None = None) -> Path:
    base = root or repo_root()
    if not vault_arg:
        return default_vault_path(base)
    candidate = Path(vault_arg).expanduser()
    if candidate.is_absolute():
        return candidate.resolve()
    return (base / candidate).resolve()


def ensure_directory(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def iso_from_timestamp(timestamp: float) -> str:
    return datetime.fromtimestamp(timestamp, tz=timezone.utc).replace(
        microsecond=0
    ).isoformat()


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def relative_to_repo(path: Path, root: Path | None = None) -> str:
    base = root or repo_root()
    return path.resolve().relative_to(base).as_posix()


def markdown_link(source_file: Path, target: Path, label: str) -> str:
    relative = os.path.relpath(target, start=source_file.parent)
    return f"[{label}]({Path(relative).as_posix()})"


def wiki_link(path: Path | str, label: str | None = None) -> str:
    target = Path(path).as_posix() if isinstance(path, Path) else path
    return f"[[{target}|{label}]]" if label else f"[[{target}]]"


def load_file_map_rows(root: Path | None = None) -> list[dict[str, str]]:
    base = root or repo_root()
    csv_path = base / "docs/ACTIVE_MANUSCRIPT_FILE_MAP.csv"
    with csv_path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        rows = []
        for raw_row in reader:
            row = {key: (value or "").strip() for key, value in raw_row.items()}
            if any(row.values()):
                rows.append(row)
    return rows


def file_map_index(root: Path | None = None) -> dict[str, dict[str, str]]:
    return {row["file_name"]: row for row in load_file_map_rows(root)}


def deterministic_vault_pdf_relative_path(relative_repo_pdf_path: str) -> str:
    repo_path = Path(relative_repo_pdf_path)
    for bucket in PDF_SOURCE_BUCKETS:
        repo_dir = bucket["repo_dir"].as_posix()
        if relative_repo_pdf_path.startswith(f"{repo_dir}/"):
            return (bucket["vault_dir"] / repo_path.name).as_posix()
    raise ValueError(f"Unsupported repo PDF path: {relative_repo_pdf_path}")


def source_note_relative_path(file_name: str) -> Path:
    return SOURCE_NOTE_RELATIVE / f"{Path(file_name).stem}.md"


def reference_note_relative_path(reference_id: str) -> Path:
    return REFERENCE_SOURCE_RELATIVE / f"{reference_id}.md"


def line_relative_path(line_name: str) -> Path:
    return LINES_RELATIVE / f"{line_name}.md"


def routing_relative_path(status: str) -> Path:
    return ROUTING_INDEX_RELATIVE / f"{status}.md"


def family_relative_path(family: str) -> Path:
    return FAMILY_INDEX_RELATIVE / f"{family}.md"


def priority_relative_path(role: str) -> Path:
    return PRIORITY_INDEX_RELATIVE / f"{role}.md"


def concept_relative_path(title: str) -> Path:
    return CONCEPTS_RELATIVE / f"{CONCEPT_BY_TITLE[title]['slug']}.md"


def concept_link(title: str) -> str:
    return wiki_link(concept_relative_path(title), title)


def load_manifest(vault_root: Path) -> dict[str, object]:
    manifest_path = vault_root / MANIFEST_RELATIVE
    if not manifest_path.exists():
        return {"generated_at": "", "entries": [], "stale_actions": []}
    with manifest_path.open(encoding="utf-8") as handle:
        return json.load(handle)


def manifest_index(manifest: dict[str, object]) -> dict[str, dict[str, object]]:
    entries = manifest.get("entries", [])
    index: dict[str, dict[str, object]] = {}
    if isinstance(entries, list):
        for entry in entries:
            if isinstance(entry, dict):
                key = str(entry.get("relative_repo_path", ""))
                if key:
                    index[key] = entry
    return index


def write_json(path: Path, payload: object) -> None:
    ensure_directory(path.parent)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, ensure_ascii=False, sort_keys=False)
        handle.write("\n")


def write_text(path: Path, content: str) -> None:
    ensure_directory(path.parent)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def render_frontmatter(values: dict[str, str]) -> str:
    lines = ["---"]
    for key in NOTE_FRONTMATTER_ORDER:
        lines.append(f"{key}: {json.dumps(values.get(key, ''), ensure_ascii=False)}")
    lines.append("---")
    return "\n".join(lines)


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    closing = text.find("\n---\n", 4)
    if closing == -1:
        return {}
    data: dict[str, str] = {}
    for line in text[4:closing].splitlines():
        if not line.strip() or ":" not in line:
            continue
        key, raw_value = line.split(":", 1)
        key = key.strip()
        raw_value = raw_value.strip()
        if not key:
            continue
        if raw_value.startswith('"'):
            try:
                data[key] = json.loads(raw_value)
            except json.JSONDecodeError:
                data[key] = raw_value.strip('"')
        else:
            data[key] = raw_value
    return data


def extract_manual_block(existing_text: str | None, default_body: str) -> str:
    if existing_text:
        start = existing_text.find(MANUAL_BLOCK_START)
        end = existing_text.find(MANUAL_BLOCK_END)
        if start != -1 and end != -1 and start < end:
            inner = existing_text[start + len(MANUAL_BLOCK_START) : end].strip()
            if inner:
                return inner
    return default_body.strip()


def render_manual_block(body: str) -> str:
    return (
        f"{MANUAL_BLOCK_START}\n"
        f"{body.strip()}\n"
        f"{MANUAL_BLOCK_END}"
    )


def list_pdf_sources(root: Path | None = None) -> list[PdfSource]:
    base = root or repo_root()
    sources: list[PdfSource] = []
    for bucket in PDF_SOURCE_BUCKETS:
        repo_dir = base / bucket["repo_dir"]
        vault_dir = bucket["vault_dir"]
        for source_path in sorted(repo_dir.glob("*.pdf")):
            sources.append(
                PdfSource(
                    category=str(bucket["category"]),
                    source_path=source_path,
                    relative_repo_path=relative_to_repo(source_path, base),
                    relative_vault_path=(vault_dir / source_path.name).as_posix(),
                )
            )
    return sources


def read_text_if_exists(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def slugify(value: str) -> str:
    slug_chars: list[str] = []
    previous_dash = False
    for char in value.lower():
        if char.isalnum():
            slug_chars.append(char)
            previous_dash = False
            continue
        if slug_chars and not previous_dash:
            slug_chars.append("-")
            previous_dash = True
    slug = "".join(slug_chars).strip("-")
    return slug or "reference"
