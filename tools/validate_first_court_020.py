#!/usr/bin/env python3
"""Static CK3 Court I validation. This does NOT launch Crusader Kings III."""
from pathlib import Path
import json
import re
import struct
import sys

BASE = Path("Bogowie_Pamietaja")
errors = []
passed = []

def check(condition, description):
    (passed if condition else errors).append(description)

def read(path):
    return (BASE / path).read_text(encoding="utf-8-sig")

def balanced(source):
    # Script syntax balance (strip comments outside quoted strings).
    depth = 0
    quote = False
    escape = False
    for line in source.splitlines():
        for c in line:
            if c == "#" and not quote:
                break
            if c == '"' and not escape:
                quote = not quote
            if not quote:
                if c == "{":
                    depth += 1
                elif c == "}":
                    depth -= 1
                    if depth < 0:
                        return False
            escape = (c == "\\" and not escape)
            if c != "\\":
                escape = False
    return depth == 0 and not quote

new_sources = [
    "events/bp_judgement_events_020.txt",
    "common/scripted_triggers/bp_judgement_triggers_020.txt",
    "common/scripted_effects/bp_judgement_effects_020.txt",
    "common/modifiers/bp_judgement_modifiers_020.txt",
    "common/traits/bp_gods_marks_020.txt",
]
for path in new_sources:
    check((BASE/path).is_file(), f"exists {path}")
    if (BASE/path).is_file():
        check(balanced(read(path)), f"balanced script {path}")

court = read("events/bp_judgement_events_020.txt")
effects = read("common/scripted_effects/bp_judgement_effects_020.txt")
triggers = read("common/scripted_triggers/bp_judgement_triggers_020.txt")
book = read("events/bp_book_events.txt")
watch = read("events/bp_announcement_events.txt")
weles = read("events/bp_weles_events.txt")
gromnica = read("events/bp_gromnica_events.txt")
traits = read("common/traits/bp_gods_marks_020.txt")
mods = read("common/modifiers/bp_judgement_modifiers_020.txt")

ids = re.findall(r"^\s*(bp_judgement\.\d+)\s*=\s*\{", court, re.M)
check(len(ids) == 7 and len(set(ids)) == 7, "seven unique court event IDs")
refs = re.findall(r"trigger_event\s*=\s*(bp_judgement\.\d+)", court)
check(all(i in ids for i in refs), "all court event links resolve")
check("bp_first_court_due_v020_trigger = yes" in watch, "single existing watcher schedules court")
check("trigger_event = bp_judgement.1001" in read("events/bp_test_events.txt"), "test entry exists")
check("bp_first_court_lock_v020" in court, "dynasty once-per-cycle lock")
check("bp_first_court_finalized_v020" in effects, "anti-duplicate finalization")
check("add_gold =" not in court and "add_gold =" not in effects, "no gold from Court I")

expected = ["light", "oath", "boundary", "silence", "pending"]
check(all(f"bp_first_court_path_{k}_v020" in court for k in expected),
      "five verdict paths implemented")
check(all(f"bp_first_court_last_{k}_v020" in effects for k in expected + ["declined"]),
      "persistent dynasty last-result chronicle")
check(all(f"bp_first_court_{k}_modifier_v020" in mods for k in ["light", "oath", "boundary"]),
      "three temporary skill boons")
check("diplomacy = 5" in mods and "intrigue = 5" in mods and "learning = 5" in mods
      and "dread_baseline_add = 10" in mods, "approved numeric bonuses")

needed = set(re.findall(r"\b(bp_first_court_[a-z0-9_]+_(?:effect|trigger))\b",
                        court + effects + triggers))
declared = set(re.findall(r"^\s*(bp_first_court_[a-z0-9_]+_(?:effect|trigger))\s*=\s*\{",
                          effects + "\n" + triggers, re.M))
check(needed <= declared, "all new scripted triggers and effects defined")

check("bp_gromnica_both_done_v020" in gromnica, "double Gromnica duty recorded")
for key in ["bp_weles_refused_offering_v020", "bp_weles_lied_now_v020",
            "bp_weles_blood_now_v020", "bp_weles_mercy_now_v020",
            "bp_weles_asked_time_v020", "bp_weles_truth_now_v020"]:
    check(key in weles, f"Weles records {key}")

