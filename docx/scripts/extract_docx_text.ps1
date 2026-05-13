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
    $documentEntry = $zip.GetEntry('word/document.xml')
    if ($null -eq $documentEntry) {
        throw "word/document.xml not found in $resolvedPath"
    }

    $commentsEntry = $zip.GetEntry('word/comments.xml')

    $reader = [System.IO.StreamReader]::new($documentEntry.Open())
    try {
        $xmlText = $reader.ReadToEnd()
    }
    finally {
        $reader.Close()
    }

    $xml = [xml]$xmlText
    $ns = [System.Xml.XmlNamespaceManager]::new($xml.NameTable)
    $ns.AddNamespace('w', 'http://schemas.openxmlformats.org/wordprocessingml/2006/main')

    $paragraphs = @()
    foreach ($p in $xml.SelectNodes('//w:body/w:p', $ns)) {
        $parts = @()
        foreach ($node in $p.SelectNodes('.//w:t', $ns)) {
            if ($node.InnerText) {
                $parts += $node.InnerText
            }
        }

        $joined = ($parts -join '').Trim()
        if ($joined.Length -gt 0) {
            $paragraphs += $joined
        }
    }

    $insCount = $xml.SelectNodes('//w:ins', $ns).Count
    $delCount = $xml.SelectNodes('//w:del', $ns).Count
    $commentRangeCount = $xml.SelectNodes('//w:commentRangeStart', $ns).Count

    "FILE: $resolvedPath"
    "PARAGRAPHS: $($paragraphs.Count)"
    "TRACKED_INSERTIONS: $insCount"
    "TRACKED_DELETIONS: $delCount"
    "COMMENT_RANGES: $commentRangeCount"
    "COMMENTS_XML_PRESENT: $([bool]($null -ne $commentsEntry))"
    ""
    "TEXT:"
    foreach ($paragraph in $paragraphs) {
        $paragraph
    }
}
finally {
    $zip.Dispose()
}
