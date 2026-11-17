# -*- coding: utf-8 -*-
# FORK 3 · МЕХАНИЧЕСКИЙ СУДЬЯ
# Манифест Инварианта · v0.2.3 · stdlib-only
#
# Независимость от генератора: другой код, другая арифметика (Decimal), никаких
# весов и семантики — только маркеры и числа. Семантика решается отдельными
# прогонами (R1/R2/R3), эта машина фиксирует только механические следы.
#
# Правила вердиктов:
#   BREAK — число потеряно/изменено; редкий термин потерян; отрицание
#           (полярность) потеряно.
#   DRIFT — маркер условия/причинности отсутствует (отношение могло
#           сохраниться лексикой — решает семантический судья).
#   SOFT  — все механические инварианты на месте.

import json
import re
import unicodedata
from decimal import Decimal, InvalidOperation
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"

NEGATION_TOKENS = ["не", "нет", "ни", "нельзя", "ничего", "никогда", "а не"]
CONDITION_TOKENS = ["пока", "если", "без", "когда", "после", "до", "лишь", "тогда", "прежде", "как только"]
CAUSALITY_TOKENS = ["потому", "поэтому", "значит", "ибо", "из-за", "так как", "следствие", "отсюда"]


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKC", text).lower().replace("ё", "е")
    text = re.sub(r"\s+", " ", text)
    return text


def has_number(text: str, expected: str) -> bool:
    """Число считается сохранённым, если встречается ровно (запятая=точка)."""
    t = normalize(text)
    variants = {
        expected,
        expected.replace(".", ","),
    }
    for v in variants:
        if re.search(r"(?<![\d.])" + re.escape(v) + r"(?![\d])", t):
            return True
    return False


def token_count(text: str, tokens) -> int:
    t = normalize(text)
    n = 0
    for tok in tokens:
        if tok == "не":
            n += len(re.findall(r"(?<![\w-])не(?![\w-])", t))
        elif tok == "ни":
            n += len(re.findall(r"(?<![\w-])ни(?![\w-])", t))
        else:
            n += len(re.findall(re.escape(normalize(tok)), t))
    return n


def check_transform(source: dict, transformed: str) -> dict:
    checks = {}
    # 1. Числа — критично.
    for num in source["numbers"]:
        ok = has_number(transformed, num)
        checks[f"число {num}"] = "SOFT" if ok else "BREAK"
    # 2. Редкие термины — критично. Мягкие термины (заменяемые перефразом
    #    без потери референта) — только DRIFT.
    for term in source.get("rare_terms", []):
        ok = normalize(term) in normalize(transformed)
        checks[f"термин «{term}»"] = "SOFT" if ok else "BREAK"
    for term in source.get("soft_terms", []):
        ok = normalize(term) in normalize(transformed)
        checks[f"мягкий термин «{term}»"] = "SOFT" if ok else "DRIFT"
    # 3. Отрицание — критично (полярность).
    if source["negation"]:
        src_n = token_count(source["text"], NEGATION_TOKENS)
        dst_n = token_count(transformed, NEGATION_TOKENS)
        if src_n > 0 and dst_n == 0:
            checks["отрицание"] = "BREAK"
        elif dst_n == 0:
            checks["отрицание"] = "BREAK"
        else:
            checks["отрицание"] = "SOFT"
    # 4. Условие — маркер.
    if source["condition"]:
        src_c = token_count(source["text"], CONDITION_TOKENS)
        dst_c = token_count(transformed, CONDITION_TOKENS)
        checks["условие (маркер)"] = "SOFT" if (src_c == 0 or dst_c > 0) else "DRIFT"
    # 5. Причинность — маркер.
    if source["causality"]:
        src_c = token_count(source["text"], CAUSALITY_TOKENS)
        dst_c = token_count(transformed, CAUSALITY_TOKENS)
        checks["причинность (маркер)"] = "SOFT" if (src_c == 0 or dst_c > 0) else "DRIFT"

    if any(v == "BREAK" for v in checks.values()):
        verdict = "BREAK"
    elif any(v == "DRIFT" for v in checks.values()):
        verdict = "DRIFT"
    else:
        verdict = "SOFT"
    return {"verdict": verdict, "checks": checks}


def run() -> dict:
    corpus = json.loads((DATA / "FORK3_CORPUS.json").read_text(encoding="utf-8"))
    transforms = json.loads((DATA / "FORK3_TRANSFORMS.json").read_text(encoding="utf-8"))["трансформации"]
    by_id = {t["id"]: t for t in transforms}

    results = {}
    for c in corpus:
        t = by_id[c["id"]]
        results[c["id"]] = {
            key: check_transform(c, t[key]) for key in ("T2a", "T2b", "T3")
        }
    return {
        "лента": "FORK3_MECHANICAL",
        "судья": "CODE_INDEPENDENT (stdlib, Decimal, маркерные списки — не модель)",
        "детерминизм": True,
        "результаты": results,
    }


if __name__ == "__main__":
    out = run()
    path = DATA / "FORK3_MECHANICAL.json"
    path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print("MECHANICAL →", path)