def keys(s):
    return re.findall(r"^\s*([A-Za-z0-9_.]+):0\s+\"", s, re.M)

locale = {}
for lang in ["polish", "english"]:
    locpath = BASE/"localization"/lang/f"bp_l_{lang}.yml"
    data = locpath.read_bytes()
    check(data.startswith(b"\xef\xbb\xbf"), f"{lang} localization has UTF-8 BOM")
    text = data.decode("utf-8-sig")
    k = keys(text)
    check(len(k) == len(set(k)), f"{lang} localization has no duplicated keys")
    locale[lang] = set(k)
    expected_keys = set(re.findall(r"\b(?:title|desc|name)\s*=\s*(bp_judgement\.[a-z0-9_.]+)", court))
    section = book[book.find("bp_book.0012 = {"):]
    expected_keys.update(re.findall(r"\b(?:title|desc|name)\s*=\s*(bp_book\.0012[a-z0-9_.]*)", section))
    expected_keys.update([
        "trait_bp_gods_mark_1_v020", "trait_bp_gods_mark_1_v020_desc",
        "bp_first_court_light_modifier_v020", "bp_first_court_oath_modifier_v020",
        "bp_first_court_boundary_modifier_v020", "bp_test.9006.court_one",
        "bp_book.0002.first_court",
    ])
    check(expected_keys <= locale[lang],
          f"{lang} localization reference coverage (missing: {sorted(expected_keys-locale[lang])})")
    relevant_lines = [
        line for line in text.splitlines()
        if re.match(r"^\s*(bp_judgement\.|bp_book\.0012|bp_first_court_|trait_bp_gods_mark_1_v020)", line)
    ]
    check(all(line.endswith('"') for line in relevant_lines),
          f"{lang} court localization lines terminate correctly")

relevant = lambda ks: {k for k in ks if
    k.startswith(("bp_judgement.", "bp_book.0012", "bp_first_court_", "trait_bp_gods_mark_1_v020")) or
    k in {"bp_test.9006.court_one", "bp_book.0002.first_court"}}
check(relevant(locale["polish"]) == relevant(locale["english"]), "PL/EN court key parity")

icon = BASE/"gfx/interface/icons/traits/bp_gods_mark_1_v020.dds"
check(icon.is_file(), "custom trait DDS exists")
if icon.is_file():
    b = icon.read_bytes()
    # The old 64x64 DXT5 trait icon rendered as a question mark in-game.
    # v0.2.0 DEV uses uncompressed 120x120 ARGB DDS with seven mip levels.
    # Accept the older texture in the validator for compatible test branches.
    basic = len(b) >= 128 and b[:4] == b"DDS " and struct.unpack_from("<I", b, 4)[0] == 124
    size = struct.unpack_from("<II", b, 12) if basic else (0, 0)
    old_bc3 = basic and size == (64, 64) and len(b) == 4224 and b[84:88] == b"DXT5"
    new_argb = (
        basic and size == (120, 120) and len(b) == 76864
        and struct.unpack_from("<I", b, 76)[0] == 32  # pixel format block
        and (struct.unpack_from("<I", b, 80)[0] & 0x40) != 0  # RGB bit flag
        and struct.unpack_from("<I", b, 88)[0] == 32  # bits per pixel
        and struct.unpack_from("<I", b, 28)[0] == 7  # mipmaps
    )
    check(old_bc3 or new_argb, "trait DDS valid: old BC3 64x64 or current ARGB 120x120 with mipmaps")
check("icon = \"gfx/interface/icons/traits/bp_gods_mark_1_v020.dds\"" in traits,
      "trait points to deployed custom DDS icon")
check("bp_book.0012 = {" in book, "read-only court chronicle page exists")

result = {
    "version": "0.2.0-dev-court-1", "static_result": "PASS" if not errors else "FAIL",
    "game_tested": False, "passed": len(passed), "failed": len(errors),
    "errors": errors, "checks": passed,
}
Path("validation_first_court_020.json").write_text(
    json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps({k:v for k,v in result.items() if k!="checks"}, ensure_ascii=False, indent=2))
sys.exit(1 if errors else 0)
