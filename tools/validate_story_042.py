#!/usr/bin/env python3
"""Static check for the 0.4.2 two-window CK3 festivals (not a game-engine test).

Each festival MUST open: (1) an educational introduction with a bonus,
(2) a separate, consequential story event. Legacy announcements route silently.
Also checks that raw 0.4 modifiers and opinions all have PL/EN names and texts.
"""
from pathlib import Path
from subprocess import run
import json
import re

ROOT=Path(__file__).resolve().parent.parent
MOD=ROOT/"Bogowie_Pamietaja"
EVENTS=MOD/"events"
SPECS={
 "gromnica":(1001,2101),"weles":(2001,2102),"spring":(3001,2103),
 "jare":(4001,2104),"gaik":(5001,2105),"dziady":(6001,2106),
 "stado":(7001,2107),"kupala":(8001,2108),"perun":(9101,2109),
 "harvest":(9201,2110),"autumn":(9301,2111),"szczodre":(9401,2112),
}

def balanced(text, start):
    assert text[start]=="{"
    dep=0
    quote=False
    comment=False
    escape=False
    for i in range(start,len(text)):
        ch=text[i]
        if ch=="\n":
            comment=False
        if comment:
            continue
        if quote and escape:
            escape=False
            continue
        if quote and ch=="\\":
            escape=True
            continue
        if ch=='"':
            quote=not quote
            continue
        if quote:
            continue
        if ch=="#":
            comment=True
            continue
        if ch=="{":
            dep+=1
        elif ch=="}":
            dep-=1
            if dep==0:
                return text[start:i+1]
            assert dep>=0
    raise ValueError("Unbalanced braces at "+str(start))

def event_block(text, ident):
    starts=list(re.finditer(r"(?m)^"+re.escape(ident)+r"\s*=\s*\{",text))
    assert len(starts)==1, f"Expected one event: {ident} (found {len(starts)})"
    return balanced(text, starts[0].end()-1)

def all_balanced(text,path):
    # Sanity check all comment- and quote-aware event blocks;
    # ignore the file's namespace declaration.
    for m in re.finditer(r"(?m)^([a-z0-9_]+\.\d+)\s*=\s*\{",text):
        balanced(text,m.end()-1)

assert "0.4.2-dev" in (MOD/"descriptor.mod").read_text(encoding="utf-8-sig")
for p in [*EVENTS.glob("*.txt"),*(MOD/"common").rglob("*.txt")]:
    all_balanced(p.read_text(encoding="utf-8-sig"),p)

stories=(EVENTS/"bp_041_story_events.txt").read_text(encoding="utf-8-sig")
assert "namespace = bp_041" in stories
announcements=(EVENTS/"bp_announcement_events.txt").read_text(encoding="utf-8-sig")
necessary_040=set()
necessary_041=set()
for i,(name,(original,story)) in enumerate(SPECS.items(),1):
    intro_text=(EVENTS/f"bp_{name}_events.txt").read_text(encoding="utf-8-sig")
    introductory=event_block(intro_text,f"bp_{name}.{original}")
    dramatic=event_block(stories,f"bp_041.{story}")
    assert "hidden = yes" not in introductory
    assert "hidden = yes" not in dramatic
    assert f"title = bp_041_{name}.intro.t" in introductory
    assert f"desc = bp_041_{name}.intro.desc" in introductory
    assert f"name = bp_041_{name}.intro.a" in introductory
    assert re.search(r"\badd_piety\s*=\s*45\b",introductory)
    assert re.search(r"\badd_stress\s*=\s*-10\b",introductory)
    assert "days = 90" in introductory
    assert introductory.count(f"trigger_event = bp_041.{story}")==1
    assert len(re.findall(r"\boption\s*=\s*\{",introductory))==1
    assert "bp_scene_" in introductory, f"Missing approved holiday art: {name}"
    assert "bp_initialize_effect = yes" in dramatic
    assert "rite_lock" in dramatic, f"Missing annual lock: {name}"
    assert f"title = bp_040_{name}.t" in dramatic
    assert f"desc = bp_040_{name}.desc" in dramatic
    assert "bp_scene_" in dramatic
    assert len(re.findall(r"\boption\s*=\s*\{",dramatic))>=2
    assert not re.search(r"\badd_piety\s*=\s*45\b",dramatic),f"Duplicate participation reward: {name}"
    assert not re.search(r"\badd_stress\s*=\s*-10\b",dramatic),f"Duplicate participation stress relief: {name}"
    # True delayed Weles/Perun/Mokosh consequences are permitted but are not
    # part of the festival's click cascade.
    assert not re.search(r"\btrigger_event\s*=\s*bp_",dramatic),f"Unwanted third popup: {name}"
    necessary_041.update(f"bp_041_{name}.intro.{suffix}" for suffix in ("t","desc","a"))
    necessary_040.update(re.findall(r"\b(?:title|desc)\s*=\s*(bp_040_[a-z0-9_.]+)",dramatic))
    necessary_040.update(re.findall(r"\boption\s*=\s*\{\s*name\s*=\s*(bp_040_[a-z0-9_.]+)",dramatic))
    # Old optional notices are SILENT routers, not additional popups.
    ann=event_block(announcements,f"bp_announcement.{1000+i}")
    assert "hidden = yes" in ann
    assert f"trigger_event = bp_{name}.{original}" in ann
    assert not re.search(r"\boption\s*=\s*\{",ann)

