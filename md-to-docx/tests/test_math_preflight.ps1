$ErrorActionPreference = 'Stop'

$skillRoot = Split-Path $PSScriptRoot -Parent
$buildScript = Join-Path $skillRoot 'scripts\build_md_to_docx.ps1'
$referenceDoc = Join-Path $skillRoot 'assets\default_reference.docx'
$luaFilter = Join-Path $skillRoot 'assets\docx_blank_lines.lua'
$tmp = Join-Path $env:TEMP ('md_to_docx_math_test_' + [guid]::NewGuid().ToString('N'))

try {
  New-Item -ItemType Directory -Force -Path $tmp | Out-Null
  $source = Join-Path $tmp 'formula.md'
  $output = Join-Path $tmp 'formula.docx'
  $log = Join-Path $tmp 'build.log'

  @'
# Formula test

``` math
C(v) = \frac{n - 1}{\sum_{u \neq v}^{}{d(u,v)}}
```

where $`C(v)`$ is closeness centrality.
'@ | Set-Content -LiteralPath $source -Encoding UTF8

  & powershell -ExecutionPolicy Bypass -File $buildScript `
    -WorkspaceRoot $tmp `
    -SourcePath $source `
    -OutputPath $output `
    -ReferenceDocPath $referenceDoc `
    -LuaFilterPath $luaFilter *>&1 | Tee-Object -FilePath $log | Out-Null

  Add-Type -AssemblyName System.IO.Compression.FileSystem
  $archive = [System.IO.Compression.ZipFile]::OpenRead($output)
  try {
    $entry = $archive.GetEntry('word/document.xml')
    $reader = New-Object System.IO.StreamReader($entry.Open())
    try {
      $xml = $reader.ReadToEnd()
    } finally {
      $reader.Dispose()
    }
  } finally {
    $archive.Dispose()
  }

  if ($xml -notmatch '<m:oMathPara') {
    throw 'Fenced math was not exported as a Word display equation.'
  }
  if ($xml -notmatch '<m:oMath') {
    throw 'Inline math was not exported as a Word equation.'
  }
  if ($xml -match '\$`C\(v\)`\$|``` math') {
    throw 'Malformed Markdown math leaked into the Word document.'
  }
  $buildLog = Get-Content -LiteralPath $log -Raw
  if ($buildLog -notmatch '\[preflight/fix\].*math') {
    throw 'Math normalization was not reported by preflight.'
  }

  Write-Output 'PASS: malformed Markdown math normalized to Word OMML.'
} finally {
  if (Test-Path -LiteralPath $tmp) {
    Remove-Item -LiteralPath $tmp -Recurse -Force
  }
}
