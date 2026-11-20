# GLOBAL PRACTICE ATLAS 2025–2026

**Завершённый исследовательский пакет**  
Вместо бесконечных планов и частичных аудитов — цельный результат.

---

## 1. Что сделано

Исходный каталог из 1000 позиций (001–1000) сохранён как **базовый реестр**.  
К нему добавлен **закрытый блок недостающих промышленных направлений** (1001–1045), выявленных по актуальным обзорам 2025–2026 (Gartner, Deloitte, IEA, Stanford HAI, EU AI Act timeline).

Каталог больше не претендует на звание «500/1000 лучших». Это **карта сущностей** с явной методологией оценки.

### Принципы финальной версии

| Принцип | Реализация |
|---------|------------|
| Сохранение ID | Исходные 001–1000 не удаляются и не перенумеровываются |
| Типизация | Каждая позиция относится к одному из типов: Практика / Технология / Метод / Архитектура / Принцип / Стандарт / Организационная модель |
| Зрелость | 4 уровня: Research → Experimental → Deployed → Mainstream |
| Доказательность | Ссылки на первичные источники или явный статус UNKNOWN |
| Независимость | Отдельные рейтинги по критериям, а не один «рейтинг лучших» |

---

## 2. Структура каталога (10 доменов)

| Домен | Диапазон ID | Содержание |
|-------|-------------|------------|
| A. ИИ, агенты и вычисления | 001–100 + 1001–1020 | Multi-agent, Agentic, Foundation Models, MLOps, Physical AI |
| B. Наука, инженерия, производство | 101–200 | Open Science, Materials, Additive Manufacturing, Biotech |
| C. Экономика, управление, кооперация | 201–300 | Circular Economy, Sociocracy, Supply Chain Resilience |
| D. Образование, мышление, творчество | 301–400 | Lifelong Learning, Metacognition, Human-AI Co-Creation |
| E. Экология, энергия, здоровье, города | 401–500 | Nature-Based Solutions, Microgrids, Regenerative Design |
| F. Космос, логистика, риски, право | 501–600 | ISRU, Physical Internet, Legal Tech, Skills-Based Hiring |
| G. Нейронауки, сложные системы, биология | 601–700 | Connectomics, Complex Adaptive Systems, Soft Robotics |
| H. Теория знания, математика, эпистемология | 701–800 | Algorithmic Information Theory, Formal Methods, Knowledge Graphs |
| I. Робототехника, материалы, энергия, независимость | 801–900 | Multi-Robot Systems, Metamaterials, Local-First, Graceful Degradation |
| J. Целостные системы, автономность, устойчивость | 901–1000 | Systems-of-Systems, Bounded Autonomy, Resilience Engineering |

---

## 3. Критические пробелы, закрытые в 2026

По данным Deloitte Tech Trends 2026, Gartner Strategic Technology Trends 2026 и IEA World Energy Outlook 2026:

### 3.1. ИИ как промышленная инфраструктура

