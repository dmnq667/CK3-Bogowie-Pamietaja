# Bogowie Pamietaja 0.2.0 DEV: upgrade an existing mod IN PLACE.
# Safe target detection. No new mod folder or .mod launcher entry is created.
$ErrorActionPreference = 'Stop'
$archive = Join-Path $PSScriptRoot 'Bogowie_Pamietaja_0.2.0_DEV_SAD_I.zip'
$root = 'H:\codex\CK3_Bogowie_Pamietaja'
$possible = @(
    (Join-Path $root 'Bogowie_Pamietaja'),
    (Join-Path $root 'mod\Bogowie_Pamietaja'),
    $root,
    (Join-Path ([Environment]::GetFolderPath('MyDocuments')) 'Paradox Interactive\Crusader Kings III\mod\Bogowie_Pamietaja')
)
$temp = $null
try {
    if (!(Test-Path -LiteralPath $archive -PathType Leaf)) {
        throw "Package archive missing: $archive"
    }
    $destination = $null
    foreach ($candidate in $possible) {
        if ((Test-Path -LiteralPath (Join-Path $candidate 'descriptor.mod') -PathType Leaf)) {
            $destination = $candidate
            break
        }
    }
    if ($null -eq $destination) {
        throw "No existing Bogowie Pamietaja install found. No files copied. Expected H:\codex\CK3_Bogowie_Pamietaja."
    }
    $targetDescriptor = Get-Content -LiteralPath (Join-Path $destination 'descriptor.mod') -Raw
    if ($targetDescriptor -notmatch 'Bogowie pamietaja') {
        throw "The target descriptor belongs to another mod: $destination. Stopping."
    }
    Add-Type -AssemblyName System.IO.Compression.FileSystem
    $zip = [System.IO.Compression.ZipFile]::OpenRead($archive)
    try {
        foreach ($entry in $zip.Entries) {
            $entryPath = $entry.FullName.Replace('\','/')
            if (!$entryPath.StartsWith('Bogowie_Pamietaja/') -or $entryPath.Contains('../') -or $entryPath.Contains(':/')) {
                throw "Archive contains a path outside the mod: $entryPath"
            }
        }
    } finally {
        $zip.Dispose()
    }
    $temp = Join-Path $env:TEMP ("BP020-" + [Guid]::NewGuid().ToString('N'))
    New-Item -ItemType Directory -Path $temp -Force | Out-Null
    Expand-Archive -LiteralPath $archive -DestinationPath $temp -Force
    $source = Join-Path $temp 'Bogowie_Pamietaja'
    $files = @(Get-ChildItem -LiteralPath $source -File -Recurse)
    if ($files.Count -lt 70) { throw "Incomplete package ($($files.Count) files); nothing copied." }
    $descriptor = Get-Content -LiteralPath (Join-Path $source 'descriptor.mod') -Raw
    if ($descriptor -notmatch '0\.2\.0-dev') { throw "Wrong package version; nothing copied." }
    if (!(Test-Path -LiteralPath (Join-Path $source 'gfx\interface\icons\traits\bp_gods_mark_1_v020.dds'))) {
        throw "Missing corrected trait icon; nothing copied."
    }

    Write-Host "Existing target: $destination"
    Write-Host "Mod files: $($files.Count)"
    Write-Host 'Checking and replacing files...'
    $count = 0
    foreach ($file in $files) {
        $relative = $file.FullName.Substring($source.Length).TrimStart('\','/')
        $target = Join-Path $destination $relative
        $parent = Split-Path -Parent $target
        if (!(Test-Path -LiteralPath $parent)) {
            New-Item -ItemType Directory -Path $parent -Force | Out-Null
        }
        Copy-Item -LiteralPath $file.FullName -Destination $target -Force
        $count++
    }
    foreach ($file in $files) {
        $relative = $file.FullName.Substring($source.Length).TrimStart('\','/')
        $target = Join-Path $destination $relative
        if (!(Test-Path -LiteralPath $target -PathType Leaf)) { throw "Missing after copy: $relative" }
        $sourceHash = (Get-FileHash -LiteralPath $file.FullName -Algorithm SHA256).Hash
        $targetHash = (Get-FileHash -LiteralPath $target -Algorithm SHA256).Hash
        if ($sourceHash -ne $targetHash) { throw "Copy mismatch: $relative" }
    }
    Write-Host "COMPLETE. $count files copied and verified by SHA256."
    Write-Host 'Your original CK3 launcher mod entry is unchanged. Version: 0.2.0 DEV (compact narrative).'
    exit 0
} catch {
    Write-Error $_.Exception.Message
    exit 1
} finally {
    if ($null -ne $temp -and (Test-Path -LiteralPath $temp)) {
        Remove-Item -LiteralPath $temp -Recurse -Force -ErrorAction SilentlyContinue
    }
}
