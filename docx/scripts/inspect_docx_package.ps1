[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$Path
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

if (-not (Test-Path -LiteralPath $Path)) {
    throw "File not found: $Path"
}

Add-Type -AssemblyName System.IO.Compression.FileSystem

$resolvedPath = (Resolve-Path -LiteralPath $Path).Path
$zip = [System.IO.Compression.ZipFile]::OpenRead($resolvedPath)

try {
    "FILE: $resolvedPath"
    "ENTRIES:"
    $zip.Entries |
        Sort-Object FullName |
        Select-Object FullName, Length |
        Format-Table -AutoSize |
        Out-String -Width 200
}
finally {
    $zip.Dispose()
}
