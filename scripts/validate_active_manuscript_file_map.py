#!/usr/bin/env python3

"""Validate docs/ACTIVE_MANUSCRIPT_FILE_MAP.csv against the active TeX tree."""

from __future__ import annotations

import csv
import sys
from pathlib import Path


REQUIRED_COLUMNS = [
    "file_name",
    "relative_path",
    "pdf_path",
    "title",
    "family",
    "document_type",
    "project_role",
    "line_name",
    "frontline_status",
    "status_reason",
    "reading_priority",
    "sequence_stage",
    "upstream_dependency",
    "downstream_target",
    "benchmark_effect",
    "short_description",
    "current_use_rule",
    "last_known_relevance",
]


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def load_rows(csv_path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with csv_path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        fieldnames = reader.fieldnames or []
        rows = []
        for raw_row in reader:
            row = {key: (value or "").strip() for key, value in raw_row.items()}
            if any(row.values()):
                rows.append(row)
    return fieldnames, rows


def expected_relative_path(file_name: str) -> str:
    return f"manuscripts/active/tex/{file_name}"


def expected_pdf_path(file_name: str) -> str:
    return f"manuscripts/active/pdf/{Path(file_name).stem}.pdf"


def validate() -> list[str]:
    root = repo_root()
    csv_path = root / "docs/ACTIVE_MANUSCRIPT_FILE_MAP.csv"
    tex_root = root / "manuscripts/active/tex"

    errors: list[str] = []

    if not csv_path.exists():
        return [f"Missing CSV inventory: {csv_path}"]

    fieldnames, rows = load_rows(csv_path)
    missing_columns = [column for column in REQUIRED_COLUMNS if column not in fieldnames]
    if missing_columns:
        errors.append(
            "CSV is missing required columns: " + ", ".join(missing_columns)
        )

    tex_files = sorted(tex_root.glob("*.tex"))
    active_names = {path.name for path in tex_files}

    row_names: list[str] = []
    row_relative_paths: list[str] = []

    for index, row in enumerate(rows, start=2):
        missing_values = [column for column in REQUIRED_COLUMNS if not row.get(column, "")]
        if missing_values:
            errors.append(
                f"CSV row {index} is missing values for: {', '.join(missing_values)}"
            )

        file_name = row.get("file_name", "")
        relative_path = row.get("relative_path", "")
        pdf_path = row.get("pdf_path", "")

        if file_name:
            row_names.append(file_name)
            expected_rel = expected_relative_path(file_name)
            expected_pdf = expected_pdf_path(file_name)

            if relative_path and relative_path != expected_rel:
                errors.append(
                    f"{file_name}: relative_path should be {expected_rel}, found {relative_path}"
                )

            if pdf_path and pdf_path != expected_pdf:
                errors.append(
                    f"{file_name}: pdf_path should be {expected_pdf}, found {pdf_path}"
                )

        if relative_path:
            row_relative_paths.append(relative_path)
            target = root / relative_path
            if not target.exists():
                errors.append(f"{file_name or f'row {index}'}: missing TeX path {relative_path}")

        if pdf_path:
            target = root / pdf_path
            if not target.exists():
                errors.append(f"{file_name or f'row {index}'}: missing PDF path {pdf_path}")

    duplicate_names = sorted({name for name in row_names if row_names.count(name) > 1})
    if duplicate_names:
        errors.append("Duplicate file_name rows: " + ", ".join(duplicate_names))

    duplicate_paths = sorted(
        {path for path in row_relative_paths if row_relative_paths.count(path) > 1}
    )
    if duplicate_paths:
        errors.append("Duplicate relative_path rows: " + ", ".join(duplicate_paths))

    row_name_set = set(row_names)
    missing_rows = sorted(active_names - row_name_set)
    extra_rows = sorted(row_name_set - active_names)

    if missing_rows:
        errors.append(
            "Active TeX files missing from the file map: " + ", ".join(missing_rows)
        )

    if extra_rows:
        errors.append(
            "CSV rows that do not match an active TeX file: " + ", ".join(extra_rows)
        )

    return errors


def main() -> int:
    errors = validate()
    root = repo_root()
    tex_count = len(list((root / "manuscripts/active/tex").glob("*.tex")))

    if errors:
        print("Active manuscript file map validation failed.", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        "Active manuscript file map validation passed: "
        f"{tex_count} active manuscripts are covered and their mapped PDFs exist."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
