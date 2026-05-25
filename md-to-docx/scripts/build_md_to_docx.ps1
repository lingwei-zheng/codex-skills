param(
  [string]$WorkspaceRoot,
  [string]$SourcePath,
  [string]$OutputPath,
  [string]$ReferenceDocPath,
  [string]$BibliographyPath,
  [string]$LuaFilterPath
)

$ErrorActionPreference = 'Stop'

$skillRoot = Split-Path $PSScriptRoot -Parent
$bundledReference = Join-Path $skillRoot 'assets\default_reference.docx'
$bundledFilter = Join-Path $skillRoot 'assets\docx_blank_lines.lua'

function Resolve-WorkspaceRoot {
  param([string]$StartPath)

  $current = Resolve-Path $StartPath
  while ($true) {
    if (Test-Path (Join-Path $current '.codex\project.yaml')) {
      return $current
    }
    $parent = Split-Path $current -Parent
    if (-not $parent -or $parent -eq $current) {
      return $null
    }
    $current = $parent
  }
}

function Get-YamlValue {
  param(
    [string]$YamlPath,
    [string]$Key
  )

  if (-not (Test-Path -LiteralPath $YamlPath)) {
    return $null
  }

  $pattern = '^\s*' + [regex]::Escape($Key) + ':\s*(.+?)\s*$'
  foreach ($line in Get-Content -LiteralPath $YamlPath) {
    if ($line -match $pattern) {
      $raw = $matches[1].Trim()
      if ($raw -match '^(#.*)?$') { return $null }
      $hashPos = $raw.IndexOf('#')
      if ($hashPos -ge 0) {
        $raw = $raw.Substring(0, $hashPos).Trim()
      }
      if ([string]::IsNullOrWhiteSpace($raw)) { return $null }
      if ($raw -eq 'null' -or $raw -eq '~') { return $null }
      if (($raw.StartsWith('"') -and $raw.EndsWith('"')) -or ($raw.StartsWith("'") -and $raw.EndsWith("'"))) {
        $raw = $raw.Substring(1, $raw.Length - 2)
      }
      return $raw
    }
  }
  return $null
}

