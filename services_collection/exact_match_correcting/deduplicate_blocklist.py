#!/usr/bin/env python3
"""
Blocklist Deduplication and Analysis Script

This script reads the exact_match_blocklist.txt file, removes duplicate entries,
and provides detailed analysis of the blocklist contents.

Usage:
    python deduplicate_blocklist.py
    
    Or pipe the file content:
    cat exact_match_blocklist.txt | python deduplicate_blocklist.py --stdin
"""

import os
import sys
from collections import Counter


def analyze_and_deduplicate_blocklist(lines=None, input_file=None, output_file=None):
    """
    Analyze and deduplicate blocklist entries.
    
    Args:
        lines: Optional list of lines (if reading from stdin or passed directly)
        input_file: Path to input file (if lines not provided)
        output_file: Path to save deduplicated output
    """
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    if input_file is None:
        input_file = os.path.join(script_dir, "exact_match_blocklist.txt")
    if output_file is None:
        output_file = os.path.join(script_dir, "exact_match_blocklist_deduplicated.txt")

    # Read all entries from the blocklist if not provided
    if lines is None:
        try:
            with open(input_file, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except PermissionError:
            print("❌ Permission denied. Try running with:")
            print(f"   cat '{input_file}' | python deduplicate_blocklist.py --stdin")
            sys.exit(1)

    # Strip whitespace and filter empty lines
    original_entries = [line.strip() for line in lines]
    non_empty_entries = [entry for entry in original_entries if entry]

    # Count occurrences of each entry
    entry_counts = Counter(non_empty_entries)
    
    # Find duplicates (entries that appear more than once)
    duplicates = {entry: count for entry, count in entry_counts.items() if count > 1}
    
    # Get unique entries (preserving original order)
    seen = set()
    unique_entries = []
    for entry in non_empty_entries:
        if entry not in seen:
            seen.add(entry)
            unique_entries.append(entry)

    # Write deduplicated entries to new file (if possible)
    file_saved = False
    if output_file:
        try:
            with open(output_file, "w", encoding="utf-8") as f:
                for entry in unique_entries:
                    f.write(entry + "\n")
            file_saved = True
        except PermissionError:
            print("⚠️  Cannot write to output file (permission denied)")
            print("   Deduplicated content will be printed to stdout instead if --print-output is used")
            print()

    # Print analysis
    print("=" * 60)
    print("BLOCKLIST ANALYSIS REPORT")
    print("=" * 60)
    print()
    
    print("📊 SUMMARY STATISTICS")
    print("-" * 40)
    print(f"  Total lines in original file:     {len(lines):,}")
    print(f"  Non-empty entries:                {len(non_empty_entries):,}")
    print(f"  Empty lines:                      {len(lines) - len(non_empty_entries):,}")
    print(f"  Unique entries:                   {len(unique_entries):,}")
    print(f"  Duplicate entries removed:        {len(non_empty_entries) - len(unique_entries):,}")
    print()
    
    if duplicates:
        print("🔄 DUPLICATE ENTRIES FOUND")
        print("-" * 40)
        # Sort duplicates by count (descending)
        sorted_duplicates = sorted(duplicates.items(), key=lambda x: x[1], reverse=True)
        for entry, count in sorted_duplicates:
            print(f"  [{count}x] {entry}")
        print()
    else:
        print("✅ No duplicate entries found!")
        print()
    
    # Domain analysis (extract top-level domains)
    tld_counter = Counter()
    for entry in unique_entries:
        # Extract the main domain part
        parts = entry.replace("http://", "").replace("https://", "").split("/")[0]
        domain_parts = parts.split(".")
        if len(domain_parts) >= 2:
            # Get TLD or common second-level domains
            tld = domain_parts[-1]
            tld_counter[tld] += 1
    
    print("🌐 TOP DOMAIN EXTENSIONS (TLDs)")
    print("-" * 40)
    for tld, count in tld_counter.most_common(15):
        print(f"  .{tld}: {count:,} entries")
    print()
    
    # Common domains
    domain_counter = Counter()
    for entry in unique_entries:
        clean_entry = entry.replace("http://", "").replace("https://", "").split("/")[0]
        parts = clean_entry.split(".")
        if len(parts) >= 2:
            # Get the main domain (e.g., "google.com" from "*.google.com")
            main_domain = ".".join(parts[-2:])
            domain_counter[main_domain] += 1
    
    print("🏢 TOP BLOCKED DOMAINS")
    print("-" * 40)
    for domain, count in domain_counter.most_common(15):
        print(f"  {domain}: {count:,} entries")
    print()
    
    print("=" * 60)
    if file_saved:
        print(f"✅ Deduplicated file saved to:")
        print(f"   {output_file}")
    else:
        print("ℹ️  Analysis complete (file not saved due to permissions)")
    print("=" * 60)
    
    return {
        "total_lines": len(lines),
        "non_empty_entries": len(non_empty_entries),
        "empty_lines": len(lines) - len(non_empty_entries),
        "unique_entries": len(unique_entries),
        "duplicates_removed": len(non_empty_entries) - len(unique_entries),
        "duplicate_details": duplicates
    }


if __name__ == "__main__":
    if "--stdin" in sys.argv:
        # Read from stdin
        lines = sys.stdin.readlines()
        results = analyze_and_deduplicate_blocklist(lines=lines)
    else:
        results = analyze_and_deduplicate_blocklist()
