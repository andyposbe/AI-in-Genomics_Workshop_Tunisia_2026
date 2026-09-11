---
title: Before you arrive
layout: default
nav_order: 2
permalink: /setup/
---

# Before you arrive
{: .no_toc }

Please come to the workshop with the software already installed.
{: .fs-5 .fw-300 }

1. TOC
{:toc}

---

## 1. Bring a laptop

Computers are not provided at either venue. Any laptop running Windows 10+, macOS 12+, or Linux is fine. You need:

- Administrator rights to install software
- About 5 GB free disk space
- A power adapter, and a plug adapter if you are travelling internationally (Tunisia uses Type C/E, 230 V)

{: .warning }
> If your institute's laptop blocks software installation, sort this out **now** with your IT team. It is the single most common reason people lose a morning.

## 2. Install UCSF ChimeraX

ChimeraX is the structure viewer used in Practicals 2, 3 and 4.

- Download: <https://www.cgl.ucsf.edu/chimerax/download.html>
- Make sure to select the correct version for your computer's operating system (see the list under *Other releases*).
- Free for academic use; you will be asked to register.
- **Install it, then open it once** to confirm that it launches. Installing without opening it hides most of the problems people hit.

If you run into any issues installing or opening ChimeraX, email <andres.posbeyikian@tsl.ac.uk> before the workshop. Do not worry if it is still not working on the day, as we can troubleshoot together during the session.

<!-- FILL IN: pin the exact ChimeraX version the facilitators will demo, so
     screenshots in the practicals match what participants see. -->

## 3. Create an AlphaFold Server account

Practical 1 uses the AlphaFold Server at <https://alphafoldserver.com/>.

- Sign in with a Google account. If you do not have one, make one now.
- Note the daily job limit per account. Check the current figure on the site before the workshop and plan your submissions around it.
- Read the terms of use. They restrict commercial use, and we will discuss what that means for your own work.

{: .note }
> There is a queue. Submit your first job as soon as Practical 1 opens, then carry on with the reading while it runs.

## 4. Check you can open a terminal

You need a command line for Practicals 3 and 4.

| System | How |
|---|---|
| macOS | Applications → Utilities → Terminal |
| Linux | Ctrl + Alt + T |
| Windows | Install [Windows Terminal](https://aka.ms/terminal), or use WSL, or Git Bash |

Open it once to check that it starts. You do not need to install anything else in advance.

<!-- FILL IN: if Practicals 3/4 need a conda environment rather than a browser,
     add the environment.yml install steps here. -->

## 5. Optional but useful

- A [Google account with Colab access](https://colab.research.google.com/) if any session runs in a notebook.
- Your own protein of interest, a sequence you actually care about. The practicals use a shared example, but every session has an open slot where you can run your own. This is where most people get their best result of the two days.

---

## Still stuck?

Email <andres.posbeyikian@tsl.ac.uk> with your operating system and the error you are seeing, and someone will get back to you before the workshop. For anything that is not about software, email <getgenome@tsl.ac.uk>.
