#!/usr/bin/env python3
"""Normalize YAML frontmatter in test case markdown files.

This rewrites the top frontmatter block in each Test Suites/*.md file so the
values are valid YAML scalars and the Postconditions field uses a block scalar.
"""

from __future__ import annotations

import os
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
TEST_SUITES = ROOT / "Test Suites"


def yaml_quote(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def extract_frontmatter_and_body(text: str) -> tuple[str, str]:
    match = re.match(r"^---\r?\n(?P<frontmatter>.*?)\r?\n---\r?\n(?P<body>.*)$", text, re.DOTALL)
    if not match:
        return "", text
    return match.group("frontmatter"), match.group("body")


def header_title(body: str, fallback: str) -> str:
    for line in body.splitlines():
        if line.startswith("#"):
            return line.lstrip("#").strip()
    return fallback


def extract_postconditions(body: str) -> list[str]:
    lines = body.splitlines()
    capture = False
    result: list[str] = []
    for line in lines:
        if re.match(r"^##\s*Postconditions\s*$", line, re.IGNORECASE):
            capture = True
            continue
        if capture and re.match(r"^##\s+", line):
            break
        if capture:
            if line.strip().startswith("-"):
                result.append(line.strip().lstrip("-").strip())
    return result


def parse_key(frontmatter: str, key: str, default: str = "") -> str:
    pattern = rf"^{re.escape(key)}:\s*(.*)$"
    for line in frontmatter.splitlines():
        match = re.match(pattern, line.strip(), re.IGNORECASE)
        if match:
            raw = match.group(1).strip()
            if raw.startswith('"') and raw.endswith('"') and len(raw) >= 2:
                raw = raw[1:-1]
            return raw
    return default


def build_frontmatter(file_id: str, title: str, priority: str, status: str, automated: str, owner: str, requirements: str, postconditions: list[str]) -> str:
    lines = ["---"]
    lines.append(f"ID: {yaml_quote(file_id)}")
    lines.append(f"Title: {yaml_quote(title)}")
    lines.append(f"Priority: {yaml_quote(priority)}")
    lines.append(f"Status: {yaml_quote(status)}")
    lines.append(f"Automated: {yaml_quote(automated)}")
    lines.append(f"Owner: {yaml_quote(owner)}")
    lines.append(f"Requirements: {yaml_quote(requirements)}")
    if postconditions:
        lines.append("Postconditions: |")
        for item in postconditions:
            lines.append(f"  - {item}")
    else:
        lines.append('Postconditions: ""')
    lines.append("---")
    return "\n".join(lines)


def normalize_file(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    frontmatter, body = extract_frontmatter_and_body(original)
    if not frontmatter:
        return False

    file_id = path.stem.upper()
    title = header_title(body, path.stem)
    priority = "Medium"
    status = "draft"
    automated = "no"
    owner = ""
    requirements = ""
    postconditions = extract_postconditions(body)

    rebuilt = build_frontmatter(file_id, title, priority, status, automated, owner, requirements, postconditions)
    new_text = rebuilt + "\n\n" + body.lstrip("\n")
    if new_text != original:
        path.write_text(new_text, encoding="utf-8")
        return True
    return False


def main() -> int:
    changed = 0
    for path in sorted(TEST_SUITES.rglob("*.md")):
        if normalize_file(path):
            changed += 1
    print(f"Normalized {changed} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
