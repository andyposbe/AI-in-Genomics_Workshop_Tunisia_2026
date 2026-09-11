---
title: "P4: Design"
layout: default
parent: Practicals
nav_order: 4
---

# Practical 4: Design
{: .no_toc }

<dl class="session-meta" markdown="0">
  <dt>When</dt><dd>Day 2, 13:30–14:45</dd>
  <dt>You need</dt><dd>ChimeraX, a browser or terminal, <code>data/practical-04_design/</code></dd>
  <dt>You leave with</dt><dd>Designed sequences, a folded prediction of your own design, and a filtered shortlist</dd>
  <dt>Pairs</dt><dd>Yes</dd>
</dl>

1. TOC
{:toc}

---

## Why this session exists

Everything up to here has been reading. This session is writing. The conceptual jump is small and the practical consequences are large: the same models that predict structure from sequence can be run to propose sequence for a structure.

By the end you should be able to:

- Explain inverse folding in one sentence to someone who missed the session
- Generate sequences for a fixed backbone with ProteinMPNN and judge whether they are plausible
- Run a binder design against a chosen target surface
- Filter designs down to the handful you would actually order
- Say what a designed binder is and is not evidence of

## Step 1. Inverse folding with ProteinMPNN

Structure prediction asks: given this sequence, what shape? Inverse folding asks the reverse: given this shape, which sequences would fold into it?

Run it on a backbone from Practical 1 or 3, generate a handful of sequences, and compare them to the native. The positions the model refuses to change are the interesting ones, usually the core and the functionally constrained residues.

<div class="checkpoint" markdown="1">
<span class="checkpoint-label">Checkpoint 1</span>
Everyone has a set of designed sequences and has compared identity to the native backbone.
</div>

## Step 2. Does the design fold?

Take your best designed sequence back through Practical 1. Predict it, then superimpose the prediction on the backbone you designed for, using the Practical 3 method.

{: .warning }
> This is a closed loop: a model checking its own homework. A design that passes
> self-consistency has cleared the lowest bar, not the highest one.

## Step 3. Binder design

A binder is a protein designed to attach to a chosen surface of a target protein, used for example to block the activity of a toxin, or in plant immunity to recognise a pathogen effector.

We demonstrate binder design with **PXDesign**. <!-- FILL IN: the exact run: target surface from the P1/P2 complex, hotspot residue selection, number of designs, expected runtime. Other tools under consideration for the session: BoltzGen, BindCraft, Protenix. -->

{: .note }
> **Facilitators:** the toolchain has to run inside 135 minutes on participant laptops with
> conference wifi and no GPU. A hybrid works well: everyone analyses a pre-computed design
> set, and anyone whose connection holds also launches their own run.

<div class="checkpoint" markdown="1">
<span class="checkpoint-label">Checkpoint 2</span>
Everyone has a set of candidate binders, whether their own or the pre-computed set.
</div>

## Step 4. Filtering

Generating designs is cheap. Deciding which twelve to order is the job.

<!-- FILL IN: the filter cascade you want them to apply, with thresholds and the reasoning
     behind each. Interface confidence, self-consistency, buried surface area,
     aggregation and expression liabilities. Make them discard designs and defend the cuts. -->

## Step 5. What happens at the bench

<!-- FILL IN: honest numbers on experimental success rates for binder design, with
     citations, and the workflow that follows: expression, purification, binding assay,
     and what a negative result actually tells you. -->

## Step 6. Take it back to your own system

Bring one question to the closing discussion:

- What would you design, if you could design anything, for your own system?
- What is the step in that plan you have no idea how to do?

## Troubleshooting

| Problem | Fix |
|---|---|
| Runtime disconnected | Reconnect and restart the cell. Designs are not saved automatically, so download as you go. |
| Out of memory | Reduce batch size or design length. |
| Designs look like poly-alanine | Check you passed the right chain and that the backbone is not mostly low-confidence. |
| No time left | Switch to the pre-computed set in `data/practical-04_design/` and go straight to filtering. |

## Going further

<!-- FILL IN: where to read next, which methods are moving fastest, and what a realistic
     first project looks like for someone returning to their own lab with no GPU. -->