function Convert-MdImagePath {
  param(
    [string]$Candidate,
    [string]$WorkspaceRoot,
    [string]$SourceDir
  )

  $path = $Candidate.Trim() -replace '\\', '/'
  if ($path.StartsWith('./')) {
    $path = $path.Substring(2)
  }
  if ([System.IO.Path]::IsPathRooted($path)) {
    return $path
  }
  $fromSourceDir = Join-Path $SourceDir ($path -replace '/', '\')
  if (Test-Path -LiteralPath $fromSourceDir) {
    return $fromSourceDir
  }
  $fromRoot = Join-Path $WorkspaceRoot ($path -replace '/', '\')
  if (Test-Path -LiteralPath $fromRoot) {
    return $fromRoot
  }
  return $null
}

function Convert-EmfWmfToPng {
  param(
    [string]$InputPath
  )
  Add-Type -AssemblyName System.Drawing
  $pngPath = [System.IO.Path]::ChangeExtension($InputPath, '.png')
  $img = [System.Drawing.Image]::FromFile($InputPath)
  try {
    $img.Save($pngPath, [System.Drawing.Imaging.ImageFormat]::Png)
  } finally {
    $img.Dispose()
  }
  return $pngPath
}

function Prepare-MarkdownForPandoc {
  param(
    [string]$SourcePath,
    [string]$WorkspaceRoot
  )

  $sourceDir = [System.IO.Path]::GetDirectoryName($SourcePath)
  $raw = Get-Content -LiteralPath $SourcePath -Raw -Encoding UTF8
  $content = $raw

  $warnings = New-Object System.Collections.Generic.List[string]
  $fixes = New-Object System.Collections.Generic.List[string]

  if ($content -match '(?is)<table\b') {
    $warnings.Add('Detected HTML <table> blocks. Prefer Pandoc Markdown tables for stable Word output.')
  }
  if ($content -match '(?is)<(td|th)[^>]*(rowspan|colspan)\s*=') {
    $warnings.Add('Detected rowspan/colspan in HTML tables. This is a common source of Word table layout issues.')
  }

  $imgPattern = '<img\b[^>]*>'
  $matches = [regex]::Matches($content, $imgPattern, [System.Text.RegularExpressions.RegexOptions]::IgnoreCase)

  foreach ($m in $matches) {
    $tag = $m.Value
    $srcMatch = [regex]::Match($tag, 'src\s*=\s*"(.*?)"', [System.Text.RegularExpressions.RegexOptions]::IgnoreCase)
    if (-not $srcMatch.Success) { continue }
    $src = $srcMatch.Groups[1].Value.Trim()
    if ([string]::IsNullOrWhiteSpace($src)) { continue }

    $resolved = Convert-MdImagePath -Candidate $src -WorkspaceRoot $WorkspaceRoot -SourceDir $sourceDir
    $replacementSrc = ($src -replace '\\', '/')

    if ($resolved) {
      $ext = [System.IO.Path]::GetExtension($resolved).ToLowerInvariant()
      if ($ext -eq '.emf' -or $ext -eq '.wmf') {
        try {
          $pngAbs = Convert-EmfWmfToPng -InputPath $resolved
          $pngRel = [System.IO.Path]::GetRelativePath($WorkspaceRoot, $pngAbs) -replace '\\', '/'
          $replacementSrc = $pngRel
          $fixes.Add("Converted vector image '$src' to '$pngRel' for Pandoc compatibility.")
        } catch {
          $warnings.Add("Failed to convert '$src' to PNG: $($_.Exception.Message)")
        }
      } else {
        $replacementSrc = [System.IO.Path]::GetRelativePath($WorkspaceRoot, $resolved) -replace '\\', '/'
      }
    } else {
      $warnings.Add("Image path not found: '$src'")
    }

    $widthMatch = [regex]::Match($tag, 'width\s*:\s*([0-9.]+in)', [System.Text.RegularExpressions.RegexOptions]::IgnoreCase)
    $heightMatch = [regex]::Match($tag, 'height\s*:\s*([0-9.]+in)', [System.Text.RegularExpressions.RegexOptions]::IgnoreCase)

    $attrs = @()
    if ($widthMatch.Success) { $attrs += "width=$($widthMatch.Groups[1].Value)" }
    if ($heightMatch.Success) { $attrs += "height=$($heightMatch.Groups[1].Value)" }

    $replacement = "![]($replacementSrc)"
    if ($attrs.Count -gt 0) {
      $replacement += "{${($attrs -join ' ')}}"
    }
    $content = $content.Replace($tag, $replacement)
  }

  if ($content -ne $raw) {
    $tmpDir = Join-Path $env:TEMP ('md_to_docx_' + [guid]::NewGuid().ToString('N'))
    New-Item -ItemType Directory -Force -Path $tmpDir | Out-Null
    $tmpMd = Join-Path $tmpDir ([System.IO.Path]::GetFileName($SourcePath))
    Set-Content -LiteralPath $tmpMd -Value $content -Encoding UTF8
    return @{
      Path = $tmpMd
      TempDir = $tmpDir
      Warnings = $warnings
      Fixes = $fixes
    }
  }

  return @{
    Path = $SourcePath
    TempDir = $null
    Warnings = $warnings
    Fixes = $fixes
  }
}

function Resolve-ProjectPath {
  param(
    [string]$Root,
    [string]$RelativePath
  )

  if ([string]::IsNullOrWhiteSpace($RelativePath)) {
    return $null
  }
  if ([System.IO.Path]::IsPathRooted($RelativePath)) {
    return $RelativePath
  }
  return (Join-Path $Root $RelativePath)
}

function Ensure-Child {
  param($Parent, [string]$LocalName, $Doc, $NamespaceManager, [string]$NamespaceUri)

  $node = $Parent.SelectSingleNode("w:$LocalName", $NamespaceManager)
  if ($null -eq $node) {
    $node = $Doc.CreateElement('w', $LocalName, $NamespaceUri)
    [void]$Parent.AppendChild($node)
  }
  return $node
}

function Set-Border {
  param($Borders, [string]$Name, [string]$Value, [string]$Size, $Doc, $NamespaceManager, [string]$NamespaceUri)

  $node = $Borders.SelectSingleNode("w:$Name", $NamespaceManager)
  if ($null -eq $node) {
    $node = $Doc.CreateElement('w', $Name, $NamespaceUri)
    [void]$Borders.AppendChild($node)
  }

  [void]$node.SetAttribute('val', $NamespaceUri, $Value)
  if ($Value -eq 'single') {
    [void]$node.SetAttribute('sz', $NamespaceUri, $Size)
    [void]$node.SetAttribute('space', $NamespaceUri, '0')
    [void]$node.SetAttribute('color', $NamespaceUri, '000000')
  } else {
    $node.RemoveAttribute('sz', $NamespaceUri)
    $node.RemoveAttribute('space', $NamespaceUri)
    $node.RemoveAttribute('color', $NamespaceUri)
  }
}

if ([string]::IsNullOrWhiteSpace($WorkspaceRoot)) {
  $WorkspaceRoot = Resolve-WorkspaceRoot -StartPath '.'
  if ($null -eq $WorkspaceRoot) {
    $WorkspaceRoot = (Resolve-Path '.').Path
  }
} else {
  $WorkspaceRoot = (Resolve-Path $WorkspaceRoot).Path
}

$projectYaml = Join-Path $WorkspaceRoot '.codex\project.yaml'

$projectSource = Get-YamlValue -YamlPath $projectYaml -Key 'current_pandoc_manuscript'
if (-not $projectSource) {
  $projectSource = Get-YamlValue -YamlPath $projectYaml -Key 'source_of_truth'
}
$projectReference = Get-YamlValue -YamlPath $projectYaml -Key 'reference_docx'
$projectBibliography = Get-YamlValue -YamlPath $projectYaml -Key 'bibliography'
$projectFilter = Get-YamlValue -YamlPath $projectYaml -Key 'docx_blank_line_filter'

$sourceCandidate = $projectSource
if (-not [string]::IsNullOrWhiteSpace($SourcePath)) {
  $sourceCandidate = $SourcePath
}

$referenceCandidate = $projectReference
if (-not [string]::IsNullOrWhiteSpace($ReferenceDocPath)) {
  $referenceCandidate = $ReferenceDocPath
}
if ([string]::IsNullOrWhiteSpace($referenceCandidate) -and (Test-Path -LiteralPath $bundledReference)) {
  $referenceCandidate = $bundledReference
}

$bibliographyCandidate = $projectBibliography
if (-not [string]::IsNullOrWhiteSpace($BibliographyPath)) {
  $bibliographyCandidate = $BibliographyPath
}

$filterCandidate = $projectFilter
if (-not [string]::IsNullOrWhiteSpace($LuaFilterPath)) {
  $filterCandidate = $LuaFilterPath
}
if ([string]::IsNullOrWhiteSpace($filterCandidate) -and (Test-Path -LiteralPath $bundledFilter)) {
  $filterCandidate = $bundledFilter
}

$resolvedSource = Resolve-ProjectPath -Root $WorkspaceRoot -RelativePath $sourceCandidate
$resolvedReference = Resolve-ProjectPath -Root $WorkspaceRoot -RelativePath $referenceCandidate
$resolvedBibliography = Resolve-ProjectPath -Root $WorkspaceRoot -RelativePath $bibliographyCandidate
$resolvedFilter = Resolve-ProjectPath -Root $WorkspaceRoot -RelativePath $filterCandidate

if (-not $resolvedSource -or -not (Test-Path -LiteralPath $resolvedSource)) {
  throw "Could not resolve SourcePath."
}
if (-not $resolvedReference -or -not (Test-Path -LiteralPath $resolvedReference)) {
  throw "Could not resolve ReferenceDocPath."
}
if (-not $resolvedFilter -or -not (Test-Path -LiteralPath $resolvedFilter)) {
  throw "Could not resolve LuaFilterPath."
}

 $prepared = Prepare-MarkdownForPandoc -SourcePath $resolvedSource -WorkspaceRoot $WorkspaceRoot
 $pandocSource = $prepared.Path
 foreach ($f in $prepared.Fixes) {
  Write-Host "[preflight/fix] $f"
 }
 foreach ($w in $prepared.Warnings) {
  Write-Warning $w
 }

if ([string]::IsNullOrWhiteSpace($OutputPath)) {
  $sourceBase = [System.IO.Path]::GetFileNameWithoutExtension($resolvedSource)
  $OutputPath = Join-Path $WorkspaceRoot ("output\submission\docx\{0}.docx" -f $sourceBase)
} else {
  $OutputPath = Resolve-ProjectPath -Root $WorkspaceRoot -RelativePath $OutputPath
}

$buildOutput = [System.IO.Path]::ChangeExtension($OutputPath, '.build.tmp.docx')

if (Test-Path -LiteralPath $buildOutput) {
  Remove-Item -LiteralPath $buildOutput -Force
}

Add-Type -AssemblyName System.IO.Compression.FileSystem

if ($resolvedBibliography -and (Test-Path -LiteralPath $resolvedBibliography)) {
  & pandoc `
    $pandocSource `
    '--from' 'markdown+pipe_tables+raw_attribute+grid_tables' `
    '--to' 'docx' `
    '--standalone' `
    '--citeproc' `
    "--bibliography=$resolvedBibliography" `
    "--resource-path=$WorkspaceRoot" `
    "--reference-doc=$resolvedReference" `
    "--lua-filter=$resolvedFilter" `
    '--output' $buildOutput
} else {
  & pandoc `
    $pandocSource `
    '--from' 'markdown+pipe_tables+raw_attribute+grid_tables' `
    '--to' 'docx' `
    '--standalone' `
    '--citeproc' `
    "--resource-path=$WorkspaceRoot" `
    "--reference-doc=$resolvedReference" `
    "--lua-filter=$resolvedFilter" `
    '--output' $buildOutput
}

if ($LASTEXITCODE -ne 0) {
  throw "Pandoc export failed."
}

$tmp = Join-Path $env:TEMP ('docx_tables_' + [guid]::NewGuid().ToString('N'))
New-Item -ItemType Directory -Force -Path $tmp | Out-Null
$zipForExpand = $null
$zipForCompress = $null

try {
  $zipForExpand = Join-Path $env:TEMP ('docx_tables_' + [guid]::NewGuid().ToString('N') + '.zip')
  Copy-Item -LiteralPath $buildOutput -Destination $zipForExpand -Force
  Expand-Archive -LiteralPath $zipForExpand -DestinationPath $tmp -Force

  $documentPath = Join-Path $tmp 'word\document.xml'
  [xml]$doc = Get-Content -Raw -Encoding UTF8 $documentPath
  $nsm = New-Object System.Xml.XmlNamespaceManager($doc.NameTable)
  $nsm.AddNamespace('w', 'http://schemas.openxmlformats.org/wordprocessingml/2006/main')
  $wNs = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'

  $tables = @($doc.SelectNodes('//w:tbl', $nsm))
  foreach ($tbl in $tables) {
    $tblPr = $tbl.SelectSingleNode('w:tblPr', $nsm)
    if ($null -eq $tblPr) {
      $tblPr = $doc.CreateElement('w', 'tblPr', $wNs)
      [void]$tbl.PrependChild($tblPr)
    }

    $tblBorders = Ensure-Child -Parent $tblPr -LocalName 'tblBorders' -Doc $doc -NamespaceManager $nsm -NamespaceUri $wNs
    Set-Border -Borders $tblBorders -Name 'top' -Value 'single' -Size '12' -Doc $doc -NamespaceManager $nsm -NamespaceUri $wNs
    Set-Border -Borders $tblBorders -Name 'bottom' -Value 'single' -Size '12' -Doc $doc -NamespaceManager $nsm -NamespaceUri $wNs
    foreach ($borderName in 'left', 'right', 'insideH', 'insideV') {
      Set-Border -Borders $tblBorders -Name $borderName -Value 'nil' -Size '0' -Doc $doc -NamespaceManager $nsm -NamespaceUri $wNs
    }

    $rows = @($tbl.SelectNodes('w:tr', $nsm))
    foreach ($row in $rows) {
      foreach ($tc in @($row.SelectNodes('w:tc', $nsm))) {
        $tcPr = $tc.SelectSingleNode('w:tcPr', $nsm)
        if ($null -eq $tcPr) {
          $tcPr = $doc.CreateElement('w', 'tcPr', $wNs)
          [void]$tc.PrependChild($tcPr)
        }
        $tcBorders = Ensure-Child -Parent $tcPr -LocalName 'tcBorders' -Doc $doc -NamespaceManager $nsm -NamespaceUri $wNs
        foreach ($borderName in 'top', 'left', 'bottom', 'right', 'insideH', 'insideV') {
          Set-Border -Borders $tcBorders -Name $borderName -Value 'nil' -Size '0' -Doc $doc -NamespaceManager $nsm -NamespaceUri $wNs
        }
      }
    }

    if ($rows.Count -gt 0) {
      foreach ($tc in @($rows[0].SelectNodes('w:tc', $nsm))) {
        $tcBorders = $tc.SelectSingleNode('w:tcPr/w:tcBorders', $nsm)
        Set-Border -Borders $tcBorders -Name 'top' -Value 'single' -Size '12' -Doc $doc -NamespaceManager $nsm -NamespaceUri $wNs
        Set-Border -Borders $tcBorders -Name 'bottom' -Value 'single' -Size '8' -Doc $doc -NamespaceManager $nsm -NamespaceUri $wNs
      }
      foreach ($tc in @($rows[$rows.Count - 1].SelectNodes('w:tc', $nsm))) {
        $tcBorders = $tc.SelectSingleNode('w:tcPr/w:tcBorders', $nsm)
        Set-Border -Borders $tcBorders -Name 'bottom' -Value 'single' -Size '12' -Doc $doc -NamespaceManager $nsm -NamespaceUri $wNs
      }
    }
  }

  $doc.Save($documentPath)

  if (Test-Path -LiteralPath $OutputPath) {
    Remove-Item -LiteralPath $OutputPath -Force
  }
  if (Test-Path -LiteralPath $buildOutput) {
    Remove-Item -LiteralPath $buildOutput -Force
  }

  $zipForCompress = Join-Path $env:TEMP ('docx_tables_' + [guid]::NewGuid().ToString('N') + '.zip')
  $zip = [System.IO.Compression.ZipFile]::Open($zipForCompress, [System.IO.Compression.ZipArchiveMode]::Create)
  try {
    foreach ($file in Get-ChildItem -LiteralPath $tmp -Recurse -File) {
      $relative = $file.FullName.Substring($tmp.Length).TrimStart('\', '/')
      $entryName = $relative -replace '\\', '/'
      [void][System.IO.Compression.ZipFileExtensions]::CreateEntryFromFile($zip, $file.FullName, $entryName)
    }
  } finally {
    $zip.Dispose()
  }

  Move-Item -LiteralPath $zipForCompress -Destination $buildOutput -Force
  Move-Item -LiteralPath $buildOutput -Destination $OutputPath -Force
  Write-Host "Built $OutputPath"
  Write-Host "Styled tables: $($tables.Count)"
} finally {
  if ($prepared -and $prepared.TempDir -and (Test-Path -LiteralPath $prepared.TempDir)) {
    Remove-Item -LiteralPath $prepared.TempDir -Recurse -Force
  }
  if ($zipForExpand -and (Test-Path -LiteralPath $zipForExpand)) {
    Remove-Item -LiteralPath $zipForExpand -Force
  }
  if ($zipForCompress -and (Test-Path -LiteralPath $zipForCompress)) {
    Remove-Item -LiteralPath $zipForCompress -Force
  }
  if (Test-Path $tmp) {
    Remove-Item -LiteralPath $tmp -Recurse -Force
  }
}
