---
title: "P3: Compare"
layout: default
parent: Practicals
nav_order: 3
---

# Practical 3: Compare
{: .no_toc }

<dl class="session-meta" markdown="0">
  <dt>When</dt><dd>Day 2, 09:30–11:15</dd>
  <dt>You need</dt><dd>ChimeraX, a terminal, <code>data/practical-03_compare/</code></dd>
  <dt>You leave with</dt><dd>A pairwise superposition, a set of structural neighbours, and a multiple structure alignment</dd>
  <dt>Pairs</dt><dd>Yes</dd>
</dl>

1. TOC
{:toc}

---

## Why this session exists

One structure is an anecdote. Once you have thirty, you can ask questions sequence alone cannot answer: which of these share a fold despite sharing no identity, and which look similar for trivial reasons? This is structure-based annotation.

By the end you should be able to:

- Align two structures with TM-align and interpret the TM-score
- Search a structure against a database with Foldseek and interpret the hits
- Align multiple structures with FoldMason and read the result
- Explain when structural similarity implies shared function and when it does not

## Step 1. Pairwise alignment with TM-align

Start inside ChimeraX for the visual version:

```
open <model-A>.cif
open <model-B>.cif
matchmaker #2 to #1
```

Then run the same pair through TM-align and compare what the two tell you.

<!-- FILL IN: how to read the TM-align output: aligned length, RMSD, TM-score, and which
     of the two TM-scores (normalised by which chain) you should quote. The key point:
     RMSD over few residues is meaningless, and a global RMSD hides local agreement. -->

<div class="checkpoint" markdown="1">
<span class="checkpoint-label">Checkpoint 1</span>
Everyone has two structures superimposed and can state the TM-score and how many residues it covers.
</div>

## Step 2. Structure search with Foldseek

Query the example structure against a structure database and look at the top hits.

<!-- FILL IN: the exact Foldseek route used on the day (web server vs local install),
     the database to search, and the columns to read. Find at least one hit with
     negligible sequence identity but a clear structural match. That case is the
     argument for the whole session. -->

## Step 3. Multiple structure alignment with FoldMason

Align the provided set of structures and inspect the alignment and the tree that comes with it.

<!-- FILL IN: the FoldMason command, the input set, and what to look at in the output.
     Where do the structural clusters agree with the sequence tree, and where do they
     disagree? Disagreement is the interesting case: convergent folds, domain shuffling,
     or a low-confidence model contaminating the set. -->

<div class="checkpoint" markdown="1">
<span class="checkpoint-label">Checkpoint 2</span>
Everyone has an alignment for the provided set and has identified the outlier.
</div>

## Your own set

Bring a family you work on. Ten to thirty members is a good size for the time available.

## Troubleshooting

| Problem | Fix |
|---|---|
| Superposition is nonsense | You may be aligning different domains. Restrict to a residue range. |
| Search returns nothing | Check the input format and that the query is a single chain. |
| Out of time | Use the pre-computed results in `data/practical-03_compare/` and carry on. |

## Going further

<!-- FILL IN: scaling to thousands of structures, structure-aware phylogenetics and its
     current limitations, and where this feeds into Practical 4. -->