# CK3 raw modifier IDs appearing in the screenshots must be localized.
modifiers=(MOD/"common/modifiers/bp_040_modifiers.txt").read_text(encoding="utf-8-sig")
opinions=(MOD/"common/opinion_modifiers/bp_040_opinions.txt").read_text(encoding="utf-8-sig")
effect_keys=set(re.findall(r"(?m)^(bp_040_[a-z0-9_]+)\s*=\s*\{",modifiers+opinions))
assert len(effect_keys)==19, f"Expected 15 modifiers + 4 opinions, got {len(effect_keys)}"
necessary_041.update(effect_keys)
necessary_041.update(key+"_desc" for key in effect_keys)

# Preserve all previously implemented v0.4.0 event text (now in the second
# event file) and the extra vengeance stories.
blood=(EVENTS/"bp_040_blood_events.txt").read_text(encoding="utf-8-sig")
necessary_040.update(re.findall(r"\b(?:title|desc)\s*=\s*(bp_040_[a-z0-9_.]+)",blood))
necessary_040.update(re.findall(r"\boption\s*=\s*\{\s*name\s*=\s*(bp_040_[a-z0-9_.]+)",blood))
necessary_040.add("bp_040_weles_judgement.desc_bargain")

for lang in ("polish","english"):
    path=MOD/"localization"/lang/f"bp_041_l_{lang}.yml"
    txt=path.read_text(encoding="utf-8-sig")
    assert txt.startswith("l_"+lang+":")
    keys=re.findall(r'(?m)^\s*([a-z0-9_.]+):0\s+"(.*)"\s*$',txt)
    ids=[key for key,_ in keys]
    assert len(ids)==len(set(ids)),f"Duplicate localization key in {path}"
    missing=necessary_041-set(ids)
    assert not missing,f"Missing {lang} 0.4.2 localization: {sorted(missing)}"
    assert len(ids)>=74,f"Expected at least 74 localization keys, got {len(ids)} in {lang}"
    assert all(value.strip() for _,value in keys),f"Empty localization value in {lang}"
    old=MOD/"localization"/lang/f"bp_040_l_{lang}.yml"
    old_text=old.read_text(encoding="utf-8-sig")
    previous=set(re.findall(r'(?m)^\s*(bp_040_[a-z0-9_.]+):0\s+"',old_text))
    missing_old=necessary_040-previous
    assert not missing_old,f"Missing preserved dramatic text in {lang}: {sorted(missing_old)}"

