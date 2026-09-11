# Adding your slides and worksheets

For trainers and facilitators. No git, no terminal, no coding. You need a free
GitHub account and about five minutes.

Repository: <https://github.com/andyposbe/AI-in-Genomics_Workshop_Tunisia_2026>
Website: <https://andyposbe.github.io/AI-in-Genomics_Workshop_Tunisia_2026/>

---

## Where does my file go?

| What you have | Folder | Example file name |
|---|---|---|
| A talk or session introduction from **Day 1** | `slides/day1/` | `AF-theory_Posbeyikian.pdf` |
| A talk or session introduction from **Day 2** | `slides/day2/` | `Design-intro_Sugihara.pdf` |
| A **flash talk** by a local researcher | `slides/flash/` | `Flash_Ben-Alaya.pdf` |
| A **worksheet or handout** for Practical 1 | `worksheets/practical-01_predict/` | `P1-exercises.pdf` |
| Practical 2 worksheet | `worksheets/practical-02_interpret/` | `P2-ChimeraX-exercises.pdf` |
| Practical 3 worksheet | `worksheets/practical-03_compare/` | `P3-exercises.pdf` |
| Practical 4 worksheet | `worksheets/practical-04_design/` | `P4-exercises.pdf` |
| Example files people need to run a session | `data/practical-0X_.../` | `my-sequences.fasta` |

If your file does not fit any of these, put it in the closest folder and say so
in the commit message. Someone will move it.

## Naming

`Topic_Surname.pdf` for slides, `P1-exercises.pdf` for worksheets. No spaces
in file names, use hyphens. Keep the name stable if you upload a new version,
so links to it do not break.

## How to upload, step by step

1. Sign in to GitHub and open the repository link above.
2. Click into the folder your file belongs in, from the table above.
3. Click **Add file**, then **Upload files**.
4. Drag your file onto the dashed area.
5. In the box at the bottom, write what you added, for example
   `Add Practical 2 worksheet`.
6. Click **Commit changes**.

That is it. Your file is online straight away, at a link anyone can open.

If you do not have write access to the repository, GitHub shows you a
**Propose changes** button instead. Click it and Andy gets a notification to
approve. Nothing is lost.

## Formats

- **PDF, please.** It opens on any computer, and it is the format participants
  can read on a phone during the session. Export from PowerPoint or Keynote:
  File, Export, PDF.
- If the deck has to stay editable for the next workshop, upload the `.pptx`
  **as well as** the PDF, side by side.
- Keep each file under 25 MB, which is the limit the GitHub web uploader
  accepts. If a deck is bigger, export it again at a lower image quality.
- Videos do not belong here. Put them on a TSL or GetGenome drive and add the
  link to the folder's `README.md`.

## Flash talks and permission

Do not upload someone else's talk without asking them first. Flash talks are
only added to `slides/flash/` when the speaker has said yes. If in doubt, ask
the speaker, not the repository.

Also check that what you upload contains no unpublished data belonging to
someone else, and no personal information about participants.

## Fixing a mistake in a practical page

The written guides for the four practicals are the pages on the website, not
files you upload. To correct one:

1. Open the page on the website.
2. Click **Suggest a change to this page** at the bottom.
3. Edit the text and commit, or click **Propose changes** if you do not have
   write access.

The site rebuilds itself in two or three minutes.

Markdown, in full: `**bold**`, `*italic*`, `## ` starts a heading, `- ` starts
a bullet, `[text](https://link)` makes a link, and a blank line starts a new
paragraph.

## Questions

Ask Andy, or email <getgenome@tsl.ac.uk>.
