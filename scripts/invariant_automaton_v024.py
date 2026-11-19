# -*- coding: utf-8 -*-
# АВТОМАТ ТАКТА · МАНИФЕСТ ИНВАРИАНТА · v0.2.4
# КОНЕЧНЫЙ АВТОМАТ = МЕХАНИЗМ, НЕ ДЕКЛАРАЦИЯ:
#   состояния + охраны + ТАБЛИЦА ПЕРЕХОДОВ (Harel/statecharts) + лента автомата.
# Тренды, вобранные в механизм: декларативная таблица переходов; двойной чистый
# прогон + сверка хешей (reproducible builds); проверки на каждом переходе.
# stdlib-only. Запуск из любого cwd: python3 scripts/invariant_automaton_v024.py
# EXIT 0 = CLOSED · EXIT 2 = FAIL

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

LENTA = "FORK3_LENTA_v023.json"

# ТАБЛИЦА ПЕРЕХОДОВ: состояние -> {охрана: (следующее_состояние, смысл)}
TABLE = {
    "BOOT":    {"ok": ("SEAL",    "корень найден: run_all.py + scripts/ на месте"),
               "no": ("FAIL",     "корень не похоже на ядро")},
    "SEAL":    {"ok": ("RUN_R1",  "печать артефакта цела (или отсутствует = честный пропуск)"),
               "no": ("FAIL",     "печать не совпала с якорем")},
    "RUN_R1":  {"ok": ("RUN_R2",  "чистый прогон 1: exit 0"),
               "no": ("FAIL",     "чистый прогон 1 упал")},
    "RUN_R2":  {"ok": ("COMPARE", "чистый прогон 2: exit 0"),
               "no": ("FAIL",     "чистый прогон 2 упал")},
    "COMPARE": {"ok": ("CHAIN",   "хеши ленты двух прогонов равны = детерминизм"),
               "no": ("FAIL",     "хеши разошлись = недетерминизм")},
    "CHAIN":   {"ok": ("VERDICT", "хеш-цепь ленты цела"),
               "no": ("FAIL",     "хеш-цепь разорвана")},
    "VERDICT": {"ok": ("TAPE",    "вердикт корпуса не FAIL"),
               "no": ("FAIL",     "вердикт корпуса FAIL")},
    "TAPE":    {"ok": ("CLOSED",  "лента автомата записана и подписана"),
               "no": ("FAIL",     "лента не записалась")},
}
FINAL = ("CLOSED", "FAIL")


def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def act_boot(ctx):
    ok = (ctx["root"] / "run_all.py").is_file() and (ctx["root"] / "scripts").is_dir()
    return ("ok" if ok else "no", "root=" + str(ctx["root"]))


def act_seal(ctx):
    zp = ctx["root"] / "artifacts" / "INVARIANT_v0.2.3_FORK3_PACKAGE.zip"
    sp = ctx["root"] / "artifacts" / "INVARIANT_v0.2.3_FORK3_PACKAGE.zip.sha256"
    if not zp.is_file():
        ctx["seal"] = "absent"
        return ("ok", "печати нет = пропуск (запуск не из ядра)")
    expected = sp.read_text().split()[0]
    actual = sha256_file(zp)
    ctx["seal"] = actual
    return ("ok" if actual == expected else "no",
            "печать " + actual[:8] + "…" + actual[-6:] + (" = цела" if actual == expected else " ≠ " + expected[:8] + "…"))


def make_act_run(n):
    def act(ctx):
        t = Path(tempfile.mkdtemp(prefix="automaton_r" + str(n) + "_"))
        shutil.copytree(ctx["root"], t / "repo", ignore=shutil.ignore_patterns(".git", "artifacts", "__pycache__"))
        try:
            r = subprocess.run([sys.executable, "run_all.py"], cwd=str(t / "repo"),
                               capture_output=True, text=True, timeout=300)
            code = r.returncode
        except subprocess.TimeoutExpired:
            code = -1
        lp = t / "repo" / "data" / LENTA
        h = sha256_file(lp) if lp.is_file() else None
        ctx["temps"][n] = t
        ctx["hashes"][n] = h
        guard = "ok" if code == 0 and h else "no"
        return (guard, "прогон " + str(n) + ": exit=" + str(code) +
                (" лента " + h[:8] + "…" + h[-6:] if h else " лента не создана"))
    return act


def act_compare(ctx):
    h1, h2 = ctx["hashes"].get(1), ctx["hashes"].get(2)
    ok = h1 is not None and h1 == h2
    return ("ok" if ok else "no",
            ("хеш ленты неподвижен: " + h1[:8] + "…" + h1[-6:] if ok else "run1=" + str(h1) + " run2=" + str(h2)))


