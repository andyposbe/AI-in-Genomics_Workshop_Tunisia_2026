---
title: "P2: Interpret"
layout: default
parent: Practicals
nav_order: 2
---

# Practical 2: Interpret
{: .no_toc }

<dl class="session-meta" markdown="0">
  <dt>When</dt><dd>Day 1, 15:15–17:00</dd>
  <dt>You need</dt><dd>ChimeraX, your Practical 1 outputs, <code>data/practical-02_interpret/</code></dd>
  <dt>You leave with</dt><dd>An annotated model, an exported contact list, and a set of candidate interface mutations</dd>
  <dt>Pairs</dt><dd>Yes</dd>
</dl>

1. TOC
{:toc}

---

## Why this session exists

Prediction is a service; interpretation is the skill. This session is about turning a coloured cartoon into a statement you would defend in a lab meeting.

By the end you should be able to:

- Explain what pLDDT and PAE measure, and why they answer different questions
- Load, colour and select structures in ChimeraX from the command line
- Colour an AlphaFold model by pLDDT and read its PAE plot inside ChimeraX
- Export the predicted contacts at an interface and filter them by confidence
- Propose interface mutations, and say what testing them would actually require

## Exercise 2.1. ChimeraX basics

We use the command line inside ChimeraX rather than the menus, because commands are reproducible and menus are not. Open an experimental structure from the PDB:

```
open 7B1I
```

Click `[more info…]` in the log to see the metadata: what is the title of the associated paper, and which experimental method was used?

Then work through chains, sequences and secondary structure. The hierarchy is `#` model, `/` chain, `:` residue:

```
sel #1/c              select chain C
color sel gray        colour the selection
color #1/c #2B89AD    same thing, one line, with a hex code
sel #1/b:1-10         a residue range
sel #1/b:1,5,20       a list of residues
surface #1/c          show a molecular surface
```

Save your session before moving on, as ChimeraX does not save progress automatically:

```
save ChimeraX_Exercise1.cxs
```

<div class="checkpoint" markdown="1">
<span class="checkpoint-label">Checkpoint 1</span>
Everyone has 7B1I open, coloured by secondary structure, and a saved session file.
</div>

## Exercise 2.2. Visualising AF3 models with their confidence metrics

Use the Pikp-1_186–486 + Pathogen_protein_1 prediction from Practical 1. Download the result bundle from the AlphaFold Server and unzip it. You get around 17 files, including the top-ranked model (`..._model_0.cif`), the other ranked models, and the JSON files holding the PAE data.

Drag `model_0.cif` into ChimeraX and colour by chain:

```
color #1 bychain
```

Load the confidence data: **Tools → Structure Prediction → AlphaFold Error Plot**, then pick the matching `..._full_data_0.json` if ChimeraX does not find it automatically. From here you can colour by pLDDT or by PAE domains.

### pLDDT: confidence in a position

Per-residue. Answers: *is this residue placed correctly relative to its neighbours?*

Colour the prediction by pLDDT. What can you say about the residues at the interface between the two proteins?

### PAE: confidence in a relationship

Pairwise. Answers: *if I trust where residue i is, how well do I know where residue j is?* This is the metric that tells you about domain arrangement, and the one people skip.

The PAE plot is interactive: a selection in the plot is reflected in the 3D model, which is the quickest way to find out which parts of the structure the confident blocks correspond to.

{: .note }
> Two rigid domains joined by a flexible linker can produce a model that looks completely
> wrong as a single object and is completely right as two objects. Read PAE before you
> conclude a prediction failed.

### Contacts as pseudobonds

With the PAE data loaded, draw the predicted contacts across the interface, coloured by PAE:

```
alphafold contacts #1/a to #1/b distance 3.5
```

Which β-sheet on the effector side has more high-confidence (low PAE) contacts with Pikp-1? The same command takes residue ranges and lists, so you can narrow it down:

```
alphafold contacts #1/b:20 to #1/a distance 4.5
```

<div class="checkpoint" markdown="1">
<span class="checkpoint-label">Checkpoint 2</span>
Everyone can point at a region of their model and say which metric made them distrust it.
</div>

## Exercise 2.3. Exporting the interface and designing mutations

Add `outputFile` to export the contact list for downstream analysis:

```
alphafold contacts #1/a to #1/b distance 3.5 outputFile AF3-contacts.txt
```

Each row is a residue pair below the distance cutoff with its PAE score. Open it in a spreadsheet and sort by PAE to drop the low-confidence contacts.

**PAE confidence** · 0–10 confident · 10–15 grey zone · >15 poor confidence

Then, from the interface you have just described:

- Which residues, in either protein, would you mutate to abolish the interaction?
- What experiments would test those mutants in the lab, and what controls would you include?

{: .warning }
> A drop in interface score after mutation does not predict a loss of binding. It generates
> a hypothesis for the bench.

## Troubleshooting

| Problem | Fix |
|---|---|
| ChimeraX will not open the CIF | Unzip the bundle first; open the model file, not the folder. |
| No PAE plot | PAE lives in the JSON, not the CIF. Download the full bundle. |
| `alphafold contacts` does nothing | The PAE data must be loaded first via the AlphaFold Error Plot tool. |

## Going further

<!-- FILL IN: links to the metric definitions, the AlphaFold papers, and the ChimeraX
     AlphaFold tutorials. -->
