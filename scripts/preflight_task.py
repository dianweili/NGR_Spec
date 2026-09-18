"""任务下发前的自洽性预检。

用途：计划里每个任务都给出"完整实现代码 + 完整测试代码"，但两者是人写的，
可能自相矛盾（测试数据不满足自己声明的正则、排序逻辑与断言相反、
测试助手模拟了现实不存在的输入……）。Task 3/5/6 合计因此阻塞了八轮。

这个脚本把某个任务的代码块抽出来、按真实布局落到临时目录、跑一遍 pytest，
在下发给实现者之前就暴露这类矛盾。

用法：
    python scripts/preflight_task.py <任务号>
    python scripts/preflight_task.py 7 --keep    # 保留临时目录便于排查

局限（有意为之，不追求完美）：
  - 代码块按两种方式归属文件：首行的 `# path` 注释，或前文最近的反引号路径
  - 无法执行的任务（如 Task 1 纯侦察、Task 21 装计划任务）会被跳过并说明原因
  - 预检通过不代表实现无缺陷，只代表"给定代码与给定测试互相自洽"
  - 必须在下发 Task N 之前跑，此时 Task 1..N-1 已在仓库里，依赖用真实实现而非计划文本
"""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PLAN = REPO / "docs" / "superpowers" / "plans" / "2026-09-17-6g-ran-tracker.md"
VENV_PY = REPO / ".venv" / "Scripts" / "python.exe"

# 代码块首行形如 `# ngr/fetch/manifest.py` 或 `# tests/test_x.py`
PATH_COMMENT = re.compile(r"^#\s*(ngr/[\w/]+\.py|tests/[\w/]+\.py)\s*$")


def task_section(plan_text: str, number: int) -> str:
    """截取 `### Task N:` 到下一个 `### Task` 之间的正文。"""
    start = re.search(rf"^### Task {number}: ", plan_text, re.M)
    if not start:
        raise SystemExit(f"计划里找不到 Task {number}")
    nxt = re.search(r"^### Task \d+: ", plan_text[start.end():], re.M)
    end = start.end() + (nxt.start() if nxt else len(plan_text))
    return plan_text[start.start():end]


# 代码块前文里形如 **Step 3: 写 `ngr/parse/agenda.py`** 的归属声明
PATH_IN_PROSE = re.compile(r"`((?:ngr|tests)/[\w/]+\.py)`")


def extract_blocks(section: str) -> dict[str, str]:
    """抽出 `path -> 源码`。

    两种归属方式，按优先级：
      1. 代码块首行是 `# path/to/file.py`（测试块的既定约定）
      2. 代码块之前最近的一处反引号路径（实现块通常写在 "Step N: 写 `path`" 里）
    同一路径出现多次时后者覆盖前者 —— 计划里靠后的是最终版。
    """
    out: dict[str, str] = {}
    # 闭合的 ``` 必须在行首。代码里可能出现字符串内的 ```（markdown 渲染器就会写
    # "```text"），非贪婪匹配会在那里提前截断、抽出半截模块。Task 14 是被截成语法
    # 错误才暴露的 —— 更糟的情况是截出一个**语法合法但内容缺失**的模块，
    # 那样预检会给出毫无意义的 PASS。
    for m in re.finditer(r"^```python\n(.*?)^```", section, re.S | re.M):
        body = m.group(1)
        lines = body.splitlines()
        first = lines[0].strip() if lines else ""

        pm = PATH_COMMENT.match(first)
        if pm:
            out[pm.group(1)] = body
            continue

        # 往前找最近的一处路径声明；限定窗口避免误attach到很远的无关路径
        before = section[max(0, m.start() - 400):m.start()]
        cands = PATH_IN_PROSE.findall(before)
        if cands:
            out[cands[-1]] = body
    return out




def main() -> int:
    # Windows 默认控制台是 GBK，pytest 的输出里常有它编不了的字符
    # （断言差异里的特殊符号、颜色转义等）。不改这里，脚本会在 print 阶段崩掉 ——
    # 这正是本项目全局约束反复强调的编码坑，工具自己也得守。
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")

    ap = argparse.ArgumentParser()
    ap.add_argument("task", type=int)
    ap.add_argument("--keep", action="store_true", help="保留临时目录")
    args = ap.parse_args()

    plan_text = PLAN.read_text(encoding="utf-8")
    section = task_section(plan_text, args.task)
    blocks = extract_blocks(section)
    tests = {p: s for p, s in blocks.items() if p.startswith("tests/")}
    # 只取本任务的实现块。前序任务的模块以仓库里的真实实现为准 ——
    # 预检是在下发前跑的，此时 Task 1..N-1 都已交付并通过审查，
    # 用它们的真实代码比用计划里的文本更接近实际运行环境。
    impls = {p: s for p, s in blocks.items() if p.startswith("ngr/")}

    if not tests:
        print(f"Task {args.task}: 未找到带路径注释的测试代码块，跳过预检")
        print("  （纯侦察/运维类任务没有可执行的自洽性可验，属预期）")
        return 0

    work = Path(tempfile.mkdtemp(prefix=f"preflight-t{args.task}-"))
    try:
        # 以真实仓库为底，覆盖上本任务的代码块 —— 这样既能引用已交付的模块，
        # 又能让本任务尚未实现的模块以计划给出的版本参与测试。
        shutil.copytree(REPO / "ngr", work / "ngr")
        shutil.copytree(REPO / "tests" / "fixtures", work / "tests" / "fixtures")
        shutil.copytree(REPO / "config", work / "config")
        (work / "pyproject.toml").write_text(
            "[tool.pytest.ini_options]\ntestpaths=['tests']\n", encoding="utf-8")

        for path, src in {**impls, **tests}.items():
            target = work / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(src, encoding="utf-8")
            print(f"  写入 {path} ({len(src.splitlines())} 行)")

        # 计划里空的 __init__.py 通常不写成代码块（是 mkdir/touch 出来的），
        # 抽取不到。这里为 ngr 下每一级包目录补齐，否则 import 会失败。
        for d in sorted((work / "ngr").rglob("*"), key=lambda x: len(x.parts)):
            if d.name == "__pycache__" or not d.is_dir():
                continue
            if not (d / "__init__.py").exists():
                (d / "__init__.py").write_text("", encoding="utf-8")
                print(f"  补 {d.relative_to(work).as_posix()}/__init__.py")

        print(f"\n跑 pytest（{len(tests)} 个测试文件，{len(impls)} 个实现文件）\n")
        # errors="replace"：pytest 的输出可能夹带非 UTF-8 字节（二进制 fixture 的
        # 片段、Windows 控制台转义等），不加会让 text 解码失败、stdout 变成 None。
        proc = subprocess.run(
            [str(VENV_PY), "-m", "pytest", "-q", *tests],
            cwd=work, capture_output=True, text=True,
            encoding="utf-8", errors="replace")
        print((proc.stdout or "")[-6000:])
        if (proc.stderr or "").strip():
            print("--- stderr ---")
            print(proc.stderr[-2000:])

        if proc.returncode == 0:
            print(f"\n[PASS] Task {args.task} 预检通过：给定代码与给定测试自洽")
        else:
            print(f"\n[FAIL] Task {args.task} 预检失败：计划里的代码与测试不自洽，"
                  f"修好再下发（退出码 {proc.returncode}）")
        return proc.returncode
    finally:
        if args.keep:
            print(f"\n临时目录保留在 {work}")
        else:
            shutil.rmtree(work, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
