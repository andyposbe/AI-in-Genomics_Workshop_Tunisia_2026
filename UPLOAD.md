# Resources and Slides & worksheets

Four files, about 52 KB. Nothing to delete.

## Upload

Drag all four into the repo root in one go:

- `resources.html`
- `materials.html`
- `styles.css`
- `lessons.js` (new file)

Commit message: `Expand Resources, add the Fold on Tight thread`

Upload them together. The Resources page needs the new rules in `styles.css`
and the new `lessons.js`, so a partial upload will look broken until the rest
arrives.

`styles.css` already contains everything currently live, including the hashtag
rules from the last round, plus the new thread styles. Replacing it is safe.

## What changed

**Slides & worksheets** now has only the "Available now" table. "Where
everything lives" and "For trainers and facilitators" are gone. Both worksheet
rows link straight to the PDF rather than to GitHub.

**Resources** has:

- A full Tools table: AlphaFold Server, ChimeraX, Protenix, NCBI blastp,
  InterProScan, TM-align, Foldseek, FoldMason, ProteinMPNN. The last six match
  the links at the end of the Day 2 worksheet.
- The AlphaFold talk linked to its PDF.
- Further reading, in this order: the Fold on Tight thread, GOHREP and PLESI,
  binder design links, then the papers behind the data.

## The Fold on Tight thread

The ten lessons are listed on a rail, as plain text, and nothing loads from X
until somebody presses "Show the posts". The posts then render one at a time as
they scroll into view. If X is blocked or slow, each post falls back to a link
and the lesson headings are unaffected.

The headings are taken word for word from the Zenodo PDF. The mapping of tweet
to lesson assumes the thread runs: opening post, lessons 1 to 10 in order, then
the two closing posts.

## Papers cited

| Where | Paper |
|---|---|
| Practicals 1 and 2 | Maqbool et al. 2015, eLife 4:e08709 |
| Practical 2, PDB 7B1I | Maidment et al. 2021, JBC 296:100371 |
| Practical 3 | Lahfa et al. 2024, PLOS Pathogens 20(5):e1012176 |
| Practical 4 | de Guillen et al. 2015, PLOS Pathogens 11(10):e1005228 |

7B1I and Lahfa are certain: the first is the structure file itself, the second
is named in Yu's worksheet. Maqbool is my reading of what the Day 1 sequences
are, so worth a glance.
