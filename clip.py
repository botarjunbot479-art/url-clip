#!/usr/bin/env python3
"""Local URL aliases — Arjun Singh."""
from __future__ import annotations
import argparse, json
from pathlib import Path
DB = Path(__file__).with_name("clips.json")

def load() -> dict:
    return json.loads(DB.read_text()) if DB.exists() else {}

def save(d: dict) -> None:
    DB.write_text(json.dumps(d, indent=2))

def main() -> int:
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("add"); a.add_argument("name"); a.add_argument("url")
    g = sub.add_parser("get"); g.add_argument("name")
    sub.add_parser("list")
    args = p.parse_args()
    d = load()
    if args.cmd == "add":
        d[args.name] = args.url; save(d); print("saved", args.name)
    elif args.cmd == "get":
        print(d.get(args.name) or "not found"); return 0 if args.name in d else 1
    else:
        for k,v in d.items(): print(f"{k}\t{v}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
