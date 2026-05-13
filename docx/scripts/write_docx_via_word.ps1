[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$InputTextPath,

    [Parameter(Mandatory = $true)]
    [string]$OutputPath
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

if (-not (Test-Path -LiteralPath $InputTextPath)) {
    throw "Input text file not found: $InputTextPath"
}

$resolvedInput = (Resolve-Path -LiteralPath $InputTextPath).Path
$resolvedOutput = [System.IO.Path]::GetFullPath($OutputPath)
$outputDir = Split-Path -Parent $resolvedOutput

if (-not (Test-Path -LiteralPath $outputDir)) {
    New-Item -ItemType Directory -Path $outputDir | Out-Null
}

$text = Get-Content -Raw -LiteralPath $resolvedInput
$paragraphs = $text -split "(`r`n|`n|`r){2,}"

$word = $null
$doc = $null

try {
    $word = New-Object -ComObject Word.Application
    $word.Visible = $false
    $doc = $word.Documents.Add()

    foreach ($paragraph in $paragraphs) {
        $trimmed = $paragraph.Trim()
        if ($trimmed.Length -eq 0) {
            continue
        }

        $range = $doc.Range($doc.Content.End - 1, $doc.Content.End - 1)
        $range.InsertAfter($trimmed)
        $range.InsertParagraphAfter() | Out-Null
        $range.InsertParagraphAfter() | Out-Null
    }

    $wdFormatDocumentDefault = 16
    $doc.SaveAs([ref]$resolvedOutput, [ref]$wdFormatDocumentDefault)
    "WROTE: $resolvedOutput"
}
finally {
    if ($null -ne $doc) {
        $doc.Close([ref]0) | Out-Null
        [void][System.Runtime.InteropServices.Marshal]::ReleaseComObject($doc)
    }
    if ($null -ne $word) {
        $word.Quit()
        [void][System.Runtime.InteropServices.Marshal]::ReleaseComObject($word)
    }
    [GC]::Collect()
    [GC]::WaitForPendingFinalizers()
}