def act_chain(ctx):
    d = json.load(open(ctx["temps"][1] / "repo" / "data" / LENTA, encoding="utf-8"))
    ctx["lenta"] = d
    chain = d.get("хеши", {})
    checked = skipped = 0
    for fname, expected in chain.items():
        if fname == LENTA:
            skipped += 1  # самоссылка невозможна по построению
            continue
        p = ctx["temps"][1] / "repo" / "data" / fname
        if not p.is_file():
            return ("no", "в цепи есть файл, которого нет: " + fname)
        if sha256_file(p) != expected:
            return ("no", "цепь разорвана на: " + fname)
        checked += 1
    return ("ok" if checked > 0 else "no",
            "цепь проверена: " + str(checked) + " звеньев цело" + (" (самоссылка пропущена: " + str(skipped) + ")" if skipped else ""))


def act_verdict(ctx):
    d = ctx["lenta"]
    verdict = d.get("вердикт_корпуса", "FAIL")
    status = d.get("статус_релиза", "—")
    ctx["verdict"] = verdict
    ctx["status"] = status
    return ("ok" if verdict != "FAIL" else "no",
            "вердикт=" + str(verdict) + " · статус=" + str(status))


def act_tape(ctx):
    hops = ctx["hops"]
    final = ctx["final"]
    tape = {
        "лента": "AUTOMATON_TAPE",
        "версия": "v0.2.4",
        "автомат": "конечный автомат такта: состояния + охраны + таблица переходов",
        "состояний_всего": len(set(TABLE) | set(FINAL)),
        "переходов_пройдено": len(hops) + 1,
        "финал": final,
        "вердикт_корпуса": ctx.get("verdict", "—"),
        "статус_релиза": ctx.get("status", "—"),
        "детерминизм": (ctx["hashes"].get(1) == ctx["hashes"].get(2) and ctx["hashes"].get(1) is not None),
        "лента_хеш": ctx["hashes"].get(1),
        "печать_артефакта": ctx.get("seal", "absent"),
        "хопы": hops,
        "подпись": hashlib.sha256(json.dumps(hops, sort_keys=True, ensure_ascii=False).encode()).hexdigest(),
    }
    out = ctx["root"] / "data" / "AUTOMATON_TAPE_v024.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(tape, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return ("ok", "лента автомата: data/AUTOMATON_TAPE_v024.json")


ACTIONS = {
    "BOOT": act_boot,
    "SEAL": act_seal,
    "RUN_R1": make_act_run(1),
    "RUN_R2": make_act_run(2),
    "COMPARE": act_compare,
    "CHAIN": act_chain,
    "VERDICT": act_verdict,
    "TAPE": act_tape,
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=str(Path(__file__).resolve().parent.parent))
    args = ap.parse_args()
    root = Path(args.root).resolve()
    ctx = {"root": root, "temps": {}, "hashes": {}, "hops": [], "final": None}

    print("АВТОМАТ ТАКТА · v0.2.4 · конечный автомат: 10 состояний · 8 переходов · 2 финала")
    print("=" * 68)
    state = "BOOT"
    while state not in FINAL:
        guard, obs = ACTIONS[state](ctx)
        nxt, meaning = TABLE[state][guard]
        ctx["hops"].append({"из": state, "охрана": guard, "в": nxt, "факт": obs})
        print("%-8s --[%s]--> %-8s %s" % (state, guard, nxt, obs))
        if nxt == "FAIL":
            ctx["final"] = "FAIL"
            break  # FAIL не в TABLE: терминальный, лента пишется ниже
        state = nxt
    if ctx["final"] is None:
        ctx["final"] = state  # CLOSED пришёл через TABLE (из TAPE)
    # финальная запись ленты даже при FAIL (R-05: ошибка = свидетель)
    if ctx["final"] == "FAIL":
        ok_tape = False
        try:
            hops = ctx["hops"]
            tape = {"лента": "AUTOMATON_TAPE", "версия": "v0.2.4", "финал": "FAIL",
                    "хопы": hops,
                    "подпись": hashlib.sha256(json.dumps(hops, sort_keys=True, ensure_ascii=False).encode()).hexdigest()}
            out = ctx["root"] / "data" / "AUTOMATON_TAPE_v024.json"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(json.dumps(tape, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            ok_tape = True
        except Exception:
            pass
        print("=" * 68)
        print("АВТОМАТ: FAIL · " + ("лента-свидетель записана" if ok_tape else "лента не записалась"))
        return 2

    print("=" * 68)
    print("АВТОМАТ: CLOSED · ТАКТ ЗАКРЫТ · ЛЕНТА АВТОМАТА ПОДПИСАНА")
    return 0


if __name__ == "__main__":
    sys.exit(main())
