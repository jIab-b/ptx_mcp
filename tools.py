"""PTX doc MCP tools."""
from __future__ import annotations
import subprocess
from pathlib import Path

_DOCS = Path(__file__).parent / "texts" / "ptx_docs" / "sections"

def search_ptx(query: str, max_results: int = 10) -> dict:
    """Search docs, return file list only."""
    try:
        r = subprocess.run(["grep", "-l", "-i", "-r", query, str(_DOCS)], capture_output=True, text=True, timeout=10)
        files = [Path(f) for f in r.stdout.strip().split("\n") if f and f.endswith(".md")]
    except Exception as e:
        return {"error": str(e)}
    if not files: return {"query": query, "matches": []}
    matches = [{"file": f.name, "title": f.read_text().split("\n")[0].lstrip("#").strip()[:80]} for f in files[:max_results] if f.exists()]
    return {"query": query, "total": len(files), "matches": matches}

def get_ptx_file(filename: str) -> dict:
    """Fetch doc by filename."""
    p = _DOCS / filename if "/" not in filename else Path(filename)
    if not p.exists():
        m = list(_DOCS.glob(f"*{filename}*"))
        p = m[0] if m else None
    if not p or not p.exists(): return {"error": f"Not found: {filename}"}
    c = p.read_text()
    return {"file": p.name, "content": c, "lines": c.count("\n")}
