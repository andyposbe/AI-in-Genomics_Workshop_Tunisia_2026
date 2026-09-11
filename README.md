# AI in Genomics: Real-World Applications & Opportunities

**Tunisia, 14–18 September 2026** · A two-day hands-on workshop, run twice.

| | Dates | Host | Venue |
|---|---|---|---|
| **Workshop A** | 14–15 September 2026 | Centre of Biotechnology of Borj Cédria (CBBC) | Espace Zmorda, Soukra, Tunis |
| **Workshop B** | 17–18 September 2026 | Higher Institute of Biotechnology of Sfax (ISBS) | ISBS, Sfax |

Delivered by [GetGenome](https://getgenome.net/) and [The Sainsbury Laboratory](https://www.tsl.ac.uk/), supported through the Bifrost initiative (Kamoun Lab, TSL).

### 📖 Full materials: **https://andyposbe.github.io/AI-in-Genomics_Workshop_Tunisia_2026/**

---

## Start here

Do these three things **before you arrive**. They take about 30 minutes and some need a stable internet connection.

1. **[Set up your laptop](https://andyposbe.github.io/AI-in-Genomics_Workshop_Tunisia_2026/setup/)**: install UCSF ChimeraX, create an AlphaFold Server account, check you can open a terminal.
2. **Download this repository.** Green `Code` button → `Download ZIP`, then unzip it somewhere you can find again. Or:
   ```bash
   git clone https://github.com/andyposbe/AI-in-Genomics_Workshop_Tunisia_2026.git
   ```
3. **Run the setup check:**
   ```bash
   python3 scripts/check_setup.py
   ```
   It tells you what is missing and what to do about it.

> **Bring your own laptop.** Computers are not provided at either venue.

## What you will do

Four practical sessions that run end to end as one workflow: a sequence goes in on Day 1, a designed binder comes out on Day 2.

| | Session | You will |
|---|---|---|
| **P1** | [Predict](docs/practicals/01-predict.md) | Submit your sequence data to predict models, interpret and compare scores across complexes |
| **P2** | [Interpret](docs/practicals/02-interpret.md) | Introduction to molecular visualisation to interpret protein models and design key experiments |
| **P3** | [Compare](docs/practicals/03-compare.md) | Align structures to reveal hidden relationships beyond sequence similarity |
| **P4** | [Design](docs/practicals/04-design.md) | Design de novo structures and binders against a target to create novel solutions |

The thread running through all four: **AI tools are a means to an end, not the end in and of themselves.** A prediction is a hypothesis.

## Repository layout

```
docs/            Workshop website source (Markdown, edit these rather than HTML)
  practicals/    One page per practical session
data/            Input files and pre-computed results for each practical
worksheets/      Printable exercise sheets, one folder per practical
slides/          Slide decks (uploaded after each workshop)
scripts/         Setup checks and helper scripts
assets/          Images and site styling
```

## Programme

Two days, same programme at both venues. [Full timetable →](docs/programme.md)

**Day 1. Predict & Interpret.** Introduction to AI for Genomics, theoretical introduction to AlphaFold, Practical 1, the GOHREP it! discussions, Practical 2.

**Day 2. Compare & Design.** Practical 3, model your own proteins, Practical 4, Genomics in an AI world.

## After the workshop

This repository is kept up to date once the workshop is over.

- Slide decks go into [`slides/`](slides/) within two weeks of each workshop.
- Printable worksheets go into [`worksheets/`](worksheets/), one folder per practical.
- The practical guides in [`docs/practicals/`](docs/practicals/) are updated as the sessions run and corrected afterwards.
- Pre-computed results for every step stay in [`data/`](data/).

**Adding your own slides or worksheet?** [CONTRIBUTING.md](CONTRIBUTING.md) walks through it with no git and no terminal.

## Team

Led by a team from The Sainsbury Laboratory and GetGenome, co-delivered with the [2026 Facilitator Cohort](docs/team.md), researchers based across Tunisia.

## Questions

- **During the workshop**: ask any facilitator, or [open an issue](../../issues/new/choose).
- **Anything else**: <getgenome@tsl.ac.uk>

## Reuse

Teaching materials are [CC BY 4.0](LICENSE), so reuse them, adapt them, run your own version. Code and scripts are [MIT](LICENSE-CODE). If you adapt these materials, a link back is appreciated.

`#GetGenome` `#AIinGenomics2026`
