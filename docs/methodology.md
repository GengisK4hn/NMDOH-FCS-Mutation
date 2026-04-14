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

**Note:** P681R is a point mutation (CCT→CGT substitution) that produces the RRRAR motif in translation. This mutation was characteristic of the Delta variant (dominant mid-2021 to late 2021) but has been absent from all circulating lineages since Omicron replaced Delta. The NMDOH sequences represent the first documented resurgence of P681R.

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

- **P681R history:** Characteristic mutation of Delta variant (dominant mid-2021 to late 2021)
- **Absence:** No circulating lineages carried P681R from late 2021 through 2024 (Omicron era)
- **Resurgence:** NMDOH sequences (2025-2026) represent first re-emergence of P681R via convergent evolution
- Detection via nucleotide pattern matching
- This is not a novel mutation, but its resurgence after 3+ years is notable
- FCS position approximately 23,500 in full genome reference
