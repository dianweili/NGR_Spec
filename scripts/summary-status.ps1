$ErrorActionPreference = 'Stop'

$root = Split-Path -Parent $PSScriptRoot
$python = Join-Path $root '.venv\Scripts\python.exe'
$statusScript = Join-Path $PSScriptRoot 'summary_status.py'
& $python $statusScript
exit $LASTEXITCODE
