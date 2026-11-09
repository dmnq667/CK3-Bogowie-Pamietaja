#!/usr/bin/env python3
"""Audit CK3 mod festival click cascades.

Counts visible event modals reachable from each festival entry event through
immediate trigger_event calls. Does NOT count delayed divine-story episodes as
festival modal clicks. Adds a preceding festival announcement where present.

Usage:
  python3 tools/audit_festival_flows_040.py
  python3 tools/audit_festival_flows_040.py --enforce
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EVENTS = ROOT / "Bogowie_Pamietaja" / "events"
FESTIVALS = {
    "Gromnica": "bp_gromnica.1001",
    "Siedem Nocy Welesa": "bp_weles.2001",
    "Wiosenny Nowy Rok": "bp_spring.3001",
    "Jare Gody": "bp_jare.4001",
    "Gaik / Turzyca": "bp_gaik.5001",
    "Dziady wiosenne": "bp_dziady.6001",
    "Stado": "bp_stado.7001",
    "Noc Kupaly": "bp_kupala.8001",
    "Swieto Peruna": "bp_perun.9101",
    "Dozynki": "bp_harvest.9201",
    "Dziady jesienne": "bp_autumn.9301",
    "Szczodre Gody": "bp_szczodre.9401",
}
PATTERN = re.compile(r"(?m)^([a-z0-9_]+\.\d+)\s*=\s*\{")
EVENT_CALL = re.compile(r"\btrigger_event\s*=\s*")
EVENT_NAME = re.compile(r"^(bp_[a-z0-9_]+\.\d+)$")
TARGET = re.compile(r"\bid\s*=\s*(bp_[a-z0-9_]+\.\d+)")


def balanced(text: str, open_index: int):
    """Return balanced brace block and end position, ignoring quoted content."""
    assert text[open_index] == "{"
    depth = 0
    quote = False
    escaped = False
    for k in range(open_index, len(text)):
        c = text[k]
        if escaped:
            escaped = False
            continue
        if c == "\\" and quote:
            escaped = True
            continue
        if c == '"':
            quote = not quote
            continue
        if quote:
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return text[open_index:k+1], k+1
    raise ValueError(f"Unbalanced brace at {open_index}")


def immediate_calls(event_body: str):
    targets = set()
    for m in EVENT_CALL.finditer(event_body):
        pos = m.end()
        while pos < len(event_body) and event_body[pos].isspace():
            pos += 1
        if pos >= len(event_body):
            continue
        if event_body[pos] == "{":
            value, _ = balanced(event_body, pos)
            found = TARGET.search(value)
            if found and not re.search(r"\bdays\s*=", value):
                targets.add(found.group(1))
        else:
            name = re.match(r"bp_[a-z0-9_]+\.\d+", event_body[pos:])
            if name:
                targets.add(name.group())
    return targets


def parse_events():
    entries = {}
    for file in sorted(EVENTS.glob("*.txt")):
        text = file.read_text(encoding="utf-8-sig")
        for match in PATTERN.finditer(text):
            value, _ = balanced(text, match.end()-1)
            name = match.group(1)
            if name in entries:
                raise AssertionError(f"Duplicate event ID {name}")
            entries[name] = {
                "file": str(file.relative_to(ROOT)),
                "hidden": bool(re.search(r"\bhidden\s*=\s*yes\b", value)),
                "edges": sorted(immediate_calls(value)),
            }
    return entries


def route(node: str, entries: dict, visited: frozenset):
    if node not in entries or node in visited:
        return (0, [])
    item = entries[node]
    candidates = [route(t, entries, visited | {node}) for t in item["edges"]]
    best_count, best_path = max(candidates, default=(0, []), key=lambda x: x[0])
    return best_count + (0 if item["hidden"] else 1), [node, *best_path]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--enforce", action="store_true", help="Fail if any festival exceeds two visible windows")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--exactly-two", action="store_true", help="Fail unless every festival has exactly two visible windows")
    args = parser.parse_args()
    entries = parse_events()
    assert all(start in entries for start in FESTIVALS.values())
    rows = []
    for festival, start in FESTIVALS.items():
        direct, path = route(start, entries, frozenset())
        notice = sorted(
            key for key, item in entries.items()
            if key.startswith("bp_announcement.")
            and start in item["edges"]
            and not item["hidden"]
        )
        # The existence of one festival announcement is enough; alternatives
        # do not stack when their triggers are mutually exclusive.
        max_windows = direct + (1 if notice else 0)
        rows.append({
            "festival": festival,
            "start": start,
            "visible_event_chain_upper_bound": direct,
            "announcements": notice,
            "total_modal_upper_bound": max_windows,
            "chain": path,
            "passes_two_window_rule": max_windows <= 2,
        })
    result = {
        "events_defined": len(entries),
        "festivals": rows,
        "all_pass": all(row["passes_two_window_rule"] for row in rows),
        "note": "Upper bound of immediate event chains, not a runtime simulation.",
    }
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        for row in rows:
            flag = "PASS" if row["passes_two_window_rule"] else "FAIL"
            print(f"{flag} {row['festival']}: {row['total_modal_upper_bound']} windows; "
                  f"chain: {' -> '.join(row['chain'])}")
        print("ALL PASS:", result["all_pass"])
    if args.enforce and not result["all_pass"]:
        raise SystemExit(1)
    if args.exactly_two and any(row["total_modal_upper_bound"] != 2 for row in rows):
        raise SystemExit("Two-window rule failed: every festival must have EXACTLY 2 modals.")


if __name__ == "__main__":
    main()
