#!/usr/bin/env python3
"""CK3 Gniew i Laska Bogow 0.4.0 static story validation.
Validates event wiring and localization, NOT in-game effects or AI balance.
"""
from pathlib import Path
from subprocess import run
import json
import re

ROOT = Path(__file__).resolve().parent.parent
MOD = ROOT / "Bogowie_Pamietaja"
EVENTS = MOD / "events"
SPECS = {
    "gromnica":1001,
    "weles":2001,
    "spring":3001,
    "jare":4001,
    "gaik":5001,
    "dziady":6001,
    "stado":7001,
    "kupala":8001,
    "perun":9101,
    "harvest":9201,
    "autumn":9301,
    "szczodre":9401,
}
LEGACY = [
    "bp_autumn.9302", "bp_autumn.9303", "bp_autumn.9304",
    "bp_autumn.9305", "bp_autumn.9306", "bp_autumn.9307", "bp_autumn.9308",
]
needed = set()


def balanced(text, index):
    assert text[index] == "{"
    depth, string, escaped, comment = 0, False, False, False
    for i in range(index, len(text)):
        c = text[i]
        if c == "\n":
            comment = False
        if comment:
            continue
        if c == "#" and not string:
            comment = True
            continue
        if string and escaped:
            escaped = False
            continue
        if string and c == "\\":
            escaped = True
            continue
        if c == '"':
            string = not string
            continue
        if string:
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return text[index:i+1]
    raise ValueError(f"Unclosed event or file block near {index}")


def all_balanced(text, filename):
    q, esc, comment, depth = False, False, False, 0
    for c in text:
        if c == "\n":
            comment = False
        if comment:
            continue
        if c == "#" and not q:
            comment = True
            continue
        if q and esc:
            esc = False
            continue
        if q and c == "\\":
            esc = True
            continue
        if c == '"':
            q = not q
            continue
        if q:
            continue
        if c == "{":
            depth += 1
        if c == "}":
            depth -= 1
            assert depth >= 0, f"extra closing brace in {filename}"
    assert depth == 0 and not q, f"unbalanced braces or quotes in {filename}"


assert "0.4.0-dev" in (MOD/"descriptor.mod").read_text(encoding="utf-8-sig")

for filename in list(EVENTS.glob("*.txt")) + list((MOD/"common").rglob("*.txt")):
    all_balanced(filename.read_text(encoding="utf-8-sig"), filename)

for n, number in SPECS.items():
    p = EVENTS / f"bp_{n}_events.txt"
    text = p.read_text(encoding="utf-8-sig")
    event = f"bp_{n}.{number}"
    match = re.search(r"(?m)^"+re.escape(event)+r"\s*=\s*\{", text)
    assert match, f"Missing {event}"
    block = balanced(text, match.end()-1)
    assert "hidden = yes" not in block, f"{event} unexpectedly hidden"
    assert f"title = bp_040_{n}.t" in block, f"Wrong title for {event}"
    assert f"desc = bp_040_{n}.desc" in block, f"Wrong story for {event}"
    assert "bp_initialize_effect = yes" in block, f"Uninitialized {event}"
    assert "rite_lock" in block, f"Missing annual lock {event}"
    assert "bp_scene_" in block, f"No approved art in {event}"
    assert re.findall(r"\boption\s*=\s*\{", block), f"No player action in {event}"
    # No immediately visible event chain from the holiday. Timed divine
    # encounters are deliberate independent chapters outside the feast.
    assert not re.search(r"\btrigger_event\s*=\s*bp_", block), f"Immediate nested popup in {event}"
    for m in re.finditer(r"\btrigger_event\s*=\s*\{([^{}]+)\}", block):
        assert "days =" in m.group(1), f"Non-delayed event in {event}: {m.group(0)}"
    needed.update(re.findall(r"\b(?:title|desc)\s*=\s*(bp_040_[A-Za-z0-9_.]+)",block))
    needed.update(re.findall(r"\boption\s*=\s*\{\s*name\s*=\s*(bp_040_[A-Za-z0-9_.]+)",block))

all_events = "\n".join(p.read_text(encoding="utf-8-sig") for p in EVENTS.glob("*.txt"))
assert all_events.count("bp_040.5001 = {")==1
assert all_events.count("bp_040.5002 = {")==1
assert "death = { death_reason = death_murder }" in all_events
assert "death = { killer = root death_reason = death_execution }" in all_events
assert "has_character_flag = bp_040_weles_bargain_v040" in all_events
assert "bp_040_weles_judgement.desc_bargain" in all_events
assert "trigger_event = bp_autumn.9302" not in balanced(
    (EVENTS/"bp_autumn_events.txt").read_text(encoding="utf-8-sig"),
    re.search(r"bp_autumn\.9301\s*=\s*\{",(EVENTS/"bp_autumn_events.txt").read_text(encoding="utf-8-sig")).end()-1,
)

court = (EVENTS/"bp_judgement_events_020.txt").read_text(encoding="utf-8-sig")
m = re.search(r"(?m)^bp_judgement\.1001\s*=\s*\{",court)
court_block = balanced(court, m.end()-1)
assert "hidden = yes" in court_block, "Obsolete mystical court popup remains"
assert "bp_040_blood_v040" in court_block and "bp_040_mercy_v040" in court_block

blood_event = (EVENTS/"bp_040_blood_events.txt").read_text(encoding="utf-8-sig")
needed.update(re.findall(r"\b(?:title|desc)\s*=\s*(bp_040_[A-Za-z0-9_.]+)",blood_event))
needed.update(re.findall(r"\boption\s*=\s*\{\s*name\s*=\s*(bp_040_[A-Za-z0-9_.]+)",blood_event))
needed.add("bp_040_weles_judgement.desc_bargain")

for lang in ("polish","english"):
    p=MOD/"localization"/lang/f"bp_040_l_{lang}.yml"
    text=p.read_text(encoding="utf-8-sig")
    assert text.startswith(f"l_{lang}:")
    lines=re.findall(r"(?m)^\s*(bp_040_[A-Za-z0-9_.]+):0\s+\"(.*)\"\s*$",text)
    keys=[key for key,_ in lines]
    assert len(keys)==len(set(keys)),f"Duplicate localized keys: {lang}"
    missing=needed-set(keys)
    assert not missing,f"{lang} missing: {sorted(missing)}"
    assert len(keys)>=100,f"{lang}: insufficient localized narratives"
    assert all(len(val)>0 for _,val in lines)

# Verify that all festival announcements + entry events fit two windows.
run(["python3",str(ROOT/"tools/audit_festival_flows_040.py"),"--enforce"],check=True,cwd=ROOT)
run(["python3",str(ROOT/"tools/validate_gods_030.py")],check=True,cwd=ROOT)
result={
    "version":"0.4.0-dev",
    "festival_rewrites":len(SPECS),
    "new_blood_story_events":2,
    "distinct_new_localization_keys":len(needed),
    "maximum_holiday_windows_including_announcement":2,
    "hidden_first_court_uses_remembered_conduct":True,
    "runtime_tested":False,
    "static_pass":True,
}
(ROOT/"validation_story_040.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
print(json.dumps(result,indent=2))
