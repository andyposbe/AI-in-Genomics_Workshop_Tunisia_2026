# practical-01_predict

Input sequences and AlphaFold Server output for the Predict session, one folder
per exercise. The worksheet for this session is
[`worksheets/Day1_Practicals-1-2_Worksheet.pdf`](../../worksheets/Day1_Practicals-1-2_Worksheet.pdf).

## exercise-1.1

| File | What it is |
|---|---|
| `Pikp-1_186-486.fasta` | Pikp-1, residues 186 to 486 |
| `fold_pikp_1_186_486_seed_1.zip` | AlphaFold Server output for that sequence, one job |

## exercise-1.2

| File | What it is |
|---|---|
| `Pikp-HMA.fasta` | The Pikp HMA domain |
| `folds_2026_09_12_10_26.zip` | AlphaFold Server output for four jobs: HMA monomer, dimer, trimer and tetramer |

## exercise-1.3

| File | What it is |
|---|---|
| `Pikp-1_186-486.fasta` | Pikp-1, residues 186 to 486 |
| `Pathogen_protein_1_AVR-PikD.fasta` | Pathogen protein 1, AVR-PikD |
| `Pathogen_protein_2_AVR-Pib.fasta` | Pathogen protein 2, AVR-Pib |
| `Pathogen_protein_3_AVR-Pii.fasta` | Pathogen protein 3, AVR-Pii |
| `folds_2026_09_12_15_36.zip` | AlphaFold Server output for three jobs: Pikp-1 186-486 with each of the three pathogen proteins |

## What is inside an AlphaFold Server zip

For each job: five predicted models as `.cif`, a `summary_confidences` JSON and
a `full_data` JSON per model, the job request, the MSAs, and the template hits.
