#!/usr/bin/env python3
"""
Script to clean SW and SWP CSV files by:
1. Preserving the header row
2. Keeping only rows that start with SW- or SWP-
3. Removing empty rows
4. Preserving all data columns
"""

import csv
import sys
from pathlib import Path

def clean_csv(input_file, output_file, prefix):
    """
    Clean a CSV file by keeping header and valid requirement rows only.

    Args:
        input_file: Path to input CSV
        output_file: Path to output cleaned CSV
        prefix: Required prefix for requirement IDs (e.g., 'SW-' or 'SWP-')
    """
    cleaned_rows = []
    header_row = None
    requirement_count = 0

    with open(input_file, 'r', encoding='utf-8') as infile:
        reader = csv.reader(infile)

        for row_num, row in enumerate(reader, 1):
            # Skip completely empty rows
            if not any(row):
                continue

            # Look for header row (contains "REQUIREMENT" in uppercase)
            if header_row is None and any('REQUIREMENT' in str(cell).upper() for cell in row):
                header_row = row
                cleaned_rows.append(row)
                print(f"Found header at row {row_num}: {row[:5]}...")
                continue

            # Keep rows that start with the required prefix
            if row and row[0] and row[0].strip().startswith(prefix):
                cleaned_rows.append(row)
                requirement_count += 1

    # Write cleaned data
    with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(cleaned_rows)

    print(f"✓ Cleaned {input_file}")
    print(f"  - Found {requirement_count} {prefix} requirements")
    print(f"  - Output has {len(cleaned_rows)} total rows (including header)")
    print(f"  - Saved to {output_file}")

    return requirement_count

def main():
    """Main function to clean CSV files."""
    base_path = Path("/Users/andrewbailey/dev/block-sw-discovery/client-anchor-docs/original-csvs")

    # Clean SW.csv
    sw_input = base_path / "SW.csv"
    sw_output = base_path / "SW-cleaned.csv"

    if sw_input.exists():
        print("Processing SW.csv...")
        sw_count = clean_csv(sw_input, sw_output, "SW-")
    else:
        print(f"❌ File not found: {sw_input}")

    print("\n" + "="*60 + "\n")

    # Clean SWP.csv
    swp_input = base_path / "SWP.csv"
    swp_output = base_path / "SWP-cleaned.csv"

    if swp_input.exists():
        print("Processing SWP.csv...")
        swp_count = clean_csv(swp_input, swp_output, "SWP-")
    else:
        print(f"❌ File not found: {swp_input}")

    print("\n" + "="*60)
    print("✅ All CSV files cleaned successfully!")

if __name__ == "__main__":
    main()