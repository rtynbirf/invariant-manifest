# -*- coding: utf-8 -*-
# RUN_ALL · МАНИФЕСТ ИНВАРИАНТА · v0.2.3 FORK 3
# Один вход: python3 run_all.py (из любого cwd).

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CORE = HERE / "scripts" / "invariant_fork_v023.py"

if __name__ == "__main__":
    print("МАНИФЕСТ ИНВАРИАНТА · FORK 3 · v0.2.3 · seed=7170 · stdlib-only")
    print("=" * 68)
    rc = subprocess.run([sys.executable, str(CORE)]).returncode
    print("=" * 68)
    print("ТАКТ ЗАКРЫТ · ЛЕНТЫ ПОДПИСАНЫ · ИСТОРИЯ ЦЕЛА" if rc == 0 else "FAIL-РЕЖИМ: смотри дефектный регистр")
    sys.exit(rc)
