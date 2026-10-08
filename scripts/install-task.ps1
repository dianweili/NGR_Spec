# 注册每日 07:00 的 6G RAN 跟踪任务。以普通用户运行即可。
$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
$python = Join-Path $root ".venv\Scripts\python.exe"
if (-not (Test-Path -LiteralPath $python)) { throw "未找到 $python，请先创建虚拟环境" }
$command = "Set-Location -LiteralPath '$root'; & '$python' -m ngr run"
$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-NoProfile -WindowStyle Hidden -Command `"$command`""
$trigger = New-ScheduledTaskTrigger -Daily -At 7:00am
$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -DontStopIfGoingOnBatteries -ExecutionTimeLimit (New-TimeSpan -Hours 3)
Register-ScheduledTask -TaskName "NGR_Spec" -Action $action -Trigger $trigger -Settings $settings -Description "6G RAN 进展跟踪" -Force
Write-Host "已注册 NGR_Spec（每日 07:00）。手动触发：Start-ScheduledTask -TaskName NGR_Spec"
