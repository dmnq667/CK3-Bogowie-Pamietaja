#!/usr/bin/env python3
"""Build a self-verifying Windows in-place updater for the CK3 0.2.0 DEV mod.

Runs inside GitHub Actions. Never touches the user's machine.
"""
from hashlib import sha256
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parent.parent
MOD = ROOT / "Bogowie_Pamietaja"
OUT = ROOT / "Bogowie_Pamietaja_0.2.0_DEV_AKTUALIZACJA.zip"
files = sorted(p for p in MOD.rglob("*") if p.is_file() and p.name != ".gitkeep")
assert MOD.is_dir() and (MOD / "descriptor.mod").is_file()
assert len(files) >= 70, "Unexpectedly small mod build"

manifest = "\n".join(
    f"{sha256(p.read_bytes()).hexdigest().upper()}\t{p.relative_to(MOD).as_posix()}"
    for p in files
) + "\n"

powershell = r'''
$ErrorActionPreference = 'Stop'
$Source = Join-Path $PSScriptRoot 'Bogowie_Pamietaja'
$Base = 'H:\codex\CK3_Bogowie_Pamietaja'

if (-not (Test-Path -LiteralPath $Source -PathType Container)) {
    throw 'Missing source folder. Extract the whole ZIP first.'
}

$Nested = Join-Path $Base 'Bogowie_Pamietaja'
if (Test-Path -LiteralPath (Join-Path $Nested 'descriptor.mod') -PathType Leaf) {
    $Target = $Nested
} elseif (Test-Path -LiteralPath (Join-Path $Base 'descriptor.mod') -PathType Leaf) {
    $Target = $Base
} else {
    Write-Host "No mod found at default path: $Base"
    $Custom = Read-Host 'Enter full path to the existing mod folder (with descriptor.mod)'
    if (-not (Test-Path -LiteralPath (Join-Path $Custom 'descriptor.mod') -PathType Leaf)) {
        throw 'No descriptor.mod at selected target. Nothing was copied.'
    }
    $Target = $Custom
}

$Entries = @(Get-Content -LiteralPath (Join-Path $PSScriptRoot 'MANIFEST_SHA256.tsv') -Encoding UTF8 |
    Where-Object { $_.Trim().Length -gt 0 } | ForEach-Object {
        $parts = $_.Split([char[]]@([char]9), 2)
        if ($parts.Length -ne 2) { throw 'Invalid manifest row.' }
        [PSCustomObject]@{ Hash=$parts[0]; Relative=$parts[1] }
    })
if ($Entries.Count -lt 70) { throw 'Manifest is incomplete.' }

foreach ($entry in $Entries) {
    $relative = $entry.Relative.Replace('/', '\')
    $src = Join-Path $Source $relative
    if (-not (Test-Path -LiteralPath $src -PathType Leaf)) {
        throw "Missing source: $($entry.Relative)"
    }
    if ((Get-FileHash -LiteralPath $src -Algorithm SHA256).Hash -ne $entry.Hash) {
        throw "Corrupt payload: $($entry.Relative)"
    }
}
Write-Host "Existing mod: $Target"
Write-Host "Source files verified: $($Entries.Count)"
Write-Host 'Overwriting the existing mod (no duplicate launcher entry).'

foreach ($entry in $Entries) {
    $relative = $entry.Relative.Replace('/', '\')
    $src = Join-Path $Source $relative
    $dst = Join-Path $Target $relative
    $dstDir = Split-Path -Parent $dst
    if (-not (Test-Path -LiteralPath $dstDir -PathType Container)) {
        New-Item -ItemType Directory -Force -Path $dstDir | Out-Null
    }
    Copy-Item -LiteralPath $src -Destination $dst -Force
}
foreach ($entry in $Entries) {
    $dst = Join-Path $Target ($entry.Relative.Replace('/', '\'))
    if ((Get-FileHash -LiteralPath $dst -Algorithm SHA256).Hash -ne $entry.Hash) {
        throw "Verification failed after copy: $($entry.Relative)"
    }
}
Write-Host ""
Write-Host "GOTOWE. Verified installed files: $($Entries.Count)"
Write-Host 'Continue with the existing launcher entry; no second mod was created.'
'''

batch = r'''@echo off
setlocal
cd /d "%~dp0"
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0AKTUALIZUJ_020.ps1"
set "EXITCODE=%ERRORLEVEL%"
echo.
if %EXITCODE% GEQ 1 (
    echo AKTUALIZACJA NIEUDANA. Sprawdz komunikat powyzej.
) else (
    echo GOTOWE. Nadpisano pliki istniejacego moda.
)
pause
exit /b %EXITCODE%
'''

readme = """BOGOWIE PAMIETAJA 0.2.0 DEV (wersja testowa)

1. Zamknij CK3 i launcher Paradoxu.
2. Rozpakuj CALY ZIP do dowolnego katalogu.
3. Uruchom AKTUALIZUJ_020.bat.
4. Instalator sprawdzi pliki i nadpisze ISTNIEJACY mod na dysku H:.
5. Nie tworzy drugiego wpisu w launcherze.
6. Pierwszy test wykonaj na kopii zapisu albo nowej kampanii.

Zrodla v0.1.9-alpha sa nadal na GitHubie.
"""

with ZipFile(OUT, "w", compression=ZIP_DEFLATED, compresslevel=6) as z:
    for file in files:
        z.write(file, (Path("Bogowie_Pamietaja") / file.relative_to(MOD)).as_posix())
    z.writestr("MANIFEST_SHA256.tsv", manifest.encode("utf-8"))
    z.writestr("AKTUALIZUJ_020.ps1", powershell.lstrip().encode("utf-8-sig"))
    z.writestr("AKTUALIZUJ_020.bat", batch.encode("ascii"))
    z.writestr("CZYTAJ_TO.txt", readme.encode("utf-8-sig"))

with ZipFile(OUT) as z:
    assert len(z.namelist()) == len(files) + 4
    assert z.testzip() is None
    for row in manifest.splitlines():
        expected, relative = row.split("\t", 1)
        assert sha256(z.read("Bogowie_Pamietaja/" + relative)).hexdigest().upper() == expected
print(f"Packed and verified {len(files)} files to {OUT.name} ({OUT.stat().st_size} bytes)")
