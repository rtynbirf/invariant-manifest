# -*- coding: utf-8 -*-
# FORK 3 · КОНТРОЛЬНЫЙ КОРПУС
# Манифест Инварианта · v0.2.3 · stdlib-only · seed = 7170
#
# Источник каждой строки = живой диалог проекта (не словарный бинарник).
# Категории проверок: число / отрицание / условие / причинность / редкий термин.
# rare_terms = критичные термины (потеря = BREAK).
# soft_terms = мягкие термины (потеря термина при сохранении референта = DRIFT).

import json
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"

# Каждая строка: id, текст, категории (применяемые проверки), числа, термины.
CORPUS = [
    {
        "id": "C01",
        "category": "ЧИСЛО",
        "text": "Золотое сечение = 1,618, а не 0,5: равновесие живых смещено от половины.",
        "numbers": ["1.618", "0.5"],
        "rare_terms": [],
        "soft_terms": ["золотое сечение"],
        "negation": True,
        "condition": False,
        "causality": False,
    },
    {
        "id": "C02",
        "category": "ЧИСЛО",
        "text": "7170 языков планеты = один человек: языков миллионы, сущность одна.",
        "numbers": ["7170"],
        "rare_terms": [],
        "soft_terms": [],
        "negation": False,
        "condition": False,
        "causality": False,
    },
    {
        "id": "C03",
        "category": "ОТРИЦАНИЕ",
        "text": "Носитель смертен, а смысл в слове нет.",
        "numbers": [],
        "rare_terms": [],
        "soft_terms": [],
        "negation": True,
        "condition": False,
        "causality": False,
    },
    {
        "id": "C04",
        "category": "ОТРИЦАНИЕ",
        "text": "Голова не хранит — голова бросает вперёд.",
        "numbers": [],
        "rare_terms": [],
        "soft_terms": [],
        "negation": True,
        "condition": False,
        "causality": False,
    },
    {
        "id": "C05",
        "category": "УСЛОВИЕ",
        "text": "Проекция без прогона — вера; проекция после прогона — знание.",
        "numbers": [],
        "rare_terms": [],
        "soft_terms": [],
        "negation": False,
        "condition": True,
        "causality": False,
    },
    {
        "id": "C06",
        "category": "УСЛОВИЕ",
        "text": "Пока хозяин не назвал задачу, init принадлежит тишине.",
        "numbers": [],
        "rare_terms": ["init"],
        "soft_terms": [],
        "negation": True,
        "condition": True,
        "causality": False,
    },
    {
        "id": "C07",
        "category": "ПРИЧИННОСТЬ",
        "text": "Зло = невежество: невежда опаснее злодея, потому что злодей хоть знает, что творит.",
        "numbers": [],
        "rare_terms": [],
        "soft_terms": [],
        "negation": False,
        "condition": False,
        "causality": True,
    },
    {
        "id": "C08",
        "category": "ПРИЧИННОСТЬ",
        "text": "Слово попадает в словарь, когда умирает настолько, что фиксация безопасна: словарь — архив дрейфа, не исходник.",
        "numbers": [],
        "rare_terms": [],
        "soft_terms": [],
        "negation": True,
        "condition": True,
        "causality": True,
    },
    {
        "id": "C09",
        "category": "РЕДКИЙ ТЕРМИН",
        "text": "Дяхан — язык, собранный из прожитых корней, — не фиксируют: им пользуются.",
        "numbers": [],
        "rare_terms": ["дяхан"],
        "soft_terms": [],
        "negation": True,
        "condition": False,
        "causality": False,
    },
    {
        "id": "C10",
        "category": "РЕДКИЙ ТЕРМИН",
        "text": "Уанрок — один камень с меткой: первый жетон долга, из которого выросла клинопись.",
        "numbers": [],
        "rare_terms": ["уанрок", "клинопись"],
        "soft_terms": [],
        "negation": False,
        "condition": False,
        "causality": True,
    },
]


def dump_json() -> Path:
    DATA.mkdir(parents=True, exist_ok=True)
    path = DATA / "FORK3_CORPUS.json"
    path.write_text(
        json.dumps(CORPUS, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return path


if __name__ == "__main__":
    print("CORPUS:", len(CORPUS), "предложений →", dump_json())
