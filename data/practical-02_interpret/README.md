# practical-02_interpret

Files for the Interpret session, one folder per exercise. The worksheet for this
session is
[`worksheets/Day1_Practicals-1-2_Worksheet.pdf`](../../worksheets/Day1_Practicals-1-2_Worksheet.pdf).

## exercise-2.1

| File | What it is |
|---|---|
| `7B1I.cif` | Experimental structure, PDB entry 7B1I, in mmCIF format |

## exercise-2.2

| File | What it is |
|---|---|
| `fold_pikp_1_186_486_with_pathogen_protein_1.zip` | AlphaFold Server output for Pikp-1 186-486 with pathogen protein 1 |

## exercise-2.3

| File | What it is |
|---|---|
| `AF3-contacts.txt` | One residue pair per line: a chain A residue, a chain B residue, and the PAE for that pair |

## What is inside an AlphaFold Server zip

For each job: five predicted models as `.cif`, a `summary_confidences` JSON and
a `full_data` JSON per model, the job request, the MSAs, and the template hits.
