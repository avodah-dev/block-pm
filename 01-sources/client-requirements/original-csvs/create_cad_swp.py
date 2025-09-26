#!/usr/bin/env python3
"""
Create CAD-001 from SWP-cleaned.csv
"""

import csv
import json
from pathlib import Path
from datetime import datetime

def parse_csv_to_requirements(csv_file, doc_title, doc_id):
    """Parse cleaned CSV file and extract requirements."""
    requirements = []

    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for row in reader:
            # Get the requirement ID from first column (REQ-ID)
            req_id = row.get('REQ-ID', '').strip()
            if not req_id or not req_id.startswith('SWP-'):
                continue

            # Extract fields from the CSV columns (note: REQUIREMENT has trailing space in header)
            requirement = {
                "id": req_id,
                "phase": row.get('PHASE ESTIMATE', '').strip(),
                "process": row.get('PROCESS', '').strip(),
                "requirement": row.get('REQUIREMENT ', '').strip(),  # Note the trailing space
                "details": row.get('DETAILS/CONTEXT', '').strip(),
                "new_functionality": row.get('NEW FUNCTIONALITY?', '').strip(),
                "notes": row.get('Jake Notes', '').strip() if 'Jake Notes' in row else '',
                "phase_1_notes": row.get('Phase 1', '').strip() if 'Phase 1' in row else '',
                "future_notes": row.get('Future', '').strip() if 'Future' in row else ''
            }

            # Determine category from requirement ID
            if '-M-' in req_id:
                requirement['category'] = 'MUST HAVE'
            elif '-S-' in req_id:
                requirement['category'] = 'SHOULD HAVE'
            elif '-C-' in req_id:
                requirement['category'] = 'COULD HAVE'
            elif '-N-' in req_id:
                requirement['category'] = 'NOT DOING'
            else:
                requirement['category'] = 'UNKNOWN'

            requirements.append(requirement)

    return requirements

def create_json_cad(requirements, doc_title, doc_id, source_file):
    """Create JSON format CAD document."""
    json_doc = {
        "document_id": doc_id,
        "title": doc_title,
        "source": source_file,
        "extracted_date": datetime.now().isoformat(),
        "total_requirements": len(requirements),
        "requirements_by_category": {},
        "requirements": requirements
    }

    # Count requirements by category
    categories = {}
    for req in requirements:
        cat = req['category']
        if cat not in categories:
            categories[cat] = 0
        categories[cat] += 1

    json_doc['requirements_by_category'] = categories

    return json_doc

def create_markdown_cad(requirements, doc_title, doc_id, json_doc):
    """Create Markdown format CAD document."""
    md_lines = []

    # Header
    md_lines.append(f"# {doc_id}: {doc_title}")
    md_lines.append("")
    md_lines.append("## Document Information")
    md_lines.append(f"- **Document ID**: {doc_id}")
    md_lines.append(f"- **Title**: {doc_title}")
    md_lines.append(f"- **Source**: {json_doc['source']}")
    md_lines.append(f"- **Extracted Date**: {json_doc['extracted_date']}")
    md_lines.append(f"- **Total Requirements**: {json_doc['total_requirements']}")
    md_lines.append("")

    # Summary by category
    md_lines.append("## Requirements Summary by Category")
    for cat, count in json_doc['requirements_by_category'].items():
        md_lines.append(f"- **{cat}**: {count} requirements")
    md_lines.append("")

    # Requirements by category
    categories_found = set(req['category'] for req in requirements)

    for category in ['MUST HAVE', 'SHOULD HAVE', 'COULD HAVE', 'NOT DOING']:
        if category not in categories_found:
            continue

        md_lines.append(f"## {category} Requirements")
        md_lines.append("")

        cat_reqs = [r for r in requirements if r['category'] == category]

        for req in cat_reqs:
            md_lines.append(f"### {req['id']}")
            md_lines.append(f"**Requirement**: {req['requirement']}")
            md_lines.append("")

            if req['details']:
                md_lines.append(f"**Details**: {req['details']}")
                md_lines.append("")

            if req['phase']:
                md_lines.append(f"**Phase**: {req['phase']}")
                md_lines.append("")

            if req['process']:
                md_lines.append(f"**Process**: {req['process']}")
                md_lines.append("")

            if req['new_functionality']:
                md_lines.append(f"**New Functionality**: {req['new_functionality']}")
                md_lines.append("")

            if req['notes']:
                md_lines.append(f"**Notes**: {req['notes']}")
                md_lines.append("")

            if req.get('phase_1_notes'):
                md_lines.append(f"**Phase 1 Notes**: {req['phase_1_notes']}")
                md_lines.append("")

            if req.get('future_notes'):
                md_lines.append(f"**Future Notes**: {req['future_notes']}")
                md_lines.append("")

            md_lines.append("---")
            md_lines.append("")

    return '\n'.join(md_lines)

def main():
    """Create CAD-001 from SWP-cleaned.csv"""

    # Paths
    base_path = Path("/Users/andrewbailey/dev/block-sw-discovery/client-anchor-docs")
    csv_file = base_path / "original-csvs" / "SWP-cleaned.csv"
    json_output = base_path / "CAD-001-swp-buyer-requirements.json"
    md_output = base_path / "CAD-001-swp-buyer-requirements.md"

    # Document metadata
    doc_id = "CAD-001"
    doc_title = "Sourcing Window Pro (Buyer) Requirements"
    source_file = "SWP-cleaned.csv (from original Excel export)"

    print(f"Creating {doc_id} from {csv_file.name}...")

    # Parse CSV
    requirements = parse_csv_to_requirements(csv_file, doc_title, doc_id)
    print(f"  ✓ Parsed {len(requirements)} requirements")

    # Create JSON document
    json_doc = create_json_cad(requirements, doc_title, doc_id, source_file)

    # Write JSON file
    with open(json_output, 'w', encoding='utf-8') as f:
        json.dump(json_doc, f, indent=2, ensure_ascii=False)
    print(f"  ✓ Created {json_output.name}")

    # Create and write Markdown file
    md_content = create_markdown_cad(requirements, doc_title, doc_id, json_doc)
    with open(md_output, 'w', encoding='utf-8') as f:
        f.write(md_content)
    print(f"  ✓ Created {md_output.name}")

    # Print summary
    print(f"\n{doc_id} Summary:")
    for cat, count in json_doc['requirements_by_category'].items():
        print(f"  - {cat}: {count}")
    print(f"  Total: {json_doc['total_requirements']} requirements")

if __name__ == "__main__":
    main()