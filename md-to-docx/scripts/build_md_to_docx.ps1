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

function Normalize-TeXExpression {
  param([string]$Expression)

  return ($Expression -replace '\^\{\}', '' -replace '_\{\}', '')
}

function Normalize-PandocMath {
  param(
    [string]$Content,
    $Warnings,
    $Fixes
  )

  $fencedMathPattern = '(?ms)^[ \t]*```[ \t]*math[ \t]*\r?\n(?<expr>.*?)(?:\r?\n)[ \t]*```[ \t]*$'
  $Content = [regex]::Replace(
    $Content,
    $fencedMathPattern,
    [System.Text.RegularExpressions.MatchEvaluator]{
      param($match)
      $expression = Normalize-TeXExpression -Expression $match.Groups['expr'].Value.Trim()
      $Fixes.Add('Converted a fenced ``` math block to Pandoc display math.')
      return '$$' + [Environment]::NewLine + $expression + [Environment]::NewLine + '$$'
    }
  )

  $inlineCodeMathPattern = '\$`(?<expr>[^`\r\n]+)`\$'
  $Content = [regex]::Replace(
    $Content,
    $inlineCodeMathPattern,
    [System.Text.RegularExpressions.MatchEvaluator]{
      param($match)
      $expression = Normalize-TeXExpression -Expression $match.Groups['expr'].Value
      $Fixes.Add('Removed code backticks from an inline TeX expression.')
      return '$' + $expression + '$'
    }
  )

  if ($Content -match '(?m)^[ \t]*```[ \t]*math[ \t]*$') {
    $Warnings.Add('Unconverted fenced math remains. Use $$...$$ for Word equations.')
  }
  if ($Content -match '\$`|`\$') {
    $Warnings.Add('Malformed inline math remains. Do not place code backticks inside $...$.')
  }

  return $Content
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

  $content = Normalize-PandocMath -Content $content -Warnings $warnings -Fixes $fixes

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

  $mdImagePattern = '!\[(?<alt>[^\]]*)\]\((?<path>[^)\s]+)\)(?<attrs>\{[^}]+\})?'
  $mdMatches = [regex]::Matches($content, $mdImagePattern)
  foreach ($m in $mdMatches) {
    $full = $m.Value
    $alt = $m.Groups['alt'].Value
    $candidate = $m.Groups['path'].Value
    $attrs = $m.Groups['attrs'].Value
    $resolved = Convert-MdImagePath -Candidate $candidate -WorkspaceRoot $WorkspaceRoot -SourceDir $sourceDir
    if ($resolved) {
      $normalizedAbs = ($resolved -replace '\\', '/')
      $replacement = "![$alt]($normalizedAbs)$attrs"
      if ($replacement -ne $full) {
        $content = $content.Replace($full, $replacement)
      }
    } elseif ($candidate -notmatch '^[A-Za-z]+:') {
      $warnings.Add("Markdown image path not found: '$candidate'")
    }
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

function Ensure-RunProperty {
  param($Run, $Doc, $NamespaceManager, [string]$NamespaceUri)

  $rPr = $Run.SelectSingleNode('w:rPr', $NamespaceManager)
  if ($null -eq $rPr) {
    $rPr = $Doc.CreateElement('w', 'rPr', $NamespaceUri)
    if ($Run.HasChildNodes) {
      [void]$Run.InsertBefore($rPr, $Run.FirstChild)
    } else {
      [void]$Run.AppendChild($rPr)
    }
  }
  return $rPr
}

function Set-RunToggle {
  param($RunProperty, [string]$LocalName, [bool]$Enabled, $Doc, $NamespaceManager, [string]$NamespaceUri)

  $node = $RunProperty.SelectSingleNode("w:$LocalName", $NamespaceManager)
  if ($Enabled) {
    if ($null -eq $node) {
      $node = $Doc.CreateElement('w', $LocalName, $NamespaceUri)
      [void]$RunProperty.AppendChild($node)
    }
  } elseif ($null -ne $node) {
    [void]$RunProperty.RemoveChild($node)
  }
}

function Set-ParagraphJustification {
  param($Paragraph, [string]$Value, $Doc, $NamespaceManager, [string]$NamespaceUri)

  $pPr = $Paragraph.SelectSingleNode('w:pPr', $NamespaceManager)
  if ($null -eq $pPr) {
    $pPr = $Doc.CreateElement('w', 'pPr', $NamespaceUri)
    if ($Paragraph.HasChildNodes) {
      [void]$Paragraph.InsertBefore($pPr, $Paragraph.FirstChild)
    } else {
      [void]$Paragraph.AppendChild($pPr)
    }
  }
  $jc = $pPr.SelectSingleNode('w:jc', $NamespaceManager)
  if ($null -eq $jc) {
    $jc = $Doc.CreateElement('w', 'jc', $NamespaceUri)
    [void]$pPr.AppendChild($jc)
  }
  [void]$jc.SetAttribute('val', $NamespaceUri, $Value)
}

function Add-TextPrefixToParagraph {
  param($Paragraph, [string]$Prefix, $Doc, $NamespaceManager, [string]$NamespaceUri)

  if ([string]::IsNullOrWhiteSpace($Prefix)) {
    return
  }

  $firstText = $Paragraph.SelectSingleNode('.//w:t', $NamespaceManager)
  if ($null -ne $firstText) {
    $firstText.InnerText = $Prefix + $firstText.InnerText
    return
  }

  $run = $Doc.CreateElement('w', 'r', $NamespaceUri)
  $text = $Doc.CreateElement('w', 't', $NamespaceUri)
  $text.InnerText = $Prefix
  [void]$run.AppendChild($text)
  [void]$Paragraph.AppendChild($run)
}

function Convert-HeadingsToMinimalBody {
  param($Doc, $NamespaceManager, [string]$NamespaceUri)

  $converted = 0
  $firstHeading = $true
  $sectionCounters = @(0, 0, 0, 0, 0, 0)
  $numberingActive = $true
  foreach ($p in @($Doc.SelectNodes('//w:p', $NamespaceManager))) {
    $pStyle = $p.SelectSingleNode('w:pPr/w:pStyle', $NamespaceManager)
    if ($null -eq $pStyle) {
      continue
    }

    $styleId = $pStyle.GetAttribute('val', $NamespaceUri)
    $level = $null
    if ($styleId -match '^(Heading)?([1-6])$') {
      $level = [int]$Matches[2]
    } elseif ($styleId -match '^heading([1-6])$') {
      $level = [int]$Matches[1]
    }
    if ($null -eq $level) {
      continue
    }

    $paragraphText = ''
    foreach ($t in @($p.SelectNodes('.//w:t', $NamespaceManager))) {
      $paragraphText += $t.InnerText
    }
    $paragraphText = $paragraphText.Trim()

    $bold = $false
    $italic = $false
    $numberPrefix = ''
    $isDocumentTitle = $firstHeading
    if ($isDocumentTitle) {
      $bold = $true
      Set-ParagraphJustification -Paragraph $p -Value 'center' -Doc $Doc -NamespaceManager $NamespaceManager -NamespaceUri $NamespaceUri
      $firstHeading = $false
    } elseif ($paragraphText -match '^(Abstract|References|Supplementary Material)$') {
      $bold = $true
      if ($paragraphText -match '^(References|Supplementary Material)$') {
        $numberingActive = $false
      }
    } elseif ($level -eq 1) {
      $bold = $true
    } elseif ($level -eq 2) {
      $bold = $true
      $italic = $true
    } else {
      $italic = $true
    }

    if ((-not $isDocumentTitle) -and $numberingActive -and $paragraphText -notmatch '^(Abstract|References|Supplementary Material)$' -and $paragraphText -notmatch '^\d+(\.\d+)*\.?\s+') {
      $sectionCounters[$level - 1] += 1
      for ($counterIndex = $level; $counterIndex -lt $sectionCounters.Count; $counterIndex++) {
        $sectionCounters[$counterIndex] = 0
      }
      $activeNumbers = @()
      for ($counterIndex = 0; $counterIndex -lt $level; $counterIndex++) {
        if ($sectionCounters[$counterIndex] -gt 0) {
          $activeNumbers += [string]$sectionCounters[$counterIndex]
        }
      }
      if ($activeNumbers.Count -gt 0) {
        $numberPrefix = ($activeNumbers -join '.') + '. '
      }
    }

    $pPr = $p.SelectSingleNode('w:pPr', $NamespaceManager)
    [void]$pPr.RemoveChild($pStyle)
    Add-TextPrefixToParagraph -Paragraph $p -Prefix $numberPrefix -Doc $Doc -NamespaceManager $NamespaceManager -NamespaceUri $NamespaceUri

    foreach ($r in @($p.SelectNodes('w:r', $NamespaceManager))) {
      $rPr = Ensure-RunProperty -Run $r -Doc $Doc -NamespaceManager $NamespaceManager -NamespaceUri $NamespaceUri
      Set-RunToggle -RunProperty $rPr -LocalName 'b' -Enabled $bold -Doc $Doc -NamespaceManager $NamespaceManager -NamespaceUri $NamespaceUri
      Set-RunToggle -RunProperty $rPr -LocalName 'i' -Enabled $italic -Doc $Doc -NamespaceManager $NamespaceManager -NamespaceUri $NamespaceUri
    }
    $converted += 1
  }
  return $converted
}

function Clear-MinimalCaptionJustification {
  param($Doc, $NamespaceManager, [string]$NamespaceUri)

  $cleared = 0
  foreach ($p in @($Doc.SelectNodes('//w:p', $NamespaceManager))) {
    $text = ''
    foreach ($t in @($p.SelectNodes('.//w:t', $NamespaceManager))) {
      $text += $t.InnerText
    }
    if ($text -match '^\s*(Figure|Table)\s+[A-Za-z0-9]+\.') {
      $jc = $p.SelectSingleNode('w:pPr/w:jc', $NamespaceManager)
      if ($null -ne $jc) {
        [void]$jc.ParentNode.RemoveChild($jc)
        $cleared += 1
      }
    }
  }
  return $cleared
}

function Apply-LegacyBibliographyFormatting {
  param($Doc, $NamespaceManager, [string]$NamespaceUri)

  $formatted = 0
  $inReferences = $false
  foreach ($p in @($Doc.SelectNodes('//w:p', $NamespaceManager))) {
    $text = ''
    foreach ($t in @($p.SelectNodes('.//w:t', $NamespaceManager))) {
      $text += $t.InnerText
    }
    $text = $text.Trim()
    if ($text -eq 'References') {
      $inReferences = $true
      continue
    }
    if (-not $inReferences -or [string]::IsNullOrWhiteSpace($text)) {
      continue
    }

    $pPr = $p.SelectSingleNode('w:pPr', $NamespaceManager)
    if ($null -eq $pPr) {
      $pPr = $Doc.CreateElement('w', 'pPr', $NamespaceUri)
      if ($p.HasChildNodes) {
        [void]$p.InsertBefore($pPr, $p.FirstChild)
      } else {
        [void]$p.AppendChild($pPr)
      }
    }

    $spacing = $pPr.SelectSingleNode('w:spacing', $NamespaceManager)
    if ($null -eq $spacing) {
      $spacing = $Doc.CreateElement('w', 'spacing', $NamespaceUri)
      [void]$pPr.AppendChild($spacing)
    }
    [void]$spacing.SetAttribute('line', $NamespaceUri, '480')
    [void]$spacing.SetAttribute('lineRule', $NamespaceUri, 'auto')

    $ind = $pPr.SelectSingleNode('w:ind', $NamespaceManager)
    if ($null -eq $ind) {
      $ind = $Doc.CreateElement('w', 'ind', $NamespaceUri)
      [void]$pPr.AppendChild($ind)
    }
    [void]$ind.SetAttribute('left', $NamespaceUri, '720')
    [void]$ind.SetAttribute('hanging', $NamespaceUri, '720')
    $formatted += 1
  }
  return $formatted
}

function Set-ModernWordCompatibilityMode {
  param([string]$PackageRoot)

  $settingsPath = Join-Path $PackageRoot 'word\settings.xml'
  if (-not (Test-Path -LiteralPath $settingsPath)) {
    return 'missing-settings'
  }

  $settingsText = Get-Content -Raw -Encoding UTF8 -LiteralPath $settingsPath
  $pattern = '(<w:compatSetting\b(?=[^>]*\bw:name="compatibilityMode")[^>]*\bw:val=")([^"]*)(")'
  $match = [regex]::Match($settingsText, $pattern)
  if ($match.Success) {
    $previous = $match.Groups[2].Value
    $settingsText = [regex]::Replace($settingsText, $pattern, '${1}15${3}', 1)
    Set-Content -LiteralPath $settingsPath -Value $settingsText -Encoding UTF8 -NoNewline
    return "$previous-to-15"
  }

  $insert = '<w:compatSetting w:name="compatibilityMode" w:uri="http://schemas.microsoft.com/office/word" w:val="15"/>'
  if ($settingsText -match '</w:compat>') {
    $settingsText = $settingsText -replace '</w:compat>', "$insert</w:compat>"
  } else {
    $settingsText = $settingsText -replace '</w:settings>', "<w:compat>$insert</w:compat></w:settings>"
  }
  Set-Content -LiteralPath $settingsPath -Value $settingsText -Encoding UTF8 -NoNewline
  return 'set-to-15'
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
$pandocSourceDir = [System.IO.Path]::GetDirectoryName($pandocSource)
$resourcePath = $WorkspaceRoot
if (-not [string]::IsNullOrWhiteSpace($pandocSourceDir) -and $pandocSourceDir -ne $WorkspaceRoot) {
  $resourcePath = "$WorkspaceRoot;$pandocSourceDir"
}
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
    "--resource-path=$resourcePath" `
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
    "--resource-path=$resourcePath" `
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

  $minimalBodyHeadings = Convert-HeadingsToMinimalBody -Doc $doc -NamespaceManager $nsm -NamespaceUri $wNs
  $minimalCaptions = Clear-MinimalCaptionJustification -Doc $doc -NamespaceManager $nsm -NamespaceUri $wNs
  $legacyBibliography = Apply-LegacyBibliographyFormatting -Doc $doc -NamespaceManager $nsm -NamespaceUri $wNs

  $doc.Save($documentPath)
  $compatibilityMode = Set-ModernWordCompatibilityMode -PackageRoot $tmp

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
  Write-Host "Converted headings to minimal body text: $minimalBodyHeadings"
  Write-Host "Cleared caption centering: $minimalCaptions"
  Write-Host "Formatted bibliography paragraphs: $legacyBibliography"
  Write-Host "Word compatibility mode: $compatibilityMode"
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
