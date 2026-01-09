#!/usr/bin/env python3
"""Decompose ptx_full.md into individual section files.

Usage:
    python decompose.py [ptx_full.md] [output_dir]

Defaults:
    input:  ptx_full.md (same directory as script)
    output: sections/
"""
from __future__ import annotations

import re
import sys
from pathlib import Path


def slugify(text: str) -> str:
    """Convert header text to filename-safe slug."""
    # Remove markdown formatting
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)  # [text](link) -> text
    text = re.sub(r'`([^`]+)`', r'\1', text)  # `code` -> code
    # Convert to lowercase, replace spaces/special chars with hyphens
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    text = re.sub(r'-+', '-', text)  # collapse multiple hyphens
    text = text.strip('-')
    return text[:80]  # limit length


def parse_section_number(header: str) -> tuple[str, str] | None:
    """Extract section number and title from header line.

    Returns (section_num, title) or None if not a numbered section.
    """
    # Match patterns like "## 1.2. Goals of PTX" or "###### 9.7.16.10.9.1. TensorCore..."
    # Skip headers with markdown links (duplicates)
    if '[' in header and '](' in header:
        return None

    match = re.match(r'^#{1,6}\s+(\d+(?:\.\d+)*\.?)\s+(.+?)\s*$', header)
    if match:
        section_num = match.group(1).rstrip('.')
        title = match.group(2).strip()
        return section_num, title
    return None


def get_header_level(line: str) -> int:
    """Get markdown header level (1-6) or 0 if not a header."""
    match = re.match(r'^(#{1,6})\s', line)
    return len(match.group(1)) if match else 0


def decompose(input_path: Path, output_dir: Path) -> dict[str, Path]:
    """Decompose markdown into sections.

    Returns mapping of section_number -> output_path
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    content = input_path.read_text(encoding='utf-8')
    lines = content.split('\n')

    # Find all section headers with their line numbers
    sections: list[tuple[int, str, str, int]] = []  # (line_idx, section_num, title, level)

    for i, line in enumerate(lines):
        level = get_header_level(line)
        if level == 0:
            continue
        parsed = parse_section_number(line)
        if parsed:
            section_num, title = parsed
            sections.append((i, section_num, title, level))

    # Deduplicate - keep last occurrence of each section number (cleanest)
    seen: dict[str, int] = {}
    for idx, (line_idx, section_num, title, level) in enumerate(sections):
        seen[section_num] = idx

    unique_sections = [sections[i] for i in sorted(seen.values())]

    # Write each section
    index: dict[str, Path] = {}

    for i, (start_idx, section_num, title, level) in enumerate(unique_sections):
        # Find end (next section at same or higher level, or EOF)
        if i + 1 < len(unique_sections):
            end_idx = unique_sections[i + 1][0]
        else:
            end_idx = len(lines)

        # Extract content
        section_lines = lines[start_idx:end_idx]
        section_content = '\n'.join(section_lines).strip()

        # Skip empty or very short sections
        if len(section_content) < 50:
            continue

        # Generate filename
        num_slug = section_num.replace('.', '-')
        title_slug = slugify(title)
        filename = f"{num_slug}-{title_slug}.md"

        # Write file
        out_path = output_dir / filename
        out_path.write_text(section_content + '\n', encoding='utf-8')
        index[section_num] = out_path

    return index


def build_index(sections: dict[str, Path], output_dir: Path) -> None:
    """Write an index file mapping section numbers to files."""
    index_path = output_dir / '_index.txt'
    with open(index_path, 'w', encoding='utf-8') as f:
        for section_num in sorted(sections.keys(), key=lambda x: [int(n) for n in x.split('.')]):
            f.write(f"{section_num}\t{sections[section_num].name}\n")


def main():
    script_dir = Path(__file__).parent

    input_path = Path(sys.argv[1]) if len(sys.argv) > 1 else script_dir / 'ptx_full.md'
    output_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else script_dir / 'sections'

    if not input_path.exists():
        print(f"Error: {input_path} not found")
        sys.exit(1)

    print(f"Decomposing {input_path} -> {output_dir}/")
    sections = decompose(input_path, output_dir)
    build_index(sections, output_dir)
    print(f"Created {len(sections)} section files")
    print(f"Index written to {output_dir}/_index.txt")


if __name__ == '__main__':
    main()
