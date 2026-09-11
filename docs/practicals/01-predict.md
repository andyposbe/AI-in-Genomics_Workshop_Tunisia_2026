---
title: "P1: Predict"
layout: default
parent: Practicals
nav_order: 1
---

# Practical 1: Predict
{: .no_toc }

<dl class="session-meta" markdown="0">
  <dt>When</dt><dd>Day 1, 11:20–12:30</dd>
  <dt>You need</dt><dd>A browser, an AlphaFold Server account, <code>data/practical-01_predict/</code></dd>
  <dt>You leave with</dt><dd>Predicted structures for a monomer and for complexes, plus their confidence metrics</dd>
  <dt>Pairs</dt><dd>Yes, one screen submitting, one reading</dd>
</dl>

1. TOC
{:toc}

---

## Why this session exists

Pressing submit is easy. The reason we spend the session here is not the button. It is so that by the end you can say which parts of your model you would stake an experiment on.

By the end you should be able to:

- Submit monomer, homomer and heteromer jobs to the AlphaFold 3 server and explain how the inputs differ
- Set the modelling parameters, seed number and templates, and say what they change
- Read pLDDT, pTM and ipTM well enough to rank two models against each other
- Say what the model does **not** know

## The example system

We work with the rice immune receptor **Pikp-1**, which confers resistance to *Pyricularia oryzae*, the fungus causing rice blast disease. The practicals use residues 186–486, which span the integrated HMA domain and the NB-ARC domain, and three effector proteins secreted by the same fungus: **AVR-PikD**, **AVR-Pib** and **AVR-Pii** (given to you as Pathogen_protein_1, 2 and 3).

All sequences are in [`data/practical-01_predict/`](https://github.com/andyposbe/AI-in-Genomics_Workshop_Tunisia_2026/tree/main/data/practical-01_predict).

## Exercise 1. Model a single chain

Go to <https://alphafoldserver.com/>, create an account, and submit `Pikp-1_186-486`.

While it runs, read the next section. Do not sit and watch the queue.

Then discuss:

- What does pTM stand for, and what is the pTM score for this prediction?
- Is pLDDT high all over the model, or are some residues predicted more confidently than others?
- Are there regions of the PAE plot where the relative positions are unreliable?

### Reading the colours

The default colouring is per-residue confidence:

<div class="plddt-scale" markdown="0">
  <span class="vh">Very high · pLDDT &gt; 90<br>Backbone and side chains reliable</span>
  <span class="cf">Confident · 70–90<br>Backbone reliable</span>
  <span class="lo">Low · 50–70<br>Treat with caution</span>
  <span class="vl">Very low · &lt; 50<br>Often disordered, not wrong, but undefined</span>
</div>

A very low score is information, not failure. Regions scoring below 50 are frequently genuinely disordered in solution.

<div class="checkpoint" markdown="1">
<span class="checkpoint-label">Checkpoint 1</span>
Everyone has a completed monomer job and has downloaded the result bundle.
</div>

## Exercise 2. Oligomeric states

Model the **HMA domain** of Pikp-1 on its own as a dimer (n = 2), trimer (n = 3) and tetramer (n = 4), and record pTM and ipTM for each.

- What does ipTM stand for?
- What does the PAE look like across the different oligomeric states? Is there high confidence in the relative positioning of the protomers in every case?

The crystal structure of Pikp-HMA was solved as a homodimer (PDB [5A6P](https://www.rcsb.org/structure/5A6P), Maqbool *et al.* 2015). Compare that with what the modelling suggests.

## Exercise 3. Protein–protein interaction prediction

Model three heteromeric complexes between Pikp-1_186–486 and each of the three pathogen proteins. Using the confidence metrics alone:

- Which effector is most likely to interact with Pikp-1, and which metrics tell you that?
- Which Pikp-1 domain contributes to binding?
- What experiments would you do to test the hypothesis?

<div class="checkpoint" markdown="1">
<span class="checkpoint-label">Checkpoint 2</span>
Everyone has the three complex predictions and has found the interface confidence score for each.
</div>

{: .warning }
> A high interface score is not evidence that two proteins interact in a cell. It is evidence
> that the model can place them together confidently. All models need to be tested with
> functional assays afterwards.

## Your own protein

Bring a sequence from your own work and submit it. Write down your prediction before the job finishes: which regions do you expect to score well, and why? Then check.

## Troubleshooting

| Problem | Fix |
|---|---|
| Job stuck in queue | Expected at peak times. Carry on; use `data/practical-01_predict/precomputed/`. |
| Hit the daily job limit | Pair up and share a submission. Limits are per account. |
| Sequence rejected | Check for stop codons, gaps, or non-standard characters. |
| Download will not open | It is a zip. Unzip before opening the CIF. |

## Going further

<!-- FILL IN: pointers to local/ColabFold alternatives, batch submission, and what changes
     when you need thousands of predictions rather than three. Link the Bifrost work here. -->
