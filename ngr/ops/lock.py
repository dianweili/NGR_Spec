from __future__ import annotations

import json
import os
from pathlib import Path


class ExclusiveRunLock:
    """轻量跨进程锁，防止两个摘要运行互相覆盖 state。"""

    def __init__(self, path: Path):
        self.path = Path(path)
        self.held = False

    @staticmethod
    def _pid_is_running(pid: object) -> bool:
        if not isinstance(pid, int) or pid <= 0:
            return False
        try:
            os.kill(pid, 0)
        except (ProcessLookupError, OSError):
            return False
        except PermissionError:
            return True
        return True

    def acquire(self) -> bool:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        for _ in range(2):
            try:
                with self.path.open("x", encoding="utf-8") as file:
                    json.dump({"pid": os.getpid()}, file)
                self.held = True
                return True
            except FileExistsError:
                try:
                    owner = json.loads(self.path.read_text(encoding="utf-8"))
                except (OSError, json.JSONDecodeError):
                    owner = {}
                if self._pid_is_running(owner.get("pid")):
                    return False
                try:
                    self.path.unlink()
                except FileNotFoundError:
                    pass
        return False

    def release(self) -> None:
        if self.held:
            try:
                self.path.unlink()
            except FileNotFoundError:
                pass
            self.held = False
