#!/usr/bin/env python3
"""Generate CSV inventory for Test Suites and optionally add metadata frontmatter to test files.

Usage:
  python scripts/generate_inventory.py [--apply]

If --apply is provided the script will insert a YAML-like frontmatter block into any
test markdown file that is missing it, and will ensure a '## Postconditions' section exists.
The script writes 'OnTrack TCM - Test Suites.csv' at the repository root.
"""
import os
import csv
import re
import sys


BASE = 'Test Suites'
CSV_NAME = 'OnTrack TCM - Test Suites.csv'


def find_md_files(base=BASE):
    for root, dirs, files in os.walk(base):
        for f in files:
            if f.lower().endswith('.md'):
                yield os.path.join(root, f)


def read_file(path):
    with open(path, 'r', encoding='utf-8') as fh:
        return fh.read()


def write_file(path, text):
    with open(path, 'w', encoding='utf-8') as fh:
        fh.write(text)


def extract_title_and_id(text, filename):
    # Title: first header
    title = ''
    for line in text.splitlines():
        if line.strip().startswith('#'):
            title = line.lstrip('#').strip()
            break
        if line.strip():
            # fallback: first non-empty line
            title = title or line.strip()
            break

    # ID: prefer filename token
    base = os.path.basename(filename)
    m = re.match(r'(RP-[A-Z0-9-]+)\.md', base, re.IGNORECASE)
    if m:
        id_ = m.group(1).upper()
    else:
        # try to find in content
        mm = re.search(r'\b(RP-[A-Z0-9-]+)\b', text)
        id_ = mm.group(1).upper() if mm else ''

    return title, id_


def has_frontmatter(text):
    return text.lstrip().startswith('---') or re.match(r'^ID:\s', text)


def make_frontmatter(meta):
    lines = ['---']
    for k in ['ID','Title','Priority','Status','Automated','Owner','Requirements','Postconditions']:
        v = meta.get(k,'')
        # ensure lists are comma-separated strings
        if isinstance(v, list):
            v = ', '.join(v)
        lines.append(f"{k}: {v}")
    lines.append('---\n')
    return '\n'.join(lines)


def ensure_postconditions(text):
    if re.search(r'^##\s*Postconditions', text, re.IGNORECASE | re.MULTILINE):
        return text
    if not text.endswith('\n'):
        text += '\n'
    text += '\n## Postconditions\n\n- None\n'
    return text


def process(apply_changes=False):
    rows = []
    for path in sorted(find_md_files()):
        rel = path.replace('\\','/')
        text = read_file(path)
        title, id_ = extract_title_and_id(text, path)
        fm_present = has_frontmatter(text)

        meta = {'ID': id_, 'Title': title, 'Priority': 'Medium', 'Status': 'draft', 'Automated': 'no', 'Owner': '', 'Requirements': '', 'Postconditions': ''}

        if not fm_present and apply_changes:
            # backup
            bak = path + '.bak'
            if not os.path.exists(bak):
                write_file(bak, text)
            fm = make_frontmatter(meta)
            new_text = fm + text
            new_text = ensure_postconditions(new_text)
            write_file(path, new_text)
            text = new_text

        # attempt to extract fields from frontmatter-ish or top lines
        # simple parse: look for lines like 'Key: value' before first blank line
        header = ''
        for i, line in enumerate(text.splitlines()[:30]):
            header += line + '\n'
            if line.strip() == '':
                break

        def kv(key):
            m = re.search(rf'^{key}:\s*(.*)$', header, re.IGNORECASE | re.MULTILINE)
            return m.group(1).strip() if m else ''

        priority = kv('Priority') or meta['Priority']
        status = kv('Status') or meta['Status']
        automated = kv('Automated') or meta['Automated']
        owner = kv('Owner') or ''
        requirements = kv('Requirements') or ''
        postconds = kv('Postconditions') or ''

        rows.append({'ID': id_, 'Title': title, 'Module': os.path.dirname(rel), 'Priority': priority, 'Status': status, 'Owner': owner, 'ReqIDs': requirements, 'Automated': automated, 'File': rel, 'Postconditions': postconds})

    # write CSV
    csv_path = CSV_NAME
    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['ID','Title','Module','Priority','Status','Owner','ReqIDs','Automated','Postconditions','File']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for r in rows:
            writer.writerow(r)

    print(f'Wrote {csv_path} with {len(rows)} entries')


if __name__ == '__main__':
    apply_changes = '--apply' in sys.argv
    process(apply_changes=apply_changes)
