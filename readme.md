# PTX ISA MCP Server

MCP server exposing the NVIDIA PTX ISA documentation as searchable, per-section markdown.

Tools:
- `search_ptx(query, max_results=10)` — keyword search over the docs, returns matching files.
- `get_ptx_file(filename)` — fetch a single section by filename.

## Docs

Bundled docs track **PTX ISA 9.3** (the latest release).

Source: <https://docs.nvidia.com/cuda/parallel-thread-execution/index.html>

To refresh to the latest PTX ISA:

```
cd texts/ptx_docs
python fetch.py        # downloads the latest HTML -> ptx_full.md
python decompose.py    # splits ptx_full.md -> sections/
```
