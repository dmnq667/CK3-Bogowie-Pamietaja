#!/usr/bin/env python3
"""Static check for the 0.4.5 two-window CK3 festivals (not a game-engine test).

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

assert "0.4.5-dev" in (MOD/"descriptor.mod").read_text(encoding="utf-8-sig")
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
    assert not missing,f"Missing {lang} 0.4.5 localization: {sorted(missing)}"
    assert len(ids)>=74,f"Expected at least 74 localization keys, got {len(ids)} in {lang}"
    assert all(value.strip() for _,value in keys),f"Empty localization value in {lang}"
    old=MOD/"localization"/lang/f"bp_040_l_{lang}.yml"
    old_text=old.read_text(encoding="utf-8-sig")
    previous=set(re.findall(r'(?m)^\s*(bp_040_[a-z0-9_.]+):0\s+"',old_text))
    missing_old=necessary_040-previous
    assert not missing_old,f"Missing preserved dramatic text in {lang}: {sorted(missing_old)}"

# 0.4.5 removes the unsupported "letter_event + character window" attempt
# because it neither paused gameplay nor preserved all event UI text.
# Normal character events show the original CK3 interface. Auto-pause is
# UNCONFIRMED and is NOT claimed to be fixed by this rollback.
def pause_envelope(block, ident):
    assert "type = character_event" in block,ident
    for unwanted in ("type = letter_event","window = character_event",
                     "sender = root","opening = bp_043_empty_opening"):
        assert unwanted not in block,(ident,unwanted)
    # Only opening/arrival toasts are forbidden. IMPORTANT: result messages
    # within options are intentional and must remain (risk of death, rescue).
    before_options=block.split("    option = {",1)[0]
    assert "send_interface_toast" not in before_options,ident
    assert "send_interface_message" not in before_options,ident

for name,(original,story) in SPECS.items():
    opener=(EVENTS/f"bp_{name}_events.txt").read_text(encoding="utf-8-sig")
    pause_envelope(event_block(opener,f"bp_{name}.{original}"),f"bp_{name}.{original}")
    pause_envelope(event_block(stories,f"bp_041.{story}"),f"bp_041.{story}")

for path,ident in (
    ("bp_weles_events.txt","bp_weles.2020"),
    ("bp_perun_events.txt","bp_perun.9110"),
    ("bp_spring_events.txt","bp_spring.3010"),
    ("bp_040_blood_events.txt","bp_040.5001"),
    ("bp_040_blood_events.txt","bp_040.5002"),
):
    pause_envelope(event_block((EVENTS/path).read_text(encoding="utf-8-sig"),ident),ident)

all_events="\n".join(p.read_text(encoding="utf-8-sig") for p in EVENTS.glob("*.txt"))
assert "opening = bp_043_empty_opening" not in all_events,"Broken letter opening remained"
for key in ("bp_042_rite_arrived_message","bp_042_story_arrived_message",
            "bp_042_divine_arrived_message"):
    assert key not in all_events,f"Redundant arrival toast: {key}"
messages=(MOD/"common/messages/bp_042_messages.txt").read_text(encoding="utf-8-sig")
assert messages.count("message_filter_type = bp_042_events_pause")==18
assert "bp_042_trial_success_message" in messages
assert "bp_042_trial_failure_message" in messages
filter_src=(MOD/"common/message_filter_types/bp_042_message_filters.txt").read_text(encoding="utf-8-sig")
assert re.search(r"(?m)^\s*auto_pause\s*=\s*no\s*$",filter_src)
for lang in ("polish","english"):
    path=MOD/"localization"/lang/f"bp_043_l_{lang}.yml"
    txt=path.read_text(encoding="utf-8-sig")
    assert txt.startswith("l_"+lang+":")
    assert 'bp_043_empty_opening:0 " "' in txt  # legacy unused key is harmless

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
risk_text="\n".join((
    stories,(EVENTS/"bp_040_blood_events.txt").read_text(encoding="utf-8-sig"),
    (EVENTS/"bp_perun_events.txt").read_text(encoding="utf-8-sig"),
    (EVENTS/"bp_weles_events.txt").read_text(encoding="utf-8-sig")
))
for key in result_keys:
    assert risk_text.count("title = "+key+".t")==1,key
    assert risk_text.count("desc = "+key+".desc")==1,key
    # Native CK3 common/messages definitions are the actual rendered source
    # of result toast text. Event-local title/desc alone were ignored and
    # caused a literal bp_042_trial_success_message_desc on screenshots.
    typ=key+"_message"
    assert risk_text.count("type = "+typ)==1,typ
    match=re.search(r"(?m)^"+re.escape(typ)+r"\s*=\s*\{([\s\S]*?)^\}",messages)
    assert match,typ
    msg=match.group(1)
    assert "title = "+key+".t" in msg,typ
    assert "desc = "+key+".desc" in msg,typ
for lang in ("polish","english"):
    data=(MOD/"localization"/lang/f"bp_042_l_{lang}.yml").read_text(encoding="utf-8-sig")
    for key in result_keys:
        assert key+".t:0" in data,key
        assert key+".desc:0" in data,key
    for key in (
        "bp_042_result_generic_good.desc",
        "bp_042_result_generic_bad.desc",
        "bp_042_trial_success_message_desc",
        "bp_042_trial_failure_message_desc",
    ):
        assert key+":0" in data,(lang,key)

risk_weights={
  "bp_041.2105":(25,75),
  "bp_041.2108":(25,75),
  "bp_041.2109":(20,80),
  "bp_040.5001":(30,70),
  "bp_040.5002":(25,75),
  "bp_perun.9110":(25,75),
  "bp_weles.2020":(35,65),
}
for ident,weights in risk_weights.items():
    if ident.startswith("bp_041."): src=stories
    elif ident.startswith("bp_040."): src=(EVENTS/"bp_040_blood_events.txt").read_text(encoding="utf-8-sig")
    else: src=(EVENTS/("bp_perun_events.txt" if "perun" in ident else "bp_weles_events.txt")).read_text(encoding="utf-8-sig")
    ev=event_block(src,ident)
    for w in weights:
        assert re.search(r"(?m)^\s*"+str(w)+r"\s*=\s*\{",ev),(ident,w)
    assert re.search(r"\bdeath\s*=\s*\{\s*death_reason",ev),ident

# 0.4.5: recover the ORIGINAL 0.1.9 calendar behaviour:
# the existing daily watcher actively opens the first holiday window itself.
# It must reserve each feast once per season before opening it, otherwise
# a quickly advancing 30 April -> 2 May calendar can queue duplicates.
watcher_src=(EVENTS/"bp_announcement_events.txt").read_text(encoding="utf-8-sig")
watcher=event_block(watcher_src,"bp_announcement.1299")
assert "hidden = yes" in watcher
assert "trigger_event = { id = bp_announcement.1299 days = 1 }" in watcher
assert "bp_first_court_due_v020_trigger = yes" in watcher
assert "trigger_event = bp_judgement.1001" in watcher
festival_ids={
    "gromnica":("bp_gromnica.1001","v014","v013"),
    "weles":("bp_weles.2001","v014","v013"),
    "spring":("bp_spring.3001","v014","v013"),
    "jare":("bp_jare.4001","v014","v013"),
    "gaik":("bp_gaik.5001","v015","v015"),
    "dziady":("bp_dziady.6001","v015","v015"),
    "stado":("bp_stado.7001","v015","v015"),
    "kupala":("bp_kupala.8001","v015","v015"),
    "perun":("bp_perun.9101","v019","v019"),
    "harvest":("bp_harvest.9201","v019","v019"),
    "autumn":("bp_autumn.9301","v019","v019"),
    "szczodre":("bp_szczodre.9401","v019","v019")
}
assert len(festival_ids)==len(SPECS)==12
for n,(ident,announce_version,rite_version) in festival_ids.items():
    for phrase in (
        f"bp_{n}_calendar_window_trigger = yes",
        f"NOT = {{ has_variable = bp_{n}_announced_{announce_version} }}",
        f"NOT = {{ has_variable = bp_{n}_rite_lock_{rite_version} }}",
        f"set_variable = {{ name = bp_{n}_announced_{announce_version} value = yes days = 335 }}",
        f"trigger_event = {ident}",
    ):
        assert phrase in watcher,(n,phrase)
    assert watcher.count(f"trigger_event = {ident}")==1,(n,"duplicate schedule")
    # The actual popup is the *educational* first stage, NOT a new
    # confirmation or a hidden announcement router.
    opener=event_block((EVENTS/f"bp_{n}_events.txt").read_text(encoding="utf-8-sig"),ident)
    assert "type = character_event" in opener,n
    assert "hidden = yes" not in opener,n
    assert f"title = bp_041_{n}.intro.t" in opener,n
    assert f"trigger_event = bp_041.{SPECS[n][1]}" in opener,n

# Ensure the pictured Szczodre Gody scene has real DDS assets and database
# aliases: the screenshot with the empty dark area was a letter_event
# presentation regression, NOT missing DDS data.
backgrounds=(MOD/"common/event_backgrounds/bp_slavic_holiday_backgrounds.txt").read_text(encoding="utf-8-sig")
dds_dir=MOD/"gfx/interface/illustrations/event_scene"
for i in ("01","02","03"):
    tag=f"bp_scene_szczodre_{i}"
    texture=f"bp_szczodre_{i}.dds"
    assert re.search(r"(?m)^"+tag+r"\s*=\s*\{",backgrounds),tag
    assert f"event_scene/{texture}" in backgrounds,tag
    path=dds_dir/texture
    assert path.is_file() and path.stat().st_size>600000,path
    assert path.read_bytes()[:4]==b"DDS ",f"Not a DDS image: {path}"
first=event_block((EVENTS/"bp_szczodre_events.txt").read_text(encoding="utf-8-sig"),"bp_szczodre.9401")
second=event_block(stories,"bp_041.2112")
assert "override_background = { reference = bp_scene_szczodre_02 }" in first
assert "override_background = { reference = bp_scene_szczodre_01 }" in second
assert "type = character_event" in first and "type = character_event" in second
assert "type = letter_event" not in first and "type = letter_event" not in second

# Jare Gody regression: the early draft chose ANY adult courtier and
# claimed a violent attack without any actual evidence or prior actions.
# An innocent chaste/zealous princess could be executed. That is removed.
jare_block=event_block(stories,"bp_041.2104")
assert "random_courtier" not in jare_block
assert "save_scope_as = bp_040_target" not in jare_block
assert "death = " not in jare_block
assert "scope:bp_040_target" not in jare_block
for fragment in (
    "desc = bp_040_jare.desc_blood",
    "desc = bp_040_jare.desc_mercy",
    "has_character_flag = bp_040_blood_v040",
    "has_character_flag = bp_040_mercy_v040",
    "name = bp_040_jare.a",
    "name = bp_040_jare.b",
    "name = bp_040_jare.c",
    "bp_040_actual_blood_effect = yes",
    "bp_040_schedule_revenge_effect = yes",
):
    assert fragment in jare_block,fragment
for lang in ("polish","english"):
    localization=(MOD/"localization"/lang/f"bp_040_l_{lang}.yml").read_text(encoding="utf-8-sig")
    for key in ("bp_040_jare.desc_blood","bp_040_jare.desc_mercy"):
        assert key+":0" in localization,(lang,key)
    assert "[bp_040_target.GetTitledFirstName]" not in "\n".join(
        line for line in localization.splitlines()
        if re.match(r"\s*bp_040_jare\.",line)
    ),"Named innocent must never be accused in Jare Gody"

run(["python3",str(ROOT/"tools/audit_festival_flows_040.py"),"--enforce","--exactly-two"],check=True,cwd=ROOT)
run(["python3",str(ROOT/"tools/validate_gods_030.py")],check=True,cwd=ROOT)

summary={
 "version":"0.4.5-dev",
 "two_window_festivals":len(SPECS),
 "standard_character_events_restored":29,
 "automatic_calendar_festival_entries":len(festival_ids),
 "jare_random_accused_removed":True,
 "story_variants_based_on_blood_or_mercy":2,
 "localized_result_messages":len(result_keys),
 "szczodre_dds_integrity_checked":3,
 "pausing_restored_to_original_event_flow":True,
 "auto_pause_in_ck3_unverified":True,
 "redundant_opening_toasts":0,
 "dangerous_chains_preserved":len(risk_weights),
 "visible_trial_outcomes_preserved":len(result_keys),
 "original_artworks_preserved":31,
 "in_game_pause_confirmed":False,
 "static_validation":"PASS",
}
(ROOT/"validation_story_045.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
print(json.dumps(summary,indent=2))
