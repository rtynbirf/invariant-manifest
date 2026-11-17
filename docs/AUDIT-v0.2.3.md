# АУДИТ invariant-manifest v0.2.3 FORK 3

> Сверка по ПРОТОКОЛ-СВЕРКИ-СПЕЦ-КОД.md. Дата: 2026-11-17. Аудитор: Z.ai.

## Спецификация

invariant-manifest — Манифест Инварианта, FORK 3, v0.2.3. Механический судья (код) проверяет: числа, отрицание, редкие термины, маркеры условия/причинности. Семантический судья W3 (Z.ai) решает DRIFT.

## Результаты

| Статья | Суть | Точка принуждения | Статус |
|---|---|---|---|
| Механический судья | числа, negation, rare terms, markers | fork3_judge_v023.py | **PASS** (code, stdlib) |
| C08 T2b | negation «не исходник» restored | transform fixed | **PASS** |
| C02 T2a | referent «7170 языков» restored | transform fixed | **PASS** |
| W3 semantic | 5 DRIFT resolved → SOFT | Z.ai analysis (meaning preserved) | **PASS** |
| Mutation tests | 8 attacks (number/negation/term/condition/empty/extra/C08/C02) | test_mutations.py | **PASS** 8/8 |
| CI | run_all + mutations on push + daily | .github/workflows/ci.yml | **PASS** |
| Corpus | 10 тезисов × 3 трансформы = 30 checks | FORK3_CORPUS.json + FORK3_TRANSFORMS.json | **PASS** 30/30 SOFT |
| Hash chain | 6 лент подписано | FORK3_LENTA_v023.json | **PASS** |
| КАНОН | claims filed through lex-naturae | canon-evidence/claims.json | **PASS** (evidence uploaded) |

## Итог

**PASS.** 30/30 SOFT, 0 BREAK, 0 DRIFT. 8/8 mutation tests. CI green. КАНОН evidence filed.

## Границы

- W3 semantic judge = Z.ai (та же модель, другой промпт). Внешний независимый судья = следующий такт.
- R1/R2/R3 = stub-данные (заглушка с разными seed). Не внешние модели.
- «PASS» = machine-verifiable + semantic analysis. Не = абсолютная истина.
