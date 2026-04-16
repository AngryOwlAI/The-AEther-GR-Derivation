#!/usr/bin/env python3

from __future__ import annotations

import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent

PUBLIC_STEMS = [
    "aether_flow_exact_closure_sequence_overview",
    "aether_flow_exact_closure_note",
    "aether_flow_foundations",
    "aether_flow_dynamics",
    "aether_flow_consistency",
    "aether_flow_relativistic_recovery",
    "aether_flow_geometry",
    "aether_flow_exact_closure_flagship_article",
]

LINK_AUDIT_FILES = [
    REPO_ROOT / "README.md",
    REPO_ROOT / "docs" / "index.md",
    REPO_ROOT / "docs" / "start-here.md",
    REPO_ROOT / "docs" / "theory-package.md",
    REPO_ROOT / "docs" / "research-archive.md",
    REPO_ROOT / "docs" / "how-to-review.md",
    REPO_ROOT / "docs" / "ai-collaboration-and-method.md",
    REPO_ROOT / "docs" / "front-facing-article.md",
    REPO_ROOT / "docs" / "AETHER_FLOW_CLAIM_BOUNDARY.md",
    REPO_ROOT / "docs" / "AETHER_FLOW_NAMING_AND_VOCABULARY.md",
    REPO_ROOT / "RESEARCH_PLAN.md",
    REPO_ROOT / "EXECUTION_CHECKLIST.md",
]

FORBIDDEN_PHRASES = {
    REPO_ROOT / "docs" / "index.md": [
        "observer-relevant zepto-section minimizer-image-core collapse to observer-relevant zepto-section minimizer-section core theorem",
        "immediate next primary manuscript target is one layer below that theorem",
    ],
    REPO_ROOT / "docs" / "research-archive.md": [
        "The current live frontier:",
        "proto-section-generating substrate pre-proto-section dynamics",
        "The next primary manuscript should now act one level below the current pre-proto-section frontier.",
    ],
}

LINK_PATTERN = re.compile(r"!?\[(?P<label>[^\]]+)\]\((?P<target>[^)]+)\)")


def check_public_bundle(errors: list[str]) -> None:
    for stem in PUBLIC_STEMS:
        active_tex = REPO_ROOT / "manuscripts" / "active" / "tex" / f"{stem}.tex"
        public_tex = REPO_ROOT / "docs" / "assets" / "tex" / f"{stem}.tex"
        public_pdf = REPO_ROOT / "docs" / "assets" / "pdfs" / f"{stem}.pdf"

        if not active_tex.exists():
            errors.append(f"Missing active TeX source: {active_tex}")
            continue
        if not public_tex.exists():
            errors.append(f"Missing public TeX copy: {public_tex}")
            continue
        if active_tex.read_bytes() != public_tex.read_bytes():
            errors.append(
                f"Public TeX drift: docs/assets/tex/{stem}.tex does not match manuscripts/active/tex/{stem}.tex"
            )
        if not public_pdf.exists():
            errors.append(f"Missing public PDF: {public_pdf}")
            continue
        if public_pdf.stat().st_mtime < public_tex.stat().st_mtime:
            errors.append(
                f"Stale public PDF: docs/assets/pdfs/{stem}.pdf is older than docs/assets/tex/{stem}.tex"
            )


def check_links(errors: list[str]) -> None:
    for file_path in LINK_AUDIT_FILES:
        text = file_path.read_text(encoding="utf-8")
        for match in LINK_PATTERN.finditer(text):
            target = match.group("target").strip()
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = target.split("#", 1)[0].strip()
            if not target:
                continue
            resolved = (file_path.parent / target).resolve()
            if not resolved.exists():
                line_no = text.count("\n", 0, match.start()) + 1
                errors.append(f"Broken local link: {file_path.relative_to(REPO_ROOT)}:{line_no} -> {target}")


def check_forbidden_phrases(errors: list[str]) -> None:
    for file_path, phrases in FORBIDDEN_PHRASES.items():
        text = file_path.read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase in text:
                errors.append(
                    f"Stale phrase still present in {file_path.relative_to(REPO_ROOT)}: {phrase}"
                )


def main() -> int:
    errors: list[str] = []

    check_public_bundle(errors)
    check_links(errors)
    check_forbidden_phrases(errors)

    if errors:
        print("PUBLIC DOC SYNC CHECK FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PUBLIC DOC SYNC CHECK PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
