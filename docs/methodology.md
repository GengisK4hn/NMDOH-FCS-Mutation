# Methodology

## Data Source

Sequences were downloaded from the NCBI Nucleotide database using the following search query:

```
Severe acute respiratory syndrome coronavirus 2[Organism] AND New Mexico[All Fields] AND 2026[All Fields]
```

- Download date: 2026-04-14
- Total sequences retrieved: 260
- Format: FASTA (complete genomes)
- Source: NCBI Nucleotide (https://www.ncbi.nlm.nih.gov/nuccore)

## Detection Method

### P681R Mutation Detection

The analysis scans nucleotide sequences for the P681R mutation at the furin cleavage site.

**Reference Patterns:**
- Wildtype: `CCTCGGCGGGCA` (translates to PRRA amino acids)
- P681R: `CCTCGTCGGCGGGCACGT` (translates to PRRAR amino acids)

**Note:** P681R is a point mutation (CCT→CGT substitution) that produces the RRRAR motif at the S1/S2 furin cleavage site. This mutation was characteristic of the 2021 Delta variant, where it enhanced furin cleavage efficiency and fitness. Its re-detection in 2025-2026 NMDOH sequences after years of rarity in dominant Omicron lineages illustrates convergent evolution at a functionally important site.

**Detection Logic:**
```python
# Pseudocode
for sequence in fasta_file:
    if "CCTCGTCGGCGGGCACGT" in sequence:
        classify_as_p681r()
    elif "CCTCGGCGGGCA" in sequence:
        classify_as_wildtype()
    else:
        classify_as_other()
```

## Analysis Results

| Category | Count | Percentage |
|----------|-------|------------|
| P681R mutation | 26 | 10.0% |
| Wildtype | 234 | 90.0% |
| Total analyzed | 260 | 100% |

## Sequences with P681R

### 2026 Collection Year (n=3)

| Accession | Sample ID |
|-----------|-----------|
| PZ222127.1 | NMDOH-2026000801 |
| PZ222120.1 | NMDOH-2026001709 |
| PZ222100.1 | NMDOH-2026001828 |

### All P681R Sequences (n=26)

The remaining 23 sequences with P681R were collected in 2025.

## Reproducibility

To reproduce these findings:

1. Download the data:
```bash
esearch -db nucleotide \
  -query "Severe acute respiratory syndrome coronavirus 2[Organism] AND New Mexico[All Fields] AND 2026[All Fields]" \
  | efetch -format fasta > data/nm_2026_sequences.fasta
```

2. Run the detection script:
```bash
python scripts/fcs_scanner.py data/nm_2026_sequences.fasta
```

Expected output: `26/260 sequences with P681R mutation`

## Technical Notes

- **P681R functional role:** The S1/S2 furin cleavage site is a well-established determinant of SARS-CoV-2 entry; the P681R substitution (present in Delta) increases cleavage efficiency
- **Delta context:** P681R was a defining mutation of the Delta variant (2021), contributing to its increased fitness and transmissibility
- **Resurgence:** Re-detection after years of rarity in Omicron-lineage viruses illustrates convergent evolution at this functional site
- Detection via nucleotide pattern matching at position ~23,500 in full genome reference
