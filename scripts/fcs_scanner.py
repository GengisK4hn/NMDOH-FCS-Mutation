#!/usr/bin/env python3
"""
FCS Scanner - Detect furin cleavage site motifs in SARS-CoV-2 sequences.

This script scans FASTA files for the FCS motif and reports findings.
Detection is based on nucleotide pattern matching.

Reference:
- Wildtype FCS: PRRA (CCTCGGCGGGCA)
- Extended FCS: PRRRAR (CCTCGTCGGCGGGCACGT)
"""

import sys
from pathlib import Path

try:
    from Bio import SeqIO
except ImportError:
    print("Error: Biopython required. Install with: pip install biopython")
    sys.exit(1)


def scan_fasta(fasta_path):
    """
    Scan a FASTA file for FCS motifs.

    Args:
        fasta_path: Path to FASTA file

    Returns:
        dict: Detection results
    """
    sequences = list(SeqIO.parse(fasta_path, "fasta"))

    # Detection patterns (nucleotide level)
    PATTERN_WILDTYPE = "CCTCGGCGGGCA"  # PRRA
    PATTERN_EXTENDED = "CCTCGTCGGCGGGCACGT"  # PRRRAR

    results = {
        "total": len(sequences),
        "wildtype": 0,
        "extended": 0,
        "other": 0,
        "extended_list": []
    }

    for record in sequences:
        seq = str(record.seq).upper()
        has_extended = PATTERN_EXTENDED in seq
        has_wildtype = PATTERN_WILDTYPE in seq

        if has_extended:
            results["extended"] += 1
            results["extended_list"].append({
                "accession": record.id,
                "description": record.description
            })
        elif has_wildtype:
            results["wildtype"] += 1
        else:
            results["other"] += 1

    return results


def main():
    if len(sys.argv) < 2:
        print("Usage: python fcs_scanner.py <fasta_file>")
        sys.exit(1)

    fasta_path = Path(sys.argv[1])

    if not fasta_path.exists():
        print(f"Error: File not found: {fasta_path}")
        sys.exit(1)

    print(f"Scanning: {fasta_path}")
    print("=" * 60)

    results = scan_fasta(fasta_path)

    print(f"\nTotal sequences: {results['total']}")
    print(f"Extended FCS (PRRRAR): {results['extended']}")
    print(f"Wildtype FCS (PRRA): {results['wildtype']}")
    print(f"Other/No FCS detected: {results['other']}")

    if results['extended_list']:
        print(f"\nSequences with extended FCS:")
        for i, seq_info in enumerate(results['extended_list'], 1):
            print(f"  {i}. {seq_info['accession']}")

    print("\n" + "=" * 60)
    print(f"Result: {results['extended']}/{results['total']} sequences with extended FCS")


if __name__ == "__main__":
    main()
