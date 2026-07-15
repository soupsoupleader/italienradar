[CmdletBinding()]
param(
  [string]$InputFile = "download-system/content/t00-neutral-build.json",
  [string]$ProofRoot = ".tmp/phase-3-2-2-2-4/master-build-proof",
  [ValidateSet("a","b")][string]$BuildName = "a"
)
$ErrorActionPreference = "Stop"
$repo = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot "../..")).Path
$proof = Join-Path $repo $ProofRoot
$bundle = Join-Path $proof ("bundle-" + $BuildName)
$out = Join-Path $proof ("run-" + $BuildName)
$document = Join-Path $bundle "document.html"
$raw = Join-Path $proof ("t00-master-build-" + $BuildName + ".raw.pdf")
$final = Join-Path $proof ("t00-master-build-" + $BuildName + ".pdf")
$chromeProfile = Join-Path $proof ("chrome-profile-" + $BuildName)
New-Item -ItemType Directory -Force -Path $proof | Out-Null

function Resolve-Chrome {
  $candidates = @()
  if ($env:ITALIENRADAR_CHROME_PATH) { $candidates += $env:ITALIENRADAR_CHROME_PATH }
  foreach ($key in @("HKCU:\Software\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe","HKLM:\Software\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe","HKLM:\Software\WOW6432Node\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe")) {
    try { $p=(Get-ItemProperty -LiteralPath $key -ErrorAction Stop).'(default)'; if($p){$candidates += $p} } catch {}
  }
  if ($env:ProgramFiles) { $candidates += (Join-Path $env:ProgramFiles "Google\Chrome\Application\chrome.exe") }
  if (${env:ProgramFiles(x86)}) { $candidates += (Join-Path ${env:ProgramFiles(x86)} "Google\Chrome\Application\chrome.exe") }
  foreach ($candidate in $candidates | Select-Object -Unique) {
    if (Test-Path -LiteralPath $candidate) {
      $version = (& $candidate --version 2>$null | Select-Object -First 1)
      if (-not $version) { $version = (Get-Item -LiteralPath $candidate).VersionInfo.ProductVersion; $version = "Chrome/$version (file-version fallback; --version produced no stdout)" }
      if ($version) { return [PSCustomObject]@{Path=(Resolve-Path -LiteralPath $candidate).Path;Version=$version} }
    }
  }
  throw "RENDERER_NOT_FOUND: Chrome could not be resolved"
}

$chrome = Resolve-Chrome
$python = if ($env:ITALIENRADAR_PYTHON_PATH) { $env:ITALIENRADAR_PYTHON_PATH } else { "python" }
$builder = Join-Path $repo "download-system\scripts\build_document.py"
$documentUrl = "file:///" + $document.Replace("\", "/")
if (Test-Path -LiteralPath $out) { Remove-Item -LiteralPath $out -Recurse -Force }
if (Test-Path -LiteralPath $raw) { Remove-Item -LiteralPath $raw -Force }
if (Test-Path -LiteralPath $final) { Remove-Item -LiteralPath $final -Force }
if (Test-Path -LiteralPath $chromeProfile) { Remove-Item -LiteralPath $chromeProfile -Recurse -Force }
& $python $builder --input (Join-Path $repo $InputFile) --bundle $bundle --output $out
if ($LASTEXITCODE -ne 0) { throw "DOCUMENT_BUILD_FAILED: $LASTEXITCODE" }
if (-not (Test-Path -LiteralPath $document)) { throw "BUNDLE_DOCUMENT_MISSING" }

$flags = @("--headless","--no-pdf-header-footer","--disable-background-networking","--disable-component-update","--disable-default-apps","--disable-extensions","--disable-features=OptimizationHints,MediaRouter,AutofillServerCommunication","--no-first-run","--no-sandbox","--run-all-compositor-stages-before-draw","--virtual-time-budget=1000","--user-data-dir=$chromeProfile","--print-to-pdf=$raw",$documentUrl)
$process = Start-Process -FilePath $chrome.Path -ArgumentList $flags -PassThru -WindowStyle Hidden
$completed = $process.WaitForExit(60000)
if (-not $completed) { Stop-Process -Id $process.Id -Force; throw "RENDERER_TIMEOUT" }
if (-not (Test-Path -LiteralPath $raw)) { throw "PDF_OUTPUT_MISSING" }
Copy-Item -LiteralPath $raw -Destination $final -Force
$renderer = [ordered]@{path_rule="ITALIENRADAR_CHROME_PATH > HKCU/HKLM App Paths > Program Files";resolved_path=$chrome.Path;version=$chrome.Version;flags=$flags;offline=true;locale="de-DE";timezone="UTC";capability_gate="DECLARED_AND_VERIFIED_BY_VERIFY_BUILD"}
$renderer | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath (Join-Path $out "renderer-report.json") -Encoding UTF8
$report = Get-Content -Raw -LiteralPath (Join-Path $out "build-report.json") | ConvertFrom-Json
$report.renderer_path = $chrome.Path; $report.renderer_version = $chrome.Version; $report.pdf = Split-Path -Leaf $final; $report.capability_gate = "PENDING_VERIFY_BUILD"; $report.flags = $flags
$report | ConvertTo-Json -Depth 6 | Set-Content -LiteralPath (Join-Path $out "build-report.json") -Encoding UTF8
Write-Output "BUILD_NAME=$BuildName"
Write-Output "CHROME_VERSION=$($chrome.Version)"
Write-Output "RAW_PDF=$raw"
Write-Output "PDF=$final"
