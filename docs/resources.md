---
title: Resources
layout: default
nav_order: 7
permalink: /resources/
---

# Resources

Everything you need during the workshop, and the things worth reading afterwards.
{: .fs-5 .fw-300 }

## Tools we use

| Tool | What for | Link |
|---|---|---|
| AlphaFold Server | Structure prediction (P1) | <https://alphafoldserver.com/> |
| UCSF ChimeraX | Visualisation and superposition (P2–P4) | <https://www.cgl.ucsf.edu/chimerax/> |
| AlphaFold DB | Pre-computed predictions for most known proteins | <https://alphafold.ebi.ac.uk/> |
| PDB | Experimental structures | <https://www.rcsb.org/> |
| UniProt | Sequences and annotation | <https://www.uniprot.org/> |
| TM-align | Pairwise structure alignment (P3) | <https://zhanggroup.org/TM-align/> |
| Foldseek | Structure search (P3) | <https://search.foldseek.com/> |
| FoldMason | Multiple structure alignment (P3) | <https://foldmason.foldseek.com/> |
| ProteinMPNN | Inverse folding (P4) | <https://github.com/dauparas/ProteinMPNN> |
| PXDesign | Binder design (P4) | <https://pxdesign.bio/> |

<!-- FILL IN: pin version numbers for each tool once the session runs are finalised. -->

## ChimeraX command cheatsheet

The commands used across Practicals 2–4. Specifiers: `#` model, `/` chain, `:` residue.

```
open 7B1I                                    open a structure from the PDB
open model_0.cif                             open a local model
color #1 bychain                             colour by chain
sel #1/c                                     select chain C
color sel gray                               colour the current selection
color #1/c #2B89AD                           select and colour in one line, hex code
sel #1/b:1-10                                a residue range
sel #1/b:1,5,20                              a list of residues
surface #1/c                                 show a molecular surface
alphafold contacts #1/a to #1/b distance 3.5              contacts across an interface
alphafold contacts #1/a to #1/b distance 3.5 outputFile AF3-contacts.txt   export them
matchmaker #2 to #1                          superimpose two structures
pwd                                          where files are being saved
save ChimeraX_Exercise1.cxs                  save the session
```

PAE data is loaded from the menu: **Tools → Structure Prediction → AlphaFold Error Plot**.

## Slides and written guides

Slide decks from the talks and session introductions are uploaded to [`slides/`](https://github.com/andyposbe/AI-in-Genomics_Workshop_Tunisia_2026/tree/main/slides) within two weeks of each workshop.

Printable worksheets are in [`worksheets/`](https://github.com/andyposbe/AI-in-Genomics_Workshop_Tunisia_2026/tree/main/worksheets). The written guide for each practical lives on its own page under [Practicals](practicals/index.md), updated during and after the workshop, so it stays the current version of the material. [Slides & worksheets](materials.md) lists everything in one place.

## Reading

**Start here**

<!-- FILL IN: three papers maximum for people who will read three papers. -->

**If you want the methods**

<!-- FILL IN: AlphaFold 2 and 3 papers, the inverse-folding and binder-design methods
     used in P4, and one good critical review of what these models get wrong. -->

**On reproducibility**

<!-- FILL IN: the GoRHEP material referenced in the workshop description, plus practical
     guidance on recording model versions, seeds and databases alongside results. -->

## Compute after the workshop

The hardest part of taking this home is access to a GPU.

<!-- FILL IN: free and low-cost options relevant to researchers in Tunisia: Colab tiers,
     national and regional HPC access, EMBL-EBI services, and which parts of the workflow
     genuinely need a GPU versus which run fine on a laptop. Be concrete; this is the
     section people will come back to. -->

## Stay in touch

- GetGenome: <https://getgenome.net/>
- Email: <getgenome@tsl.ac.uk>
- `#GetGenome` `#AIinGenomics2026`
