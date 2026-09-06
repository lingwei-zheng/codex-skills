[CmdletBinding()]
param()

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.IO.Compression.FileSystem

# Self-contained package fixture: no Word COM, network, or user documents.
$fixturePath = Join-Path ([System.IO.Path]::GetTempPath()) ('docx-tools-' + [guid]::NewGuid().ToString('N') + '.docx')
$fixtureHash = $null
try {
    $entries = @{
        '[Content_Types].xml' = '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/></Types>'
        '_rels/.rels' = '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/></Relationships>'
        'word/document.xml' = '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body><w:p><w:r><w:t>Fallback route fixture</w:t></w:r></w:p><w:p><w:r><w:t>Preserved &amp; readable</w:t></w:r></w:p><w:sectPr/></w:body></w:document>'
    }
    $archive = [System.IO.Compression.ZipFile]::Open($fixturePath, [System.IO.Compression.ZipArchiveMode]::Create)
    try {
        foreach ($name in $entries.Keys) {
            $entry = $archive.CreateEntry($name)
            $writer = [System.IO.StreamWriter]::new($entry.Open(), [System.Text.UTF8Encoding]::new($false))
            try { $writer.Write($entries[$name]) } finally { $writer.Dispose() }
        }
    } finally { $archive.Dispose() }

    $fixtureHash = (Get-FileHash -LiteralPath $fixturePath).Hash
    $textOutput = (& (Join-Path $PSScriptRoot 'extract_docx_text.ps1') -Path $fixturePath) -join "`n"
    foreach ($expected in @('PARAGRAPHS: 2', 'Fallback route fixture', 'Preserved & readable', 'TRACKED_INSERTIONS: 0', 'TRACKED_DELETIONS: 0')) {
        if (-not $textOutput.Contains($expected)) { throw "Extraction missing expected value: $expected" }
    }
    $packageOutput = (& (Join-Path $PSScriptRoot 'inspect_docx_package.ps1') -Path $fixturePath) -join "`n"
    foreach ($expected in @('[Content_Types].xml', '_rels/.rels', 'word/document.xml')) {
        if (-not $packageOutput.Contains($expected)) { throw "Inspection missing package entry: $expected" }
    }
    if ((Get-FileHash -LiteralPath $fixturePath).Hash -ne $fixtureHash) { throw 'Read-only tools modified the fixture.' }

    $missingRejected = $false
    try { & (Join-Path $PSScriptRoot 'extract_docx_text.ps1') -Path ($fixturePath + '.missing') | Out-Null }
    catch { $missingRejected = $_.Exception.Message -like 'File not found:*' }
    if (-not $missingRejected) { throw 'Missing input was not rejected clearly.' }
    Write-Output 'DOCX tools validation passed: content, package entries, read-only preservation, missing-input error.'
} finally {
    # Delete only this invocation's explicitly named fixture, never a directory.
    if (Test-Path -LiteralPath $fixturePath) { Remove-Item -LiteralPath $fixturePath }
}
