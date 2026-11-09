#!/usr/bin/env python3
"""Build a self-verifying Windows in-place updater for CK3 Gniew i Laska Bogow 0.4.6."""
from pathlib import Path
from hashlib import sha256
from zipfile import ZipFile, ZIP_DEFLATED
import re

ROOT=Path(__file__).resolve().parent.parent
MOD=ROOT/"Bogowie_Pamietaja"
OUT=ROOT/"GNIEW_I_LASKA_BOGOW_0.4.6_DEV_NADPISZ.zip"
DDS=MOD/"gfx/interface/illustrations/event_scene"
assert (MOD/"descriptor.mod").is_file()
EXPECTED_VERSION = "0.4.6-dev"
assert EXPECTED_VERSION in (MOD/"descriptor.mod").read_text(encoding="utf-8-sig")
files=sorted(p for p in MOD.rglob("*") if p.is_file() and p.name != ".gitkeep")
assert len(files)>=65,f"Incomplete mod: {len(files)} files"
for name in ["bp_deity_weles_2020.dds","bp_deity_perun_9110.dds","bp_deity_mokosh_3010.dds",
             "bp_gromnica_01.dds","bp_stado_02.dds","bp_kupala_02.dds","bp_perun_02.dds"]:
    assert (DDS/name).is_file(),f"Missing new-style texture: {name}"
