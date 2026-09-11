# Getting this repository online

For Andy. Everything here is done in a web browser, no git and no terminal.
Allow about 20 minutes the first time.

The result: the files live at
`https://github.com/andyposbe/AI-in-Genomics_Workshop_Tunisia_2026`
and the website is served at
`https://andyposbe.github.io/AI-in-Genomics_Workshop_Tunisia_2026/`

All the links in these files already point at those two addresses. If you
change the account name or the repository name, run
`python3 scripts/set_owner.py <account> <repo-name>` first, or the links break.

---

## 1. Create the repository

1. Sign in at <https://github.com> as **andyposbe**.
2. Top right, click **+** then **New repository**.
3. Fill it in exactly:
   - **Repository name:** `AI-in-Genomics_Workshop_Tunisia_2026`
   - **Description:** AI in Genomics: Real-World Applications & Opportunities. Tunisia, 14 to 18 September 2026.
   - **Public** (the website only works on a free account if the repository is public)
   - Leave *Add a README file*, *.gitignore* and *license* **unticked**. This
     folder already has all three, and ticking them creates a conflict.
4. Click **Create repository**.

You land on an empty repository page with setup instructions. Ignore the
command line instructions and continue below.

## 2. Upload the files

GitHub's uploader takes whole folders by drag and drop, but it will not take
an empty folder, and it will not take a `.zip` and unpack it.

1. On the empty repository page, click the link **uploading an existing file**.
   (If you have already uploaded once: **Add file** then **Upload files**.)
2. Open the unzipped `AI-in-Genomics_Workshop_Tunisia_2026` folder on your
   computer in a Finder window next to the browser.
3. Select everything **inside** that folder, not the folder itself:
   press <kbd>Cmd</kbd>+<kbd>A</kbd> in the Finder window.
4. Drag the selection onto the dashed upload area in the browser.
5. Wait for every file to finish listing. The count should be around 50 files.
   Check that `index.md`, `_config.yml`, `docs`, `data`, `assets` and `scripts`
   all appear.
6. In **Commit changes**, write `Add workshop site and materials`.
7. Leave **Commit directly to the main branch** selected and click
   **Commit changes**.

> **The hidden files.** macOS hides files starting with a dot, so the Finder
> selection above misses `.github/`, `.gitignore` and the `.gitkeep` files that
> hold the empty folders open. Press
> <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>.</kbd> in Finder to show them, then
> select all again and drag. The site works without them, but the issue
> templates and the empty `slides/` and `worksheets/` folders will be missing.

## 3. Turn the website on

1. In the repository, click **Settings** (top right of the repository bar).
2. In the left sidebar, click **Pages**.
3. Under **Build and deployment**, set **Source** to **GitHub Actions**.
   The repository already contains the workflow that builds the site, so
   nothing else is needed here.
4. Click **Actions** in the top repository bar and watch the run named
   *Build and deploy site*. It takes two to three minutes. A green tick means done.
5. Open <https://andyposbe.github.io/AI-in-Genomics_Workshop_Tunisia_2026/>

If the run fails, open it and read the red step. The usual cause is a typo in
`_config.yml`. Undo your last edit and the run repeats automatically.

## 4. Check it before sharing

Click through the site once:

- The four practical pages open from the **Practicals** menu.
- **Before you arrive** shows the ChimeraX download link.
- **Team** shows all the trainers and the nine facilitators.
- The GetGenome, TSL and Bifrost logos appear at the foot of the home page.

Then share the address with participants and facilitators.

## 5. Editing a page later

You never need to re-upload everything.

1. Open the page on the website and click **Suggest a change to this page**
   at the bottom. That opens the exact file on GitHub, ready to edit.
2. Edit the text, scroll down, write a short note in **Commit changes**, and
   commit to the main branch.
3. The site rebuilds itself. Give it two or three minutes, then refresh.

Everything on the site is written in Markdown: `**bold**`, `*italic*`,
`- ` for a bullet, `## ` for a heading, `[text](https://link)` for a link.

## 6. Add your collaborators

Anyone with a GitHub account can be given upload rights. They then drag their
slides straight into the right folder, with no approval step from you.

1. In the repository, click **Settings**.
2. In the left sidebar, click **Collaborators** (under *Access*).
3. Click **Add people**.
4. Type their GitHub username, or the email address on their GitHub account.
   The name has to match an existing account, so ask each person for their
   username rather than guessing.
5. Choose the role **Write** and click **Add to this repository**.
6. They get an email invitation. Nothing happens until they accept it, so ask
   them to check their inbox, including spam.

Repeat for each person. Roles, in plain terms:

| Role | Can do |
|---|---|
| **Write** | Upload files, edit pages, commit to main. The right choice for trainers and facilitators. |
| **Maintain** | The same, plus settings and Pages. Give this to one other person as a backup for you. |
| **Admin** | Everything, including deleting the repository. Keep this to yourself. |

**Someone without a GitHub account, or someone you would rather review first.**
They do not need to be a collaborator at all. On a public repository anyone
signed in can click **Add file**, upload, and click **Propose changes**, which
creates a pull request. You get an email, open the **Pull requests** tab, and
click **Merge pull request** to accept it. Nothing reaches the site until you
merge.

**What to send them.** One message with the repository link and
**[CONTRIBUTING.md](CONTRIBUTING.md)**, which tells them which folder each kind
of file goes in and walks through the upload in six clicks. Nothing else is
needed, and no git or terminal is involved.

**Removing someone later.** Settings, Collaborators, then the remove button
next to their name. Files they already uploaded stay where they are.

## 7. Adding files after the workshop

Slides go in `slides/day1/`, `slides/day2/` and `slides/flash/`, worksheets in
the four folders under `worksheets/`. The full convention, including file
naming and the PDF rule, is in **[CONTRIBUTING.md](CONTRIBUTING.md)**. You
upload your own the same way your collaborators do.

## If something goes wrong

| Problem | What to do |
|---|---|
| 404 at the site address | Pages is not on yet, or the first build has not finished. Settings, Pages, check Source is GitHub Actions, then look at Actions. |
| Site is live but the styling is missing | `url` or `baseurl` in `_config.yml` does not match the real address. Fix those two lines and commit. |
| Images do not show | The `assets/img/` folder did not upload. Add file, Upload files, drag `assets` in again. |
| Uploaded the folder instead of its contents | Everything sits one level too deep. Delete the repository (Settings, bottom of the page) and start at step 1, selecting the files inside the folder. |
| A file is too big to upload | GitHub refuses files over 25 MB in the web uploader. Put large data on Zenodo and link to it from the relevant README. |
| A collaborator says they cannot upload | They have not accepted the email invitation yet, or they are signed in to a different GitHub account. Settings, Collaborators shows who is still pending. |
