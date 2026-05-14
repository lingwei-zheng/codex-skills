[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$ExtraArgs
)

$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path

$python = Get-Command py -ErrorAction SilentlyContinue
if ($python) {
    & py -3 "$RepoRoot\scripts\install_skills.py" --platform windows --source-root "$RepoRoot" @ExtraArgs
    exit $LASTEXITCODE
}

$python = Get-Command python -ErrorAction SilentlyContinue
if ($python) {
    & python "$RepoRoot\scripts\install_skills.py" --platform windows --source-root "$RepoRoot" @ExtraArgs
    exit $LASTEXITCODE
}

throw "Python 3 is required to install skills on Windows."
