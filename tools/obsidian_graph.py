#!/usr/bin/env python3
"""Render Obsidian vault wikilink graph to PNG and send to a messaging platform.

Usage:
  python3 obsidian_graph.py                # render PNG only, print path
  OBSIDIAN_VAULT_PATH=~/Obsidian python3 obsidian_graph.py --send telegram
"""
import argparse
import os
import re
import subprocess
import tempfile
from pathlib import Path

VAULT = Path(os.environ.get("OBSIDIAN_VAULT_PATH", Path.home() / "Obsidian")).expanduser()

LINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")

def get_vault():
    return VAULT

def note_name(path: Path) -> str:
    return path.stem

def build_graph():
    vault = get_vault()
    notes = {}          # name -> Path
    links = {}          # name -> set of target names
    for md in sorted(vault.rglob("*.md")):
        if ".obsidian" in md.parts:
            continue
        name = note_name(md)
        notes[name] = md
        targets = set()
        try:
            text = md.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            text = ""
        for m in LINK_RE.finditer(text):
            tgt = m.group(1).strip()
            if tgt and tgt != name:
                targets.add(tgt)
        links[name] = targets
    return notes, links

def render_dot(notes, links, out_png):
    # build dot
    lines = ["digraph G {", "  rankdir=LR;", '  node [shape=box, style="rounded,filled", fontname="Helvetica", fillcolor="#dbeafe", color="#3b82f6", fontsize=11];',
             '  edge [color="#94a3b8", arrowhead=open];']
    for name in notes:
        safe = name.replace('"', '\\"')
        lines.append(f'  "{safe}";')
    for src, targets in links.items():
        for t in targets:
            # only draw if target currently a note; else draw as phantom node
            safe_src = src.replace('"', '\\"')
            safe_t = t.replace('"', '\\"')
            if t in notes:
                lines.append(f'  "{safe_src}" -> "{safe_t}";')
            else:
                lines.append(f'  "{safe_t}" [style=dashed, fillcolor="#fef9c3", color="#ca8a04", fontsize=10];')
                lines.append(f'  "{safe_src}" -> "{safe_t}" [style=dashed];')
    lines.append("}")
    dot = "\n".join(lines)
    with tempfile.NamedTemporaryFile("w", suffix=".dot", delete=False) as f:
        f.write(dot)
        dot_path = f.name
    try:
        subprocess.run(["dot", "-Tpng", dot_path, "-o", str(out_png)], check=True)
    finally:
        os.unlink(dot_path)
    return out_png

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=None)
    ap.add_argument("--send", default=None, help="platform target, e.g. telegram")
    args = ap.parse_args()

    notes, links = build_graph()
    if not notes:
        print("Tidak ada catatan di vault.", file=os.sys.stderr)
        return 1

    out = Path(args.out) if args.out else Path(tempfile.gettempdir()) / "obsidian-graph.png"
    render_dot(notes, links, out)
    print(f"PNG: {out}  (catatan: {len(notes)}, edge: {sum(len(v) for v in links.values())})")

    if args.send:
        target = args.send if ":" in args.send else f"{args.send}"
        send_script = (
            f'sh -c \'hermes send --to {target} "MEDIA:{out}" -s "Grafik Obsidian Vault"\'' 
        )
        r = subprocess.run(["hermes", "send", "--to", target, f"MEDIA:{out}", "-s", "Grafik Obsidian Vault"])
        if r.returncode == 0:
            print("Terkirim ke", target)
        else:
            print("Gagal kirim, rc", r.returncode, file=os.sys.stderr)
            return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())