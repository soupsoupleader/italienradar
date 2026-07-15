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
      $stdout = ""; $stderr = ""; $exitCode = $null; $source = ""
      try {
        $psi = [System.Diagnostics.ProcessStartInfo]::new()
        $psi.FileName = (Resolve-Path -LiteralPath $candidate).Path
        $psi.Arguments = "--version"
        $psi.UseShellExecute = $false
        $psi.RedirectStandardOutput = $true
        $psi.RedirectStandardError = $true
        $psi.CreateNoWindow = $true
        $proc = [System.Diagnostics.Process]::new(); $proc.StartInfo = $psi
        [void]$proc.Start()
        if (-not $proc.WaitForExit(10000)) { $proc.Kill(); throw "CHROME_VERSION_TIMEOUT" }
        $stdout = $proc.StandardOutput.ReadToEnd(); $stderr = $proc.StandardError.ReadToEnd(); $exitCode = $proc.ExitCode
      } catch { $stderr = $_.Exception.Message; $exitCode = -1 }
      $version = [regex]::Match($stdout, '\d+\.\d+\.\d+\.\d+').Value
      if ($version) { $source = "stdout" }
      if (-not $version) { $version = [regex]::Match($stderr, '\d+\.\d+\.\d+\.\d+').Value; if ($version) { $source = "stderr" } }
      if (-not $version) { $version = [regex]::Match((Get-Item -LiteralPath $candidate).VersionInfo.ProductVersion, '\d+\.\d+\.\d+\.\d+').Value; if ($version) { $source = "file-version" } }
      if ($version) { return [PSCustomObject]@{Path=(Resolve-Path -LiteralPath $candidate).Path;Version=$version;VersionSource=$source;VersionStdout=$stdout.Trim();VersionStderr=$stderr.Trim();VersionExitCode=$exitCode} }
    }
  }
  throw "RENDERER_NOT_FOUND: Chrome could not be resolved"
}

$chrome = Resolve-Chrome
$sourceCommit = (& git rev-parse HEAD 2>$null | Select-Object -First 1).Trim()
if ($sourceCommit -notmatch '^[0-9a-f]{40}$') { throw "P0_SOURCE_COMMIT_UNAVAILABLE" }
$python = if ($env:ITALIENRADAR_PYTHON_PATH) { $env:ITALIENRADAR_PYTHON_PATH } else { "python" }
$builder = Join-Path $repo "download-system\scripts\build_document.py"
$documentUrl = "file:///" + $document.Replace("\", "/")
if (Test-Path -LiteralPath $out) { Remove-Item -LiteralPath $out -Recurse -Force }
if (Test-Path -LiteralPath $raw) { Remove-Item -LiteralPath $raw -Force }
if (Test-Path -LiteralPath $final) { Remove-Item -LiteralPath $final -Force }
if (Test-Path -LiteralPath $chromeProfile) { Remove-Item -LiteralPath $chromeProfile -Recurse -Force }
& $python $builder --input (Join-Path $repo $InputFile) --bundle $bundle --output $out --chrome-version $chrome.Version --source-commit $sourceCommit
if ($LASTEXITCODE -ne 0) { throw "DOCUMENT_BUILD_FAILED: $LASTEXITCODE" }
if (-not (Test-Path -LiteralPath $document)) { throw "BUNDLE_DOCUMENT_MISSING" }

$flags = @("--headless","--no-pdf-header-footer","--disable-background-networking","--disable-component-update","--disable-default-apps","--disable-extensions","--disable-features=OptimizationHints,MediaRouter,AutofillServerCommunication","--no-first-run","--no-sandbox","--run-all-compositor-stages-before-draw","--virtual-time-budget=1000","--user-data-dir=$chromeProfile","--print-to-pdf=$raw",$documentUrl)
$process = Start-Process -FilePath $chrome.Path -ArgumentList $flags -PassThru -WindowStyle Hidden
$completed = $process.WaitForExit(60000)
if (-not $completed) { Stop-Process -Id $process.Id -Force; throw "RENDERER_TIMEOUT" }
if (-not (Test-Path -LiteralPath $raw)) { throw "PDF_OUTPUT_MISSING" }
Copy-Item -LiteralPath $raw -Destination $final -Force
$renderer = [ordered]@{path_rule="ITALIENRADAR_CHROME_PATH > HKCU/HKLM App Paths > Program Files";resolved_path=$chrome.Path;version=$chrome.Version;version_source=$chrome.VersionSource;version_stdout=$chrome.VersionStdout;version_stderr=$chrome.VersionStderr;version_exit_code=$chrome.VersionExitCode;flags=$flags;offline=$true;locale="de-DE";timezone="UTC";capability_gate="DECLARED_AND_VERIFIED_BY_VERIFY_BUILD"}
$renderer | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath (Join-Path $out "renderer-report.json") -Encoding UTF8
$report = Get-Content -Raw -LiteralPath (Join-Path $out "build-report.json") | ConvertFrom-Json
$report | Add-Member -NotePropertyName renderer_path -NotePropertyValue $chrome.Path -Force
$report | Add-Member -NotePropertyName renderer_version -NotePropertyValue $chrome.Version -Force
$report | Add-Member -NotePropertyName renderer_version_source -NotePropertyValue $chrome.VersionSource -Force
$report | Add-Member -NotePropertyName renderer_version_stdout -NotePropertyValue $chrome.VersionStdout -Force
$report | Add-Member -NotePropertyName renderer_version_stderr -NotePropertyValue $chrome.VersionStderr -Force
$report | Add-Member -NotePropertyName renderer_version_exit_code -NotePropertyValue $chrome.VersionExitCode -Force
$report | Add-Member -NotePropertyName pdf -NotePropertyValue (Split-Path -Leaf $final) -Force
$report | Add-Member -NotePropertyName capability_gate -NotePropertyValue "PENDING_VERIFY_BUILD" -Force
$report | Add-Member -NotePropertyName flags -NotePropertyValue $flags -Force
$report | ConvertTo-Json -Depth 6 | Set-Content -LiteralPath (Join-Path $out "build-report.json") -Encoding UTF8
if (Test-Path -LiteralPath $chromeProfile) { Remove-Item -LiteralPath $chromeProfile -Recurse -Force }
Write-Output "BUILD_NAME=$BuildName"
Write-Output "CHROME_VERSION=$($chrome.Version)"
Write-Output "RAW_PDF=$raw"
Write-Output "PDF=$final"
