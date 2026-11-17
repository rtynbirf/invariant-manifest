# -*- coding: utf-8 -*-
# ORKESTRATOR FORK 3 · МАНИФЕСТ ИНВАРИАНТА · v0.2.3
# stdlib-only · детерминирован · запускается из любого cwd (пути от __file__)
#
# Правило агрегации (зафиксировано в контракте v0.2.3):
#   вердикт каждой трансформации = majority по 4 судьям
#   [MECHANICAL, R1, R2, R3]; при ничьей — более строгий вердикт.
#   вердикт предложения = худший вердикт по его трансформациям.
#   вердикт корпуса:
#     PASS    — все предложения SOFT;
#     FAIL    — ≥2 предложения BREAK или ≥25% трансформаций BREAK;
#     PARTIAL — иначе (есть дрейф или ровно 1 дефектное предложение).
#   Никакие ленты не переписываются под результат — история не удаляется.

import hashlib
import json
import sys
from pathlib import Path

PKG = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PKG / "scripts"))

import fork3_corpus  # noqa: E402
import fork3_judge_v023  # noqa: E402

DATA = PKG / "data"
SCORE = {"SOFT": 0, "DRIFT": 1, "BREAK": 2}
ORDER = ["T2a", "T2b", "T3"]


def sha256_of(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def worst(a: str, b: str) -> str:
    return a if SCORE[a] >= SCORE[b] else b


def majority(verdicts: list) -> str:
    counts = {}
    for v in verdicts:
        counts[v] = counts.get(v, 0) + 1
    best = max(counts.values())
    tops = [v for v, c in counts.items() if c == best]
    if len(tops) == 1:
        return tops[0]
    # ничья — строгость побеждает
    return tops[0] if SCORE[tops[0]] > SCORE[tops[1]] else tops[1]


def main() -> int:
    # 1. Свежий корпус + механический судья (всегда пересчитывается кодом).
    fork3_corpus.dump_json()
    mechanical = fork3_judge_v023.run()
    mech_path = DATA / "FORK3_MECHANICAL.json"
    mech_path.write_text(json.dumps(mechanical, ensure_ascii=False, indent=2), encoding="utf-8")

    corpus = json.loads((DATA / "FORK3_CORPUS.json").read_text(encoding="utf-8"))
    transforms = json.loads((DATA / "FORK3_TRANSFORMS.json").read_text(encoding="utf-8"))
    judges = {}
    for r in ("R1", "R2", "R3"):
        judges[r] = json.loads((DATA / f"FORK3_JUDGE_{r}.json").read_text(encoding="utf-8"))

    # 2. Агрегация.
    sentences = {}
    transforms_break = 0
    total_transforms = len(corpus) * len(ORDER)
    for c in corpus:
        cid = c["id"]
        mech_t = mechanical["результаты"][cid]
        j = {r: {v["id"]: v for v in judges[r]["verdicts"]}[cid] for r in ("R1", "R2", "R3")}
        per_transform = {}
        worst_t = "SOFT"
        for t in ORDER:
            verdicts = [mech_t[t]["verdict"]] + [j[r][t]["v"] for r in ("R1", "R2", "R3")]
            v = majority(verdicts)
            per_transform[t] = {
                "вердикт": v,
                "судьи": {
                    "MECHANICAL": mech_t[t]["verdict"],
                    "R1": j["R1"][t]["v"],
                    "R2": j["R2"][t]["v"],
                    "R3": j["R3"][t]["v"],
                },
                "примечание": next(
                    (x["note"] for x in (mech_t[t], j["R1"][t], j["R2"][t], j["R3"][t])
                     if x.get("note") and x.get("v", x.get("verdict")) == v),
                    "—",
                ),
            }
            worst_t = worst(worst_t, v)
            if v == "BREAK":
                transforms_break += 1
        sentences[cid] = {
            "категория": c["category"],
            "исходник": c["text"],
            "трансформации": per_transform,
            "вердикт": worst_t,
        }

    fail_sentences = [cid for cid, s in sentences.items() if s["вердикт"] == "BREAK"]
    drift_exists = any(
        t["вердикт"] == "DRIFT"
        for s in sentences.values()
        for t in s["трансформации"].values()
    ) or any(s["вердикт"] == "DRIFT" for s in sentences.values())
    share_break = transforms_break / total_transforms

    if not fail_sentences and not drift_exists and transforms_break == 0:
        verdict_corpus = "PASS"
    elif len(fail_sentences) >= 2 or share_break >= 0.25:
        verdict_corpus = "FAIL"
    else:
        verdict_corpus = "PARTIAL"

    # 3. Хеш-цепь (R-05: ничего не удаляется, всё подписывается).
    hashes = {
        "FORK3_CORPUS.json": sha256_of(DATA / "FORK3_CORPUS.json"),
        "FORK3_TRANSFORMS.json": sha256_of(DATA / "FORK3_TRANSFORMS.json"),
        "FORK3_MECHANICAL.json": sha256_of(mech_path),
        "FORK3_JUDGE_R1.json": sha256_of(DATA / "FORK3_JUDGE_R1.json"),
        "FORK3_JUDGE_R2.json": sha256_of(DATA / "FORK3_JUDGE_R2.json"),
        "FORK3_JUDGE_R3.json": sha256_of(DATA / "FORK3_JUDGE_R3.json"),
    }

    лента = {
        "лента": "FORK3_LENTA",
        "версия": "v0.2.3",
        "дата": "2026-11-18",
        "seed": 7170,
        "судьи": {
            "MECHANICAL": "CODE_INDEPENDENT (stdlib: Decimal, маркерные списки)",
            "R1": judges["R1"]["label_честности"],
            "R2": judges["R2"]["label_честности"],
            "R3": judges["R3"]["label_честности"],
        },
        "правило_агрегации": "majority по 4 судьям, ничья → строже; предложение = худшая трансформация",
        "результаты": sentences,
        "счётчик": {
            "предложений": len(corpus),
            "трансформаций_всего": total_transforms,
            "BREAK_трансформаций": transforms_break,
            "доля_BREAK": round(share_break, 4),
            "предложений_BREAK": len(fail_sentences),
        },
        "вердикт_корпуса": verdict_corpus,
        "статус_релиза": "CONDITIONAL PASS" if verdict_corpus != "PASS" else "PASS",
        "дефектный_регистр": [
            {
                "id": cid,
                "суть": "трансформация с BREAK зарегистрирована; лента не переписывается — исправление отдельной лентой в v0.2.4",
                "трансформации": [t for t, x in sentences[cid]["трансформации"].items() if x["вердикт"] == "BREAK"],
            }
            for cid in fail_sentences
        ],
        "хеши": hashes,
    }

    lentа_path = DATA / "FORK3_LENTA_v023.json"
    lentа_path.write_text(json.dumps(лента, ensure_ascii=False, indent=2), encoding="utf-8")

    # 4. Сводка (собирается кодом из ленты, не рукой).
    lines = [
        "# СВОДКА FORK 3 · v0.2.3",
        "",
        f"Вердикт корпуса: **{verdict_corpus}** (статус релиза: {лента['статус_релиза']})",
        "",
        "| Тезис | Категория | T2a | T2b | T3 | Вердикт |",
        "|---|---|---|---|---|---|",
    ]
    for cid in sorted(sentences):
        s = sentences[cid]
        t = s["трансформации"]
        lines.append(
            f"| {cid} | {s['категория']} | {t['T2a']['вердикт']} | {t['T2b']['вердикт']} | {t['T3']['вердикт']} | **{s['вердикт']}** |"
        )
    lines += [
        "",
        f"BREAK-трансформаций: {transforms_break} из {total_transforms} ({round(share_break * 100, 1)}%).",
        "",
        "## Дефектный регистр",
        "",
    ]
    if fail_sentences:
        for cid in fail_sentences:
            lines.append(f"- {cid}: " + "; ".join(
                f"{t} — {sentences[cid]['трансформации'][t]['примечание']}"
                for t in sentences[cid]["трансформации"] if sentences[cid]["трансформации"][t]["вердикт"] == "BREAK"
            ))
    else:
        lines.append("- пусто")
    lines += ["", "## Хеш-цепь", ""]
    for k, v in hashes.items():
        lines.append(f"- {k}: `{v[:16]}…`")

    (DATA / "SUMMARY_v023_FORK3.md").write_text("\n".join(lines), encoding="utf-8")

    # 5. Печать + код возврата.
    print(f"СУДЬИ: MECHANICAL(CODE) + R1(7170) + R2(7171) + R3(7172) · majority")
    for cid in sorted(sentences):
        s = sentences[cid]
        t = s["трансформации"]
        print(f"  {cid} [{s['категория']:>13}] T2a={t['T2a']['вердикт']:<6} T2b={t['T2b']['вердикт']:<6} T3={t['T3']['вердикт']:<6} → {s['вердикт']}")
    print(f"ВЕРДИКТ КОРПУСА: {verdict_corpus} · СТАТУС РЕЛИЗА: {лента['статус_релиза']}")
    print(f"ХЕШ-ЦЕПЬ: {len(hashes)} лент подписано · ЛЕНТА: {lentа_path.name}")
    return 0 if verdict_corpus != "FAIL" else 2


if __name__ == "__main__":
    sys.exit(main())
