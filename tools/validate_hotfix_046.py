#!/usr/bin/env python3
"""Static QA for 0.4.6 hotfix. CK3 gameplay still requires player validation."""
from pathlib import Path
import re, struct
MOD = Path(__file__).resolve().parent.parent / "Bogowie_Pamietaja"
DECISIONS = (MOD / "common/decisions/bp_decisions.txt").read_text(encoding="utf-8-sig")
FEASTS = ["gromnica", "weles_week", "spring", "jare", "gaik", "dziady",
          "stado", "kupala", "perun", "harvest", "autumn", "szczodre"]
for name in FEASTS:
    match = re.search(r"(?ms)^bp_" + name + r"_decision\s*=\s*\{(.*?)^\}", DECISIONS)
    assert match, name
    assert "should_create_alert = { always = no }" in match.group(1), name
    assert "effect = { trigger_event = bp_" in match.group(1), name
icon = (MOD / "gfx/interface/icons/traits/bp_gods_mark_1_v020.dds").read_bytes()
assert icon[:4] == b"DDS "
assert struct.unpack_from("<II", icon, 12) == (128, 128)
assert struct.unpack_from("<I", icon, 28)[0] == 8
assert len(icon) == 87508, len(icon)
trait = (MOD / "common/traits/bp_gods_marks_020.txt").read_text(encoding="utf-8")
assert "bp_gods_mark_1_v020.dds" in trait
for lang, expected in [("polish", "Cena ofiary"), ("english", "The Price of Sacrifice")]:
    loc = (MOD / f"localization/{lang}/bp_l_{lang}.yml").read_text(encoding="utf-8-sig")
    assert f'bp_weles.2004.t:0 "{expected}"' in loc
    assert loc.count("Awaryjne przywołanie święta") == (12 if lang == "polish" else 0)
    assert "samodzielnie uruchomisz" not in loc
    assert "start the event manually" not in loc
    assert "bp_book.status_announced_019:0" in loc
print("PASS: 12 silent festival decisions; PL/EN text; 128x128 DDS with 8 mips; untouched event structure")
