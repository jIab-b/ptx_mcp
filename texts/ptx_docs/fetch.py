#!/usr/bin/env python3
"""Fetch the latest PTX ISA HTML from NVIDIA and convert it to ptx_full.md.

Usage:
    python fetch.py [output.md]
    python fetch.py --from-file local.html [output.md]

Defaults:
    source: PTX_ISA_URL (canonical "latest" PTX ISA page)
    output: ptx_full.md (same directory as script)

After running, regenerate the per-section files with:
    python decompose.py
"""
from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path

PTX_ISA_URL = "https://docs.nvidia.com/cuda/parallel-thread-execution/index.html"

VOID = {"br", "img", "hr", "meta", "link", "input", "col", "area", "base", "source", "wbr"}
INLINE_TAGS = {"a", "code", "em", "strong", "b", "i", "span", "sub", "sup",
               "abbr", "kbd", "cite", "tt", "samp", "var", "q", "u", "s"}
LANG_MAP = {"text": "", "c++": "cpp", "cpp": "cpp", "cuda": "cuda", "ptx": "ptx",
            "bash": "bash", "shell": "bash", "python": "python", "console": ""}


class Node:
    __slots__ = ("tag", "attrs", "children")

    def __init__(self, tag, attrs):
        self.tag = tag
        self.attrs = dict(attrs)
        self.children = []


class TreeBuilder(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("#root", {})
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        node = Node(tag, attrs)
        self.stack[-1].children.append(node)
        if tag not in VOID:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.stack[-1].children.append(Node(tag, attrs))

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]
                return

    def handle_data(self, data):
        self.stack[-1].children.append(data)


def classes(node):
    return node.attrs.get("class", "").split()


def has_cls(node, c):
    return c in classes(node)


def is_headerlink(n):
    return isinstance(n, Node) and n.tag == "a" and has_cls(n, "headerlink")


def collapse(s):
    return re.sub(r"[ \t\r\n]+", " ", s).strip()


def find(node, tag):
    for c in node.children:
        if isinstance(c, Node):
            if c.tag == tag:
                return c
            r = find(c, tag)
            if r is not None:
                return r
    return None


def find_direct(node, tag):
    for c in node.children:
        if isinstance(c, Node) and c.tag == tag:
            return c
    return None


def raw_text(node):
    out = []

    def walk(n):
        if isinstance(n, str):
            out.append(n)
        else:
            for c in n.children:
                walk(c)

    walk(node)
    return "".join(out)


def inline(node, strip_links=False):
    out = []
    for c in node.children:
        if isinstance(c, str):
            out.append(c)
        elif is_headerlink(c):
            continue
        else:
            t = c.tag
            if t in ("strong", "b"):
                s = inline(c, strip_links).strip()
                out.append(f"**{s}**" if s else "")
            elif t in ("em", "i", "var"):
                s = inline(c, strip_links).strip()
                out.append(f"*{s}*" if s else "")
            elif t == "code":
                s = raw_text(c).strip()
                out.append(f"`{s}`" if s else "")
            elif t == "a":
                txt = inline(c, strip_links).strip()
                href = c.attrs.get("href", "")
                if href and txt and not strip_links:
                    out.append(f"[{txt}]({href})")
                else:
                    out.append(txt)
            elif t == "br":
                out.append(" ")
            else:
                out.append(inline(c, strip_links))
    return "".join(out)


def detect_lang(div):
    for tok in classes(div):
        if tok.startswith("highlight-"):
            lang = tok[len("highlight-"):]
            return LANG_MAP.get(lang, lang)
    return ""


def fence(code, lang=""):
    code = code.strip("\n")
    return f"```{lang}\n{code}\n```"


def cell_text(td):
    return collapse(inline(td)).replace("|", "\\|")


def _span_grid(rowlist):
    """Expand a list of <tr> nodes into a rectangular grid, honoring colspan/rowspan."""
    grid = []
    carry = {}  # col -> (text, rows_remaining)
    for tr in rowlist:
        tcells = [c for c in tr.children if isinstance(c, Node) and c.tag in ("td", "th")]
        row = []
        col = 0
        ci = 0
        while True:
            if col in carry:
                text, rem = carry[col]
                row.append(text)
                if rem - 1 > 0:
                    carry[col] = (text, rem - 1)
                else:
                    del carry[col]
                col += 1
                continue
            if ci < len(tcells):
                cell = tcells[ci]
                ci += 1
                text = cell_text(cell)
                cs = max(1, int(cell.attrs.get("colspan", "1") or 1))
                rs = max(1, int(cell.attrs.get("rowspan", "1") or 1))
                for _ in range(cs):
                    row.append(text)
                    if rs > 1:
                        carry[col] = (text, rs - 1)
                    col += 1
                continue
            if any(k >= col for k in carry):
                row.append("")
                col += 1
                continue
            break
        grid.append(row)
    return grid


