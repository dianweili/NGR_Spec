# NGR Spec

追踪 3GPP RAN 中 6G（Rel-20/6GR）及其必要 5G-A 血统的协议进展，产出可 diff 的事件库、Markdown 看板和单页 HTML。

## 使用

在已安装依赖的虚拟环境中运行：

```powershell
.\.venv\Scripts\python.exe -m ngr doctor
.\.venv\Scripts\python.exe -m ngr run --no-llm
```

`run` 抓取、解析、归集、渲染；加 `--no-llm` 不调用 Codex。`backfill --wg RAN1 --from 112 --to 127` 回填区间；`remap` 在修改血统规则后离线重算；`enrich` 补跑 Codex 摘要；`lineage-report` 检查血统命中；`doctor --network` 额外测试 3GPP 连通性。

摘要由本机 `codex exec` 使用当前 ChatGPT/Codex 登录态完成。首次回填应先使用 `--no-llm`，检查 `lineage-report` 后再运行 `enrich`。

## 配置与退出码

在 `config/features.yaml` 添加特性和 `lineage` 段：每段声明工作组会议范围，以及议程锚点或标题正则。修改后运行 `remap`，无需重新联网。

| 退出码 | 含义 |
| --- | --- |
| 0 | 成功 |
| 2 | 解析防线失败；原始数据已保留 |
| 3 | Codex 用量受限，留待下次补跑 |
| 4 | `config/` 有未提交手工改动，跳过自动提交 |

可运行 `scripts/install-task.ps1` 注册每日 07:00 任务；`-StartWhenAvailable` 会在设备错过计划时间后补跑。
