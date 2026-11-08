#!/usr/bin/env python3
"""Static checks for 0.3.0 naturalistic deity and festival art.

This is NOT an in-game CK3 test.
"""
from pathlib import Path
import json
import re

ROOT=Path(__file__).resolve().parent.parent
MOD=ROOT/"Bogowie_Pamietaja"
DDS=MOD/"gfx/interface/illustrations/event_scene"
ART=(MOD/"common/event_backgrounds/bp_slavic_holiday_backgrounds.txt").read_text(encoding="utf-8-sig")
EXPECTED={
    "gromnica":[1], "weles":[2,3,4], "spring":[1,2],
    "jare":[1], "gaik":[1,2,3], "dziady":[1,2,3],
    "stado":[1,2], "kupala":[1,2], "perun":[1,2],
    "harvest":[1,2,3], "autumn":[1,2,3], "szczodre":[1,2,3],
}
texture_names={f"bp_{key}_{n:02d}.dds" for key,seq in EXPECTED.items() for n in seq}
texture_names.update(["bp_deity_weles_2020.dds","bp_deity_perun_9110.dds","bp_deity_mokosh_3010.dds"])
assert len(texture_names)==31
for filename in sorted(texture_names):
    data=(DDS/filename).read_bytes()
    assert data[:4]==b"DDS ", filename
    assert data[84:88]==b"DXT1", filename
    assert int.from_bytes(data[12:16],"little")==848,filename
    assert int.from_bytes(data[16:20],"little")==1592,filename
    assert len(data)==675136,filename
for missing in ["bp_gromnica_02.dds","bp_stado_03.dds","bp_kupala_03.dds","bp_perun_03.dds"]:
    assert not (DDS/missing).exists(),f"Unused old-style texture still in mod: {missing}"
backgrounds={
    name:tex
    for name,tex in re.findall(
        r'(bp_scene_[A-Za-z0-9_]+)\s*=\s*\{\s*background\s*=\s*\{\s*reference\s*=\s*"gfx/interface/illustrations/event_scene/([^"]+)"',
        ART,re.MULTILINE
    )
}
assert len(backgrounds)>=35,len(backgrounds)
assert all(tex in texture_names for tex in backgrounds.values()),\
    [name for name,tex in backgrounds.items() if tex not in texture_names]
assert backgrounds["bp_scene_gromnica_02"]=="bp_gromnica_01.dds"
assert backgrounds["bp_scene_stado_03"]=="bp_stado_02.dds"
assert backgrounds["bp_scene_kupala_03"]=="bp_kupala_02.dds"
assert backgrounds["bp_scene_perun_03"]=="bp_perun_02.dds"

scene_events={
    "bp_weles.2020":("bp_weles_events.txt","bp_scene_deity_weles_2020"),
    "bp_perun.9110":("bp_perun_events.txt","bp_scene_deity_perun_9110"),
    "bp_spring.3010":("bp_spring_events.txt","bp_scene_deity_mokosh_3010"),
}
for event,(filename,scene) in scene_events.items():
    text=(MOD/"events"/filename).read_text(encoding="utf-8-sig")
    assert text.count(event+" = {")==1,(filename,event)
    block=text.split(event+" = {",1)[1][:300]
    assert "reference = "+scene in block,(event,scene)
for p in (MOD/"events").glob("*.txt"):
    text=p.read_text(encoding="utf-8-sig")
    assert text.count("{")==text.count("}"),p.name
    for scene in re.findall(r'reference\s*=\s*(bp_scene_[A-Za-z0-9_]+)',text):
        assert scene in backgrounds,(p.name,scene)
keys={event+"."+suffix for event in scene_events for suffix in ("t","a","b","c","desc_default")}
keys.update({
 "bp_weles.2020.desc_blood","bp_weles.2020.desc_brave","bp_weles.2020.desc_craven",
 "bp_perun.9110.desc_brave","bp_perun.9110.desc_craven",
 "bp_spring.3010.desc_compassionate","bp_spring.3010.desc_callous",
})
for lang in ("polish","english"):
    loc=(MOD/"localization"/lang/f"bp_l_{lang}.yml").read_text(encoding="utf-8-sig")
    for key in keys:
        assert re.search(r"(?m)^\s*"+re.escape(key)+r":0\s+\".+\"\s*$",loc),f"{lang} missing {key}"
result={
 "version":"0.3.0-dev",
 "dds":len(texture_names),
 "backgrounds":len(backgrounds),
 "personal_deity_scenes":len(scene_events),
 "localization_required_keys":len(keys),
 "static_pass":True,
 "ck3_runtime_tested":False,
}
(ROOT/"validation_gods_030.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
print(json.dumps(result,indent=2))