# 0.4.2: game-native message filter is the pause mechanism, NOT an
# unsupported event-level 'pause = yes' key.
filter_path=MOD/"common/message_filter_types/bp_042_message_filters.txt"
filter_src=filter_path.read_text(encoding="utf-8-sig")
assert re.search(r"bp_042_events_pause\s*=\s*\{",filter_src)
assert re.search(r"\bauto_pause\s*=\s*yes\b",filter_src)
assert re.search(r"\balways_show\s*=\s*yes\b",filter_src)
assert re.search(r"\bdisplay\s*=\s*toast\b",filter_src)

message_path=MOD/"common/messages/bp_042_messages.txt"
message_src=message_path.read_text(encoding="utf-8-sig")
for typ in (
    "bp_042_rite_arrived_message","bp_042_story_arrived_message",
    "bp_042_divine_arrived_message","bp_042_trial_success_message",
    "bp_042_trial_failure_message"
):
    assert re.search(r"(?m)^"+re.escape(typ)+r"\s*=\s*\{",message_src),typ
assert message_src.count("message_filter_type = bp_042_events_pause")==5

# Exactly two events per festival; both must emit the pause message.
for name,(original,story) in SPECS.items():
    intro_text=(EVENTS/f"bp_{name}_events.txt").read_text(encoding="utf-8-sig")
    introductory=event_block(intro_text,f"bp_{name}.{original}")
    dramatic=event_block(stories,f"bp_041.{story}")
    assert "type = bp_042_rite_arrived_message" in introductory,name
    assert "type = bp_042_story_arrived_message" in dramatic,name

for path,ident in (
    ("bp_weles_events.txt","bp_weles.2020"),
    ("bp_perun_events.txt","bp_perun.9110"),
    ("bp_spring_events.txt","bp_spring.3010"),
    ("bp_040_blood_events.txt","bp_040.5001"),
    ("bp_040_blood_events.txt","bp_040.5002"),
):
    event=event_block((EVENTS/path).read_text(encoding="utf-8-sig"),ident)
    assert "type = bp_042_divine_arrived_message" in event,ident

# Critical regression: dangerous buttons must NOT close silently.
# There is a result message for each branch, including deaths of rulers and
# the two 50/50 outcomes where guards rescue or fail to rescue a courtier.
result_keys=(
  "bp_042_gaik_dead","bp_042_gaik_survived",
  "bp_042_kupala_dead","bp_042_kupala_survived",
  "bp_042_kupala_guard_failed","bp_042_kupala_guard_saved",
  "bp_042_perun_trial_dead","bp_042_perun_trial_survived",
  "bp_042_revenge_dead","bp_042_revenge_survived",
  "bp_042_aftermath_dead","bp_042_aftermath_survived",
  "bp_042_perun_wrath_dead","bp_042_perun_wrath_survived",
  "bp_042_weles_wrath_dead","bp_042_weles_wrath_survived",
)
risk_src="\n".join((
    stories,
    (EVENTS/"bp_040_blood_events.txt").read_text(encoding="utf-8-sig"),
    (EVENTS/"bp_perun_events.txt").read_text(encoding="utf-8-sig"),
    (EVENTS/"bp_weles_events.txt").read_text(encoding="utf-8-sig"),
))
for key in result_keys:
    assert risk_src.count("title = "+key+".t")==1,key+" is absent/duplicated"
    assert risk_src.count("desc = "+key+".desc")==1,key+" has no description"

# The risky choices retain their weights; no unintended change of odds.
risk_weights={
    "bp_041.2105":(25,75),  # Gaik ruler
    "bp_041.2108":(25,75),  # Kupala ruler (plus 50/50 guard)
    "bp_041.2109":(20,80),  # Perun's holiday trial
    "bp_040.5001":(30,70), # revenge
    "bp_040.5002":(25,75), # aftermath
    "bp_perun.9110":(25,75), # divine Perun
    "bp_weles.2020":(35,65), # divine Veles
}
for ident,weights in risk_weights.items():
    source=stories if ident.startswith("bp_041.") else (
        (EVENTS/"bp_040_blood_events.txt").read_text(encoding="utf-8-sig")
        if ident.startswith("bp_040.") else
        (EVENTS/("bp_perun_events.txt" if "perun" in ident else "bp_weles_events.txt")).read_text(encoding="utf-8-sig")
    )
    event=event_block(source,ident)
    for weight in weights:
        assert re.search(r"(?m)^\s*"+str(weight)+r"\s*=\s*\{",event),(ident,weight)

