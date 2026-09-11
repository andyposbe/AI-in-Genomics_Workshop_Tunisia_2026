#!/usr/bin/env python3
"""Regenerate site-preview.html from the repository Markdown.

Keeps the existing <head>/CSS, the embedded image dictionary and the page
shell from the current preview file, and rebuilds only the PAGES object.
"""
import json, re, sys, pathlib

ROOT = pathlib.Path(__file__).parent
REPO = ROOT.parent
PREVIEW = ROOT.parent / "site-preview.html"

PAGES = [
    ("home", "index.md"),
    ("setup", "docs/setup.md"),
    ("programme", "docs/programme.md"),
    ("practicals", "docs/practicals/index.md"),
    ("p1", "docs/practicals/01-predict.md"),
    ("p2", "docs/practicals/02-interpret.md"),
    ("p3", "docs/practicals/03-compare.md"),
    ("p4", "docs/practicals/04-design.md"),
    ("team", "docs/team.md"),
    ("resources", "docs/resources.md"),
    ("faq", "docs/faq.md"),
]

LINKMAP = {
    "setup.md": "setup", "programme.md": "programme", "team.md": "team",
    "resources.md": "resources", "faq.md": "faq",
    "practicals/index.md": "practicals", "index.md": "home",
    "practicals/01-predict.md": "p1", "practicals/02-interpret.md": "p2",
    "practicals/03-compare.md": "p3", "practicals/04-design.md": "p4",
    "01-predict.md": "p1", "02-interpret.md": "p2",
    "03-compare.md": "p3", "04-design.md": "p4",
    "docs/practicals/01-predict.md": "p1", "docs/practicals/02-interpret.md": "p2",
    "docs/practicals/03-compare.md": "p3", "docs/practicals/04-design.md": "p4",
    "docs/programme.md": "programme", "docs/team.md": "team",
}

TOC_TOKEN = '<div class="toc-slot"></div>' 


def slugify(text):
    t = re.sub(r"<[^>]+>", "", text)
    t = t.replace("&amp;", "").replace("&", "")
    t = t.lower()
    t = re.sub(r"[^\w\s-]", "", t)
    t = re.sub(r"[\s_]+", "-", t).strip("-")
    return t


def preprocess(md):
    # front matter
    if md.startswith("---"):
        md = md.split("---", 2)[2].lstrip("\n")
    # jekyll image helper
    md = re.sub(r"\{\{\s*'(/[^']+)'\s*\|\s*relative_url\s*\}\}",
                lambda m: "@@IMG:" + m.group(1).lstrip("/") + "@@", md)
    # TOC marker
    md = re.sub(r"^1\. TOC\n\{:toc\}\s*$", TOC_TOKEN, md, flags=re.M)
    md = md.replace("{: .no_toc }\n", "")
    # HTML comments -> gap divs
    def gap(m):
        body = m.group(1).strip()
        body = re.sub(r"^FILL IN:?\s*", "", body)
        body = re.sub(r"\s+", " ", body).strip()
        if not body:
            body = "Content to be written."
        return ('<div class="gap" markdown="0"><span class="gap-label">To write</span>'
                '<span>' + body.replace("&", "&amp;").replace("<", "&lt;") + "</span></div>")
    md = re.sub(r"<!--(.*?)-->", gap, md, flags=re.S)
    return md


def postprocess(html):
    # kramdown-style {: .class } applied to the preceding block
    def attr(m):
        classes = " ".join(c[1:] for c in m.group(1).split() if c.startswith("."))
        return "@@ATTR:%s@@" % classes
    html = re.sub(r"<p>\{:\s*([^}]+)\s*\}</p>", attr, html)

    def inline_attr(m):
        classes = " ".join(c[1:] for c in m.group(2).split() if c.startswith("."))
        return '<p class="%s">%s</p>' % (classes, m.group(1).rstrip())
    html = re.sub(r"<p>(.*?)\n\{:\s*([^}]+?)\s*\}</p>", inline_attr, html, flags=re.S)

    out = []
    pending = None
    for chunk in re.split(r"(@@ATTR:[^@]*@@)", html):
        m = re.match(r"@@ATTR:([^@]*)@@", chunk)
        if m:
            classes = m.group(1)
            if out:
                # attach to the previous closed block
                prev = out[-1]
                tagm = None
                for t in re.finditer(r"<(p|ul|ol|table|h[1-6])\b", prev):
                    tagm = t
                if tagm:
                    i = tagm.end()
                    prev = prev[:i] + ' class="%s"' % classes + prev[i:]
                    out[-1] = prev
            pending = classes
            continue
        if pending and chunk.strip().startswith("<blockquote>"):
            titles = {"note": "Note", "warning": "Careful", "tip": "Try this",
                      "facilitator": "Facilitator note"}
            kind = pending.split()[0]
            title = titles.get(kind, kind.title())
            chunk = chunk.replace(
                "<blockquote>",
                '<blockquote class="callout callout-%s">\n<p class="callout-title">%s</p>'
                % (kind, title), 1)
            # the attribute belonged to the following blockquote: undo the earlier attach
            if len(out) and 'class="%s"' % pending in out[-1]:
                out[-1] = out[-1].replace(' class="%s"' % pending, "", 1)
        pending = None
        out.append(chunk)
    html = "".join(out)

    # heading ids
    def hid(m):
        level, attrs, text = m.group(1), m.group(2), m.group(3)
        if "id=" in attrs:
            return m.group(0)
        return "<h%s%s id=\"%s\">%s</h%s>" % (level, attrs, slugify(text), text, level)
    html = re.sub(r"<h([1-6])([^>]*)>(.*?)</h\1>", hid, html, flags=re.S)

    # internal links
    def link(m):
        href = m.group(1)
        base = href.split("#")[0]
        slug = LINKMAP.get(base)
        if slug:
            return '<a href="#" data-go="%s">' % slug
        return m.group(0)
    html = re.sub(r'<a href="([^":]+\.md[^"]*)">', link, html)
    return html


def build_toc(html):
    items = re.findall(r'<h2[^>]*id="([^"]+)"[^>]*>(.*?)</h2>', html, flags=re.S)
    if not items:
        return ""
    lis = "".join('<li><a href="#%s">%s</a></li>' % (i, re.sub(r"<[^>]+>", "", t))
                  for i, t in items)
    return '<nav class="page-toc"><p>On this page</p><ul>%s</ul></nav>' % lis


def render(path):
    import markdown
    md = preprocess(path.read_text())
    html = markdown.markdown(
        md,
        extensions=["tables", "fenced_code", "md_in_html", "sane_lists"],
    )
    html = postprocess(html)
    if '<div class="toc-slot"></div>' in html:
        html = html.replace('<div class="toc-slot"></div>', build_toc(html))
    return html


def main():
    pages = {slug: render(REPO / rel) for slug, rel in PAGES}
    shell = PREVIEW.read_text()
    start = shell.index("const PAGES = ")
    end = shell.index(";\nconst deref", start)
    new = shell[:start] + "const PAGES = " + json.dumps(pages, ensure_ascii=False) + shell[end:]
    PREVIEW.write_text(new)
    print("rebuilt %d pages, %d bytes" % (len(pages), len(new)))


if __name__ == "__main__":
    main()
