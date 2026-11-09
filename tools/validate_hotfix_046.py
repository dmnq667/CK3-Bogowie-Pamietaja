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
assert struct.unpack_from("<II", icon, 12) == (120, 120)
assert struct.unpack_from("<I", icon, 28)[0] == 7
assert len(icon) == 76864, len(icon)
trait_path = MOD / "common/traits/bp_gods_marks_020.txt"
assert trait_path.read_bytes().startswith(b"\xef\xbb\xbf"), "Trait definition must use UTF-8 BOM"
trait = trait_path.read_text(encoding="utf-8-sig")
assert "bp_gods_mark_1_v020 = {" in trait
assert "icon =" not in trait, "CK3 automatically resolves gfx/interface/icons/traits/<trait>.dds"
assert "can_lose" not in trait, "CK3 does not accept can_lose as a modifier"
for lang, expected in [("polish", "Cena ofiary"), ("english", "The Price of Sacrifice")]:
    loc = (MOD / f"localization/{lang}/bp_l_{lang}.yml").read_text(encoding="utf-8-sig")
    assert f'bp_weles.2004.t:0 "{expected}"' in loc
    assert loc.count("Awaryjne przywołanie święta") == (12 if lang == "polish" else 0)
    assert "samodzielnie uruchomisz" not in loc
    assert "start the event manually" not in loc
    assert "bp_book.status_announced_019:0" in loc
print("PASS: 12 silent festival decisions; PL/EN text; 120x120 DDS with 7 mips; automatic icon lookup; UTF-8 BOM; untouched event structure")