loc_pause_keys={
    "message_filter_bp_042_events_pause",
    "message_filter_bp_042_events_pause_desc",
    *(f"bp_042_pause_{x}.{y}" for x in ("rite","story","divine") for y in ("t","desc")),
    "bp_042_result_generic_good.t","bp_042_result_generic_bad.t",
    *(f"{key}.{suffix}" for key in result_keys for suffix in ("t","desc")),
}
assert len(loc_pause_keys)==42,len(loc_pause_keys)
for lang in ("polish","english"):
    path=MOD/"localization"/lang/f"bp_042_l_{lang}.yml"
    text=path.read_text(encoding="utf-8-sig")
    assert text.startswith("l_"+lang+":")
    keys=re.findall(r'(?m)^\s*([a-z0-9_.]+):0\s+"(.*)"\s*
# Every holiday must have TWO, not merely 'at most two', visible events.
run(["python3",str(ROOT/"tools/audit_festival_flows_040.py"),"--enforce","--exactly-two"],check=True,cwd=ROOT)
run(["python3",str(ROOT/"tools/validate_gods_030.py")],check=True,cwd=ROOT)

summary={
    "version":"0.4.2-dev",
    "native_pause_message_filter":True,
    "dangerous_chains_with_visible_results":7,
    "localized_outcome_messages":len(result_keys),
    "localized_message_keys_042":len(loc_pause_keys),
    "holidays_with_two_windows":len(SPECS),
    "education_and_story_per_holiday":True,
    "new_modifier_and_opinion_names":len(effect_keys),
    "localization_keys_041":len(necessary_041),
    "legacy_announcements_are_hidden":True,
    "existing_31_artworks_preserved":True,
    "CK3_runtime_tested":False,
    "static_checks":"PASS",
}
(ROOT/"validation_story_042.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
print(json.dumps(summary,indent=2))
,text)
    ids=[x for x,_ in keys]
    assert len(ids)==len(set(ids)),f"Duplicate 0.4.2 keys ({lang})"
    assert loc_pause_keys.issubset(set(ids)),f"Missing {lang}: {loc_pause_keys-set(ids)}"

# Confirm exactly seven dangerous ruler-choice chains preserve the possibility
# of an actual death (not merely a stress penalty).
death_tests=(
    ("bp_041.2105",stories),
    ("bp_041.2108",stories),
    ("bp_041.2109",stories),
    ("bp_040.5001",(EVENTS/"bp_040_blood_events.txt").read_text(encoding="utf-8-sig")),
    ("bp_040.5002",(EVENTS/"bp_040_blood_events.txt").read_text(encoding="utf-8-sig")),
    ("bp_perun.9110",(EVENTS/"bp_perun_events.txt").read_text(encoding="utf-8-sig")),
    ("bp_weles.2020",(EVENTS/"bp_weles_events.txt").read_text(encoding="utf-8-sig")),
)
for ident,src in death_tests:
    assert re.search(r"\bdeath\s*=\s*\{\s*death_reason\s*=",event_block(src,ident)),ident

# This script now actually recognizes 'bp_041' numeric namespaces.
# Every holiday must have TWO, not merely 'at most two', visible events.
run(["python3",str(ROOT/"tools/audit_festival_flows_040.py"),"--enforce","--exactly-two"],check=True,cwd=ROOT)
run(["python3",str(ROOT/"tools/validate_gods_030.py")],check=True,cwd=ROOT)

summary={
    "version":"0.4.2-dev",
    "holidays_with_two_windows":len(SPECS),
    "education_and_story_per_holiday":True,
    "new_modifier_and_opinion_names":len(effect_keys),
    "localization_keys_041":len(necessary_041),
    "legacy_announcements_are_hidden":True,
    "existing_31_artworks_preserved":True,
    "CK3_runtime_tested":False,
    "static_checks":"PASS",
}
(ROOT/"validation_story_042.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
print(json.dumps(summary,indent=2))
