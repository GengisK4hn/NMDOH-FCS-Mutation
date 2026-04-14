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

### FCS Motif Detection

The analysis scans nucleotide sequences for specific patterns at the furin cleavage site region.

**Reference Patterns:**
- Wildtype FCS: `CCTCGGCGGGCA` (translates to PRRA amino acids)
- Extended FCS: `CCTCGTCGGCGGGCACGT` (translates to PRRRAR amino acids)

**Detection Logic:**
```python
# Pseudocode
for sequence in fasta_file:
    if "CCTCGTCGGCGGGCACGT" in sequence:
        classify_as_extended_fcs()
    elif "CCTCGGCGGGCA" in sequence:
        classify_as_wildtype_fcs()
    else:
        classify_as_other()
```

## Analysis Results

| Category | Count | Percentage |
|----------|-------|------------|
| Extended FCS (PRRRAR) | 26 | 10.0% |
| Wildtype FCS (PRRA) | 234 | 90.0% |
| Total analyzed | 260 | 100% |

## Sequences with Extended FCS

### 2026 Collection Year (n=3)

| Accession | Sample ID |
|-----------|-----------|
| PZ222127.1 | NMDOH-2026000801 |
| PZ222120.1 | NMDOH-2026001709 |
| PZ222100.1 | NMDOH-2026001828 |

### All Extended FCS Sequences (n=26)

The remaining 23 sequences with extended FCS were collected in 2025.

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

Expected output: `26/260 sequences with extended FCS`

## Technical Notes

- Pattern matching performed on nucleotide sequences
- No alignment or phylogenetic analysis conducted
- FCS position approximately 23,500 in full genome reference
- Results represent presence/absence of specific nucleotide patterns