def render_table(table):
    cap = find_direct(table, "caption")
    caption = collapse(inline(cap)) if cap else ""

    def rows(parent):
        return [c for c in parent.children if isinstance(c, Node) and c.tag == "tr"]

    thead = find_direct(table, "thead")
    tbody = find_direct(table, "tbody")
    head_grid = _span_grid(rows(thead)) if thead else []
    body_grid = _span_grid(rows(tbody) if tbody else rows(table))

    if head_grid:
        header = head_grid[0]
        body = head_grid[1:] + body_grid
    else:
        header = []
        body = body_grid

    ncol = max([len(header)] + [len(r) for r in body] or [0])
    if ncol == 0:
        return ""
    if not header:
        header = [""] * ncol

    def pad(r):
        return r + [""] * (ncol - len(r))

    lines = []
    if caption:
        lines.append(f"**{caption}**\n")
    lines.append("| " + " | ".join(pad(header)) + " |")
    lines.append("| " + " | ".join(["---"] * ncol) + " |")
    for r in body:
        lines.append("| " + " | ".join(pad(r)) + " |")
    return "\n".join(lines)


def render_list(node, ordered, depth=0):
    out = []
    idx = 1
    for li in node.children:
        if isinstance(li, str) or li.tag != "li":
            continue
        out.append(render_li(li, ordered, idx, depth))
        idx += 1
    return "\n".join(out)


def render_li(li, ordered, idx, depth):
    indent = "  " * depth
    marker = f"{idx}. " if ordered else "- "
    lead = []
    tail = []
    for c in li.children:
        if isinstance(c, str):
            if c.strip():
                lead.append(collapse(c))
        elif c.tag in ("ul", "ol"):
            tail.append(render_list(c, c.tag == "ol", depth + 1))
        elif c.tag == "p":
            lead.append(collapse(inline(c)))
        elif c.tag in INLINE_TAGS:
            lead.append(collapse(inline(c)))
        else:
            block = "\n\n".join(b for b in render_blocks(c) if b)
            if block:
                tail.append("\n".join(indent + "  " + ln for ln in block.split("\n")))
    text = " ".join(x for x in lead if x).strip()
    out = [f"{indent}{marker}{text}"]
    out.extend(t for t in tail if t)
    return "\n".join(out)


def render_dl(dl):
    out = []
    for c in dl.children:
        if isinstance(c, str):
            continue
        if c.tag == "dt":
            term = collapse(inline(c))
            if term:
                out.append(f"**{term}**")
        elif c.tag == "dd":
            for b in render_blocks(c):
                if b:
                    out.append(b)
    return "\n\n".join(out)


def render_blocks(node):
    blocks = []
    for c in node.children:
        if isinstance(c, str):
            txt = collapse(c)
            if txt:
                blocks.append(txt)
            continue
        t = c.tag
        if t in ("script", "style", "footer", "nav"):
            continue
        if c.attrs.get("role") == "navigation":
            continue
        if re.fullmatch(r"h[1-6]", t):
            txt = collapse(inline(c, strip_links=True))
            if txt:
                blocks.append("#" * int(t[1]) + " " + txt)
        elif t == "p":
            txt = collapse(inline(c))
            if txt:
                blocks.append(txt)
        elif t == "pre":
            blocks.append(fence(raw_text(c)))
        elif t == "div" and any(tok.startswith("highlight-") for tok in classes(c)):
            pre = find(c, "pre")
            if pre is not None:
                blocks.append(fence(raw_text(pre), detect_lang(c)))
        elif t == "div" and has_cls(c, "highlight"):
            pre = find(c, "pre")
            if pre is not None:
                blocks.append(fence(raw_text(pre)))
        elif t in ("ul", "ol"):
            blocks.append(render_list(c, t == "ol"))
        elif t == "table":
            blocks.append(render_table(c))
        elif t == "dl":
            blocks.append(render_dl(c))
        elif t == "blockquote":
            inner = "\n\n".join(b for b in render_blocks(c) if b)
            blocks.append("\n".join("> " + ln for ln in inner.split("\n")))
        else:
            blocks.extend(render_blocks(c))
    return [b for b in blocks if b]


def html_to_markdown(html):
    tb = TreeBuilder()
    tb.feed(html)
    main = None

    def search(node):
        nonlocal main
        if main is not None:
            return
        for c in node.children:
            if isinstance(c, Node):
                if c.attrs.get("role") == "main" or "document" in classes(c):
                    main = c
                    return
                search(c)

    search(tb.root)
    if main is None:
        main = tb.root
    blocks = render_blocks(main)
    text = "\n\n".join(blocks)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def detect_version(html):
    m = re.search(r"PTX ISA (\d+\.\d+) documentation", html)
    return m.group(1) if m else "unknown"


def download(url):
    try:
        import requests
        r = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (ptx_mcp fetch)"}, timeout=120)
        r.raise_for_status()
        return r.text
    except ImportError:
        import urllib.request
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (ptx_mcp fetch)"})
        with urllib.request.urlopen(req, timeout=120) as resp:
            return resp.read().decode("utf-8", "replace")


def main():
    args = sys.argv[1:]
    src_file = None
    if args and args[0] == "--from-file":
        src_file = args[1]
        args = args[2:]
    script_dir = Path(__file__).parent
    out_path = Path(args[0]) if args else script_dir / "ptx_full.md"

    if src_file:
        html = Path(src_file).read_text(encoding="utf-8")
    else:
        print(f"Downloading {PTX_ISA_URL}")
        html = download(PTX_ISA_URL)

    version = detect_version(html)
    print(f"Detected PTX ISA version: {version}")
    md = html_to_markdown(html)
    out_path.write_text(md, encoding="utf-8")
    print(f"Wrote {out_path} ({len(md)} bytes, {md.count(chr(10))} lines)")


if __name__ == "__main__":
    main()
