"""PTX doc MCP server."""
from __future__ import annotations
import json, sys
from .tools import search_ptx, get_ptx_file

TOOLS = [
    {"name": "search_ptx", "description": "Search PTX docs by keyword. Returns file list.", "inputSchema": {"type": "object", "properties": {"query": {"type": "string"}, "max_results": {"type": "integer"}}, "required": ["query"]}},
    {"name": "get_ptx_file", "description": "Fetch PTX doc by filename.", "inputSchema": {"type": "object", "properties": {"filename": {"type": "string"}}, "required": ["filename"]}},
]
HANDLERS = {"search_ptx": lambda a: search_ptx(a["query"], a.get("max_results", 10)), "get_ptx_file": lambda a: get_ptx_file(a["filename"])}

class MCPServer:
    def handle_request(self, req: dict) -> dict:
        m, i, p = req.get("method", ""), req.get("id"), req.get("params", {})
        if m == "initialize": return {"jsonrpc": "2.0", "id": i, "result": {"protocolVersion": "2024-11-05", "capabilities": {"tools": {}}, "serverInfo": {"name": "ptx-docs", "version": "0.5.0"}}}
        if m == "tools/list": return {"jsonrpc": "2.0", "id": i, "result": {"tools": TOOLS}}
        if m == "tools/call":
            n, a = p.get("name"), p.get("arguments", {})
            if n not in HANDLERS: return {"jsonrpc": "2.0", "id": i, "error": {"code": -32601, "message": f"Unknown: {n}"}}
            try: return {"jsonrpc": "2.0", "id": i, "result": {"content": [{"type": "text", "text": json.dumps(HANDLERS[n](a), indent=2)}]}}
            except Exception as e: return {"jsonrpc": "2.0", "id": i, "error": {"code": -32000, "message": str(e)}}
        return {"jsonrpc": "2.0", "id": i, "error": {"code": -32601, "message": f"Unknown: {m}"}}
    def run_stdio(self):
        while True:
            try:
                l = sys.stdin.readline()
                if not l: break
                sys.stdout.write(json.dumps(self.handle_request(json.loads(l))) + "\n"); sys.stdout.flush()
            except: continue

def create_server(): return MCPServer()
def run_server(): create_server().run_stdio()
if __name__ == "__main__": run_server()