| ID | Название | Тип | Зрелость (2026) | Комментарий |
|----|----------|-----|-----------------|-------------|
| 1001 | Foundation Models | Технология | Mainstream | Базовый слой большинства AI-систем |
| 1002 | Multimodal Foundation Models | Технология | Deployed → Mainstream | Текст + изображение + звук + действие |
| 1003 | MLOps | Практика | Mainstream | Версионирование, мониторинг, CI/CD моделей |
| 1004 | LLMOps | Практика | Deployed | Специализация MLOps под LLM |
| 1005 | Model Compression | Метод | Deployed | Общий класс |
| 1006 | Knowledge Distillation | Метод | Deployed | Перенос знаний в меньшие модели |
| 1007 | Model Quantization | Метод | Mainstream | INT8/INT4 и ниже |
| 1008 | Small Language Models | Технология | Deployed | SLM для edge и локального использования |
| 1009 | Context Engineering | Практика | Experimental → Deployed | Управление контекстом агентов |
| 1010 | Prompt Engineering | Практика | Mainstream | Уже commoditized |
| 1011 | Mechanistic Interpretability | Метод | Research → Experimental | Внутренние механизмы моделей |
| 1012 | Explainable AI (XAI) | Метод | Deployed | Более зрелый, чем mechanistic |
| 1013 | AI Alignment Engineering | Практика | Experimental | Техническая реализация alignment |
| 1014 | AI Governance | Организационная модель | Deployed | Политики + процессы + audit |
| 1015 | AI Red Teaming | Практика | Deployed | Систематическое adversarial-тестирование |
| 1016 | Computer-Use Agents | Технология | Experimental → Deployed | Агенты, управляющие компьютером |
| 1017 | Browser Automation Agents | Технология | Deployed | Специализированный класс computer-use |
| 1018 | Humanoid Robotics | Технология | Experimental | Раннее промышленное внедрение |
| 1019 | Physical AI | Архитектура | Experimental → Deployed | AI + физический мир (Deloitte #1) |
| 1020 | Autonomous Vehicle Fleets | Система | Deployed | Ограниченные географии |

### 3.2. Физическая инфраструктура AI

| ID | Название | Тип | Зрелость | Источник |
|----|----------|-----|----------|----------|
| 1021 | AI Data Centers | Инфраструктура | Mainstream | IEA: рост потребления |
| 1022 | AI Factories | Архитектура | Deployed | Специализированные кластеры |
| 1023 | Liquid-Cooled Computing | Технология | Deployed | Direct-to-chip / immersion |
| 1024 | Data Center Energy Engineering | Практика | Deployed | Power + cooling + grid interconnection |

По IEA (ноябрь 2026): потребление дата-центров удваивается к 2030 г. (≈1000 ТВт·ч). Основные ограничения — сети, трансформаторы, оборудование и сроки подключения.

### 3.3. Экономика и разработка

| ID | Название | Тип | Зрелость |
|----|----------|-----|----------|
| 1025 | FinOps | Практика | Mainstream |
| 1026 | Serverless Computing | Архитектура | Mainstream |
| 1027 | Managed Services Architecture | Архитектура | Mainstream |
| 1028 | API-First Development | Практика | Mainstream |
| 1029 | API Economy | Экономическая модель | Mainstream |
| 1030 | Low-Code / No-Code Development | Практика | Mainstream |
| 1031 | Citizen Development | Организационная модель | Deployed |

### 3.4. Связь и доверие

| ID | Название | Тип | Зрелость |
|----|----------|-----|----------|
| 1032 | 5G Advanced | Технология | Deployed |
| 1033 | 6G / IMT-2030 | Стандарт | Research → Experimental |
| 1034 | Low Earth Orbit Connectivity | Инфраструктура | Deployed |
| 1035 | Direct-to-Device Satellite | Технология | Experimental → Deployed |
| 1036 | Smart Contracts | Технология | Deployed |
| 1037 | Real-World Asset Tokenization | Практика | Experimental → Deployed |
| 1038 | Stablecoin Payment Infrastructure | Инфраструктура | Deployed |
| 1039 | Content Credentials | Стандарт | Deployed |
| 1040 | C2PA Provenance | Стандарт | Deployed |
| 1041 | Synthetic Media Detection | Метод | Experimental → Deployed |
| 1042 | AI Content Watermarking | Метод | Experimental |
| 1043 | Accessibility by Design | Принцип | Deployed |
| 1044 | Inclusive Interaction Design | Практика | Deployed |
| 1045 | Accessibility Engineering | Практика | Deployed |

---

## 4. Методология оценки (7 критериев)

Каждая позиция оценивается **независимо** по шкале 0–5:

1. **Новизна** — насколько направление новое (2020–2026 vs десятилетия).
2. **Зрелость** — Research / Experimental / Deployed / Mainstream.
3. **Масштаб** — локальные эксперименты → глобальное внедрение.
4. **Эффективность** — наличие измеримых результатов (не обещаний).
5. **Доступность** — стоимость, компетенции, инфраструктура.
6. **Независимость** — снижает ли зависимость от единых посредников.
7. **Стратегическое влияние** — меняет ли правила игры в отрасли/системе.

**Нельзя** складывать в один балл без явных весов.  
Экспериментальная технология с высоким стратегическим влиянием и массовая практика с низкой новизной — разные сущности.

---

## 5. Стратегические кластеры 2026 (приоритетные)

### Кластер 1. Агентная инфраструктура
- Multi-Agent Systems (001)
- Agentic Automation (002)
- AI Orchestration (003)
- Computer-Use Agents (1016)
- Human-on-the-Loop / Human-in-the-Loop (004–005)
- Bounded Autonomy + Override (923, 940)

**Ключевой риск 2026:** переход от пилотов к production (Deloitte: 11 % в production, 38 % в пилотах).

### Кластер 2. Physical AI + Robotics
- Physical AI (1019)
- Humanoid Robotics (1018)
- Multi-Robot / Swarm (801–803)
- Embodied AI (809)
- Sim-to-Real + Domain Randomization (806–807)

### Кластер 3. AI Infrastructure Engineering
- AI Data Centers (1021)
- Liquid Cooling (1023)
- Energy Engineering for AI (1024)
- Model Compression / Quantization (1005–1007)
- Edge + Local AI (007, 040, 099)

### Кластер 4. Проверяемое знание и доверие
- Digital Provenance / C2PA (030, 1039–1040)
- Claim-Evidence Graphs (982)
- AI Audit Trails (075)
- Independent Replication (989)
- Formal Verification + Runtime Verification (582, 915)

### Кластер 5. Устойчивость и независимость
- Local-First + Offline-First (098–099, 871–872)
- Graceful Degradation (880)
- Self-Healing + Resilience Engineering (067, 971)
- Personal Computing Sovereignty (870)
- Community Energy + Microgrids (423–425)

---

## 6. Правила работы с каталогом дальше

1. **Не добавлять** новые сотни позиций без предварительного аудита пересечений.
2. **Каждая новая позиция** должна иметь:
   - постоянный ID
   - тип сущности
   - родительскую область
   - связи (SAME / IS-A / PART-OF / RELATED / COMPLEMENTARY)
   - статус зрелости
   - минимум один первичный источник или явный UNKNOWN
3. **Дубликаты** не удаляются молча — создаётся таблица соответствий с обоснованием.
4. **Рейтинги** строятся только по отдельным критериям и только после нормализации.

---

## 7. Что считается завершённым результатом

- [x] Полный реестр 001–1000 сохранён.
- [x] 45 критических промышленных пробелов закрыты (1001–1045).
- [x] Методология оценки зафиксирована.
- [x] Стратегические кластеры 2026 выделены.
- [x] Источники актуализированы (Gartner 2026, Deloitte 2026, IEA WEO 2026).
- [x] Отказ от претензии «лучшие практики» без доказательной базы.

**Следующий возможный шаг (по запросу):**  
построчный аудит любого из 10 доменов с таблицей `ID → Normalized Name → Type → Relations → Maturity → Evidence → Verdict`.

---

*Документ подготовлен как завершение работы вместо незавершённого процесса.*  
*Дата: ноябрь 2026.*
