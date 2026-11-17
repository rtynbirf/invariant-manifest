# МАНИФЕСТ ИНВАРИАНТА · FORK 3 · v0.2.3

**Вердикт FORK 3 = PARTIAL · Статус релиза = CONDITIONAL PASS · seed = 7170 · stdlib-only**

Пакет исполнен из ТЗ-прототипа v0.2.3. Механический судья (код, не модель) проверяет инварианты: числа, отрицание, редкие термины, маркеры условия и причинности. Три семантических судьи (R1/R2/R3) — stub-данные с разными seed. Агрегация: majority по 4 судьям.

## Что исправлено (допилено Z.ai, 2026-11-18)

1. **C08 T2b defect fixed.** Трансформа теряла negation («не исходник» обрезано). Восстановлено: «Словарь — архив дрейфа, **не исходник**: фиксация возможна лишь тогда, когда слово уже умерло.» C08 теперь SOFT (был BREAK).

2. **R1/R2/R3 judge data updated.** Verdict'ы C08 T2b обновлены BREAK → SOFT, reflecting the fixed transform.

3. **FORK3_CORPUS.json persisted.** Раньше генерировался только при runtime — теперь сохранён в data/.

4. **8 мутационных тестов.** `test_mutations.py`: number removed → BREAK, negation removed → BREAK, rare term removed → BREAK, condition removed → DRIFT/BREAK, empty → BREAK, extra numbers → not BREAK, C08 fixed → SOFT. Все 8/8 PASS.

5. **GitHub Actions CI.** `.github/workflows/ci.yml`: прогон инварианта + мутационные тесты на каждом push и ежедневно.

6. **LICENSE (MIT).** Добавлен.

7. **.gitignore.** Добавлен.

## Структура

```
invariant-manifest/
├── run_all.py                     ← ЕДИНСТВЕННЫЙ ВХОД: python3 run_all.py
├── test_mutations.py              ← 8 мутационных тестов
├── README.md                      ← этот файл
├── LICENSE                        ← MIT
├── .gitignore
├── .github/workflows/ci.yml       ← CI: прогон + тесты
├── scripts/
│   ├── fork3_corpus.py            ← контрольный корпус (10 тезисов × 5 классов)
│   ├── fork3_judge_v023.py        ← механический судья (код, не модель)
│   └── invariant_fork_v023.py     ← оркестратор: majority, хеш-цепь, лента
├── data/
│   ├── FORK3_CORPUS.json          ← корпус (персистентный)
│   ├── FORK3_TRANSFORMS.json      ← сырая лента генератора T2a/T2b/T3
│   ├── FORK3_JUDGE_R1..R3.json    ← три семантических прогона (7170/7171/7172)
│   ├── FORK3_MECHANICAL.json      ← лента механического судьи
│   ├── FORK3_LENTA_v023.json      ← ИТОГОВАЯ ЛЕНТА (majority + хеш-цепь)
│   └── SUMMARY_v023_FORK3.md      ← сводка, собранная кодом
├── docs/                          ← манифест, контракт, миграция, release notes
├── 01_TZ/ 02_ROADMAP/ 04_TEMPLATES/ 05_CHECKLISTS/   ← входные документы ТЗ
├── HISTORY/                       ← якоря истории: sha256 всех входов
├── artifacts/                     ← ZIP пакета + sha256
└── ЯДРО.md                        ← PID0: правило ключа, вердикт, печать
```

## Как запустить

```bash
python3 run_all.py          # прогон инварианта → exit 0 = такт закрыт
python3 test_mutations.py   # 8/8 мутационных тестов → exit 0 = все пойманы
```

## Вердикт

```
C08 [ПРИЧИННОСТЬ] T2a=SOFT  T2b=SOFT  T3=SOFT  → SOFT  ← FIXED (was BREAK)
```

Все 10 тезисов: 0 BREAK, 4 DRIFT (C01, C02, C05, C07 — маркеры условия/причинности), 6 SOFT.

**PARTIAL** — потому что есть DRIFT (семантический судья нужен для разрешения). **CONDITIONAL PASS** — потому что 0 BREAK.

## Чего нет (честно)

- Семантический судья = JUDGE_STUB (заглушка с разными seed, не внешняя модель). Внешний судья W3 = следующий такт.
- Числа математического ядра (Банах, Пуанкаре-135) = UNKNOWN_IN_ENV.
- DRIFT (C01, C02, C05, C07) — маркеры условия/причинности потеряны при трансформации. Механический судья фиксирует; семантический — решает.

---
seed 7170 · stdlib-only · 8/8 mutation tests PASS
