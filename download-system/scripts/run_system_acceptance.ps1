[CmdletBinding()]
param([string]$ProofRoot = ".tmp/phase-3-2-2-2-5/system-acceptance")
$ErrorActionPreference = "Stop"
$repo = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot "../..")).Path
$python = if ($env:ITALIENRADAR_PYTHON_PATH) { $env:ITALIENRADAR_PYTHON_PATH } else { "python" }
& $python (Join-Path $repo "download-system/scripts/run_system_acceptance.py") --proof-root $ProofRoot
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
