# БРИФ SWEEP · TAKT v0.2.9 · РЕЕСТР → АУДИТ → ПАСПОРТА ДЛЯ ДОМЕНОВ B–J + X

Ты — агент sweep фаланги такта v0.2.9. Дом A (001–100 + 1001–1020) пропаспортирован. Твой участок: построить нормализованный реестр своего диапазона с самоаудитом и паспортными полями. Реестр — сердце; паспорта дома отрендерит машина.

## ВХОД (обязателен к прочтению)
1. `/home/z/my-project/work/passports/_data/BRIEF.md` — формат паспорта и законы честности дома (секции, ВЕРДИКТ, «(оценка INIT)»).
2. `/home/z/my-project/work/atlas/registry_a/GLOBAL_PRACTICE_ATLAS_2026.md` — SSOT каталога: твой диапазон, темы домена, известные ID из кластеров, методология (разделы 2, 5, 6).

## ТВОЙ ДИАПАЗОН И ТЕМЫ (из атласа, раздел 2)

| Домен | Диапазон | Темы |
|---|---|---|
| B | 101–200 | Наука, инженерия, производство: Open Science, Materials, Additive Manufacturing, Biotech |
| C | 201–300 | Экономика, управление, кооперация: Circular Economy, Sociocracy, Supply Chain Resilience |
| D | 301–400 | Образование, мышление, творчество: Lifelong Learning, Metacognition, Human-AI Co-Creation |
| E | 401–500 | Экология, энергия, здоровье, города: Nature-Based Solutions, Microgrids, Regenerative Design |
| F | 501–600 | Космос, логистика, риски, право: ISRU, Physical Internet, Legal Tech, Skills-Based Hiring |
| G | 601–700 | Нейронауки, сложные системы, биология: Connectomics, Complex Adaptive Systems, Soft Robotics |
| H | 701–800 | Теория знания, математика, эпистемология: AIT, Formal Methods, Knowledge Graphs |
| I | 801–900 | Робототехника, материалы, энергия, независимость: Multi-Robot, Metamaterials, Local-First, Graceful Degradation |
| J | 901–1000 | Целостные системы, автономность, устойчивость: Systems-of-Systems, Bounded Autonomy, Resilience Engineering |
| X | 1021–1045 | Кросс-доменные добавления 2026 — все 25 позиций УЖЕ НАЗВАНЫ в атласе (разделы 3.2–3.4): возьми имена/типы/зрелость оттуда и заземли поиском |

## ИЗВЕСТНЫЕ ID (якоря кластеров атласа — сохрани их смысл, ID фиксированы)
- E: 423–425 = Community Energy + Microgrids
- F: 582 = Formal Verification
- I: 801–803 = Multi-Robot/Swarm · 806–807 = Sim-to-Real + Domain Randomization · 809 = Embodied AI · 870 = Personal Computing Sovereignty · 871–872 = Local-First + Offline-First · 880 = Graceful Degradation
- J: 915 = Runtime Verification · 923, 940 = Bounded Autonomy + Override · 971 = Resilience Engineering · 982 = Claim-Evidence Graphs · 989 = Independent Replication

## ИССЛЕДОВАНИЕ (WebSearch)
- 5–10 поисков на домен (запросы на английском: тема + "2025" / "2026" / "best practices" / "adoption").
- Источник имеет право появиться в evidence ТОЛЬКО если ты реально видел его: в атласе или в результатах WebSearch (называй домен: iea.org, nature.com, gartner.com…).
- Не нашёл источника для позиции → evidence_level = "UNKNOWN". Явный UNKNOWN = добродетель, выдуманный источник = смерть партии.
- Числа — только реально увиденные, с источником в поле effect_numbers.

## ВЫХОД — ОДИН JSON-ФАЙЛ
`/home/z/my-project/work/atlas/sweep/DOMAIN_<буква>.json` — массив из N позиций (B–J: ровно 100, X: ровно 25), ID подряд без пропусков:

```json
{
 "id": 101,
 "name_en": "Open Peer Review",
 "name_ru": "Открытое рецензирование",
 "type": "Практика | Технология | Метод | Архитектура | Принцип | Стандарт | Организационная модель | Система | Инфраструктура | Паттерн",
 "subdomain": "короткое слово латиницей (как в домене A: Agents, Security, Data…)",
 "relations": "RELATED:102; PART-OF:Open Science (может быть пусто → «—»)",
 "maturity_2026": "Research | Experimental | Deployed | Mainstream | Experimental→Deployed | Deployed→Mainstream | Research→Experimental",
 "evidence_level": "High (iea.org) | Medium | Low | UNKNOWN",
 "priority": "Critical | High | Medium | Low",
 "notes": "2–4 предложения по-русски: что это, как применяется, почему значимо в 2025–2026. Без выдуманных чисел.",
 "verdict": "KEEP | KEEP (эвиденция UNKNOWN)",
 "effect_numbers": "только если нашёл числа: «<числа> — источник: <домен>» иначе пропусти поле",
 "passport": {
   "conditions": "2–4 предложения: когда/где/для кого (≥120 символов)",
   "metrics": ["что мерить 1", "что мерить 2", "что мерить 3"],
   "limits": ["ограничение 1", "ограничение 2", "ограничение 3 (выводы из общих знаний помечай «(оценка INIT)»)"],
   "cost": "оценка INIT: S|M|L — обоснование в 1 строку (от зрелости и типа)",
   "repro": "Как проверить у себя: 1–2 конкретных шага"
 }
}
```

## ЗАКОНЫ ЧЕСТНОСТИ
1. ID подряд: B=101…200, C=201…300, D=301…400, E=401…500, F=501…600, G=601…700, H=701…800, I=801…900, J=901…1000, X=1021…1045. Не выдумывать новые диапазоны.
2. Источники — только увиденные (атлас / WebSearch). Числа — только с источником. Иначе UNKNOWN.
3. Русский язык контента; имена собственные/стандарты — латиницей. Без эмодзи, TODO, XXX, 【】, «…».
4. relations — из словаря дома: SAME / IS-A / PART-OF / RELATED / COMPLEMENTARY; связывай внутри диапазона и с доменом A осмысленно, минимум треть позиций с непустым relations.
5. Проверь свой JSON перед сдачей: длина массива ровно N, ID подряд, у всех passport.conditions ≥120 символов, metrics ровно 3, limits ≥2.
6. Финальное сообщение: путь файла, число позиций, сколько позиций с реальными источниками vs UNKNOWN, какие 2–3 позиции самые слабые по данным.