manifest="".join(
    f"{sha256(p.read_bytes()).hexdigest().upper()}\t{p.relative_to(MOD).as_posix()}\n"
    for p in files
)
powershell=r'''
param([string]$TargetOverride = '')
$ErrorActionPreference = 'Stop'
$Source = Join-Path $PSScriptRoot 'Bogowie_Pamietaja'
$ManifestPath = Join-Path $PSScriptRoot 'MANIFEST_SHA256.tsv'
$Base = 'H:\codex\CK3_Bogowie_Pamietaja'
try {
    if (Get-Process -Name 'ck3' -ErrorAction SilentlyContinue) {
        throw 'Zamknij CK3 przed aktualizacja. Nie nadpisujemy plikow podczas gry.'
    }
    if (-not (Test-Path -LiteralPath (Join-Path $Source 'descriptor.mod') -PathType Leaf)) {
        throw 'Niekompletna paczka. Wypakuj CALY ZIP przed uruchomieniem.'
    }
    $candidates = @(
        ($Base + '\Bogowie_Pamietaja'),
        ($Base + '\mod\Bogowie_Pamietaja'),
        $Base,
        (Join-Path ([Environment]::GetFolderPath('MyDocuments')) 'Paradox Interactive\Crusader Kings III\mod\Bogowie_Pamietaja')
    )
    $Target = $null
    if (-not [string]::IsNullOrWhiteSpace($TargetOverride)) {
        $Target = $TargetOverride
    } else {
        foreach ($candidate in $candidates) {
            if (Test-Path -LiteralPath (Join-Path $candidate 'descriptor.mod') -PathType Leaf) {
                $Target = $candidate
                break
            }
        }
        if ($null -eq $Target) {
            $Target = Read-Host 'Podaj sciezke ISTNIEJACEGO katalogu moda (z descriptor.mod)'
        }
    }
    if (-not (Test-Path -LiteralPath (Join-Path $Target 'descriptor.mod') -PathType Leaf)) {
        throw 'Brak istniejacej instalacji. Nie tworzono drugiego moda.'
    }
    $current = Get-Content -LiteralPath (Join-Path $Target 'descriptor.mod') -Raw
    if ($current -notmatch 'Bogowie|Gniew|Gods Remember') {
        throw "Nieprawidlowy mod docelowy: $Target"
    }
    $newdesc = Get-Content -LiteralPath (Join-Path $Source 'descriptor.mod') -Raw
    if ($newdesc -notmatch 'version\s*=\s*"__EXPECTED_VERSION_REGEX__"') {
        throw 'Zla wersja paczki. Odmowa instalacji.'
    }
    $entries = @(Get-Content -LiteralPath $ManifestPath -Encoding UTF8 | Where-Object {$_.Trim() -ne ''} | ForEach-Object {
        $cols = $_.Split([char[]]@([char]9), 2)
        if ($cols.Count -ne 2) { throw 'Uszkodzony manifest.' }
        [PSCustomObject]@{Hash=$cols[0]; Relative=$cols[1]}
    })
    if ($entries.Count -lt 65) { throw 'Niekompletna paczka.' }
    foreach ($e in $entries) {
        if ($e.Relative.Contains('..') -or $e.Relative.Contains(':') -or $e.Relative.StartsWith('/')) {
            throw "Niebezpieczna sciezka: $($e.Relative)"
        }
        $src = Join-Path $Source ($e.Relative.Replace('/', '\'))
        if (-not (Test-Path -LiteralPath $src -PathType Leaf)) { throw "Brak pliku: $($e.Relative)" }
        if ((Get-FileHash -LiteralPath $src -Algorithm SHA256).Hash -ne $e.Hash) {
            throw "Zla suma SHA256: $($e.Relative)"
        }
    }
    $backup = $Target.TrimEnd('\') + '_KOPIA_PRZED_046_' + (Get-Date -Format 'yyyyMMdd_HHmmss')
    Write-Host "Istniejacy mod: $Target"
    Write-Host "Tworzenie kopii: $backup"
    Copy-Item -LiteralPath $Target -Destination $backup -Recurse -Force
    foreach ($e in $entries) {
        $rel = $e.Relative.Replace('/', '\')
        $src = Join-Path $Source $rel
        $dst = Join-Path $Target $rel
        $parent = Split-Path -Parent $dst
        if (-not (Test-Path -LiteralPath $parent)) {
            New-Item -ItemType Directory -Path $parent -Force | Out-Null
        }
        Copy-Item -LiteralPath $src -Destination $dst -Force
    }
    foreach ($name in @('bp_gromnica_02.dds','bp_stado_03.dds','bp_kupala_03.dds','bp_perun_03.dds')) {
        $old = Join-Path $Target ('gfx\interface\illustrations\event_scene\' + $name)
        if (Test-Path -LiteralPath $old -PathType Leaf) { Remove-Item -LiteralPath $old -Force }
    }
    foreach ($e in $entries) {
        $dst = Join-Path $Target ($e.Relative.Replace('/', '\'))
        if ((Get-FileHash -LiteralPath $dst -Algorithm SHA256).Hash -ne $e.Hash) {
            throw "Weryfikacja nieudana: $($e.Relative). Kopia istnieje: $backup"
        }
    }
    Write-Host ''
    Write-Host 'GOTOWE. Zaktualizowano dotychczasowy mod 0.4.6 DEV.'
    Write-Host "Kopia poprzedniej wersji: $backup"
    Write-Host 'Najpierw testuj na kopii zapisu CK3.'
} catch {
    Write-Error $_.Exception.Message
    exit 1
}
'''.lstrip()
# The version guard must derive from the descriptor version, not the previous
# release. Regression protection for the rejected 0.4.6 installer.
powershell = powershell.replace('__EXPECTED_VERSION_REGEX__', re.escape(EXPECTED_VERSION))
assert ('version\\s*=\\s*"' + re.escape(EXPECTED_VERSION) + '"') in powershell
assert '0\\.3\\.0-dev' not in powershell
bat=r'''@echo off
setlocal
chcp 65001 >nul
cd /d "%~dp0"
echo.
echo GNIEW I LASKA BOGOW - DEV 0.4.6
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0AKTUALIZUJ_046.ps1"
set "RC=%ERRORLEVEL%"
if not "%RC%"=="0" echo Wystapil blad instalacji.
echo.
pause
exit /b %RC%
'''
readme='''GNIEW I LASKA BOGOW - CK3 0.4.6 DEV

1. WYLACZ CK3.
2. Rozpakuj CALY plik ZIP w jednym folderze.
3. Uruchom AKTUALIZUJ_046.bat.
4. Instalator odnajduje dotychczasowy mod, sprawdza SHA256, zapisuje kopie i nadpisuje pliki.
5. NIE tworzy drugiego moda w launcherze.
6. Testuj na kopii zapisu. Automatyczne testy kodu nie zastepuja testu wewnatrz CK3.
7. Przy problemach sprawdz logs/error.log i przywroc poprzednia kopie.

0.4.6 DEV: przywrocony oryginalny automatyczny kalendarz 12 swiat; dwa normalne okna, 31 grafik, bez dodatkowych banerow. Pauza wymaga weryfikacji w grze.
'''
with ZipFile(OUT,"w",compression=ZIP_DEFLATED,compresslevel=6) as z:
    for p in files:
        z.write(p,(Path("Bogowie_Pamietaja")/p.relative_to(MOD)).as_posix())
    z.writestr("MANIFEST_SHA256.tsv",manifest.encode("utf-8"))
    z.writestr("AKTUALIZUJ_046.ps1",powershell.encode("utf-8-sig"))
    z.writestr("AKTUALIZUJ_046.bat",bat.encode("ascii"))
    z.writestr("CZYTAJ_TO.txt",readme.encode("utf-8-sig"))
with ZipFile(OUT) as z:
    assert z.testzip() is None
    for row in manifest.splitlines():
        expected,relative=row.split("\t",1)
        assert sha256(z.read("Bogowie_Pamietaja/"+relative)).hexdigest().upper()==expected
print(f"OK {OUT.name}, files={len(files)}, bytes={OUT.stat().st_size}")
