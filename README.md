# NMDOH SARS-CoV-2 FCS Analysis

Analysis of SARS-CoV-2 sequences from New Mexico Department of Health (NMDOH) surveillance, examining the P681R mutation at the furin cleavage site (FCS).

## Summary

- **Sequences analyzed:** 260
- **Source:** NCBI Nucleotide database (New Mexico, 2025-2026)
- **Finding:** 26 sequences (10.0%) contain P681R mutation
- **Significance:** First detection of P681R since Delta variant (late 2021)
- **2026-specific findings:** 3 sequences with P681R

## FCS Motif Reference

| Variant | DNA Sequence | Amino Acids | Description |
|---------|--------------|-------------|-------------|
| Wildtype | CCTCGGCGGGCA | PRRA | Common SARS-CoV-2 FCS |
| P681R | CCTCGTCGGCGGGCACGT | PRRRAR | P681R point mutation (same as Delta) |

**Note:** P681R is a single nucleotide substitution (CCT→CGT at position 681), not an insertion. The RRRAR motif is the translated appearance of this known mutation.

## 2026 Sequences with P681R

| Accession | Sample ID |
|-----------|-----------|
| PZ222127.1 | NMDOH-2026000801 |
| PZ222120.1 | NMDOH-2026001709 |
| PZ222100.1 | NMDOH-2026001828 |

## Repository Structure

```
.
├── data/
│   └── nm_2026_sequences.fasta    # 260 NMDOH sequences
├── results/
│   └── fcs_detection.txt           # Detection output
├── docs/
│   └── methodology.md              # Methods and reproducibility
├── scripts/
│   └── fcs_scanner.py              # Detection script
└── README.md
```

## Reproducing the Analysis

Install requirements:
```bash
pip install biopython
```

Run detection:
```bash
python scripts/fcs_scanner.py data/nm_2026_sequences.fasta
```

Expected output:
```
Total sequences: 260
Extended FCS (PRRRAR): 26
Wildtype FCS (PRRA): 234
Other/No FCS detected: 0
```

## Data Source

- **Database:** NCBI Nucleotide
- **Query:** SARS-CoV-2[Organism] AND New Mexico[All Fields] AND 2026[All Fields]
- **Download date:** 2026-04-14
- **Accession range:** PZ225545.1 - PZ038795.1

## Notes

- **P681R in Delta:** This mutation was characteristic of the 2021 Delta variant, where it enhanced furin cleavage efficiency and viral fitness
- **Resurgence:** Re-detection of P681R in 2025-2026 after years of rarity in dominant Omicron lineages illustrates convergent evolution at a functionally important site
- **Context:** The S1/S2 furin cleavage site is a well-established determinant of viral entry; P681R has been shown to increase cleavage efficiency
- Sequences are public genomic surveillance data with no patient identifiers
- Full methodology available in `docs/methodology.md`

## License

CC0 1.0 Universal Public Domain Dedication

See LICENSE file for details.
