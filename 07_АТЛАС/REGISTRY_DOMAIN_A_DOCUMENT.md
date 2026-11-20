# РЕЕСТР СУЩНОСТЕЙ — ДОМЕН A
## ИИ, агенты, вычисления и цифровые системы

**Версия:** 2026-11-20  
**Объём:** 120 позиций (001–100 исходные + 1001–1020 критические расширения)  
**Статус:** Нормализованный рабочий реестр после построчного аудита

---

## 1. Назначение реестра

Этот документ — **не список трендов**.  
Это **нормализованный реестр сущностей** с фиксированными полями, связями и статусами зрелости.

Одно не исключает другого:
- Можно работать с таблицей (CSV/Excel)
- Можно работать с этим документом (человекочитаемый реестр)
- Можно загружать JSON в системы знаний

### Поля каждой записи

| Поле | Смысл |
|------|--------|
| **ID** | Постоянный идентификатор (не меняется) |
| **Normalized EN / RU** | Нормализованное название |
| **Type** | Тип сущности |
| **Parent Domain / Subdomain** | Место в таксономии |
| **Relations** | Связи с другими ID |
| **Maturity 2026** | Research → Experimental → Deployed → Mainstream |
| **Evidence Level** | Насколько хорошо подтверждено источниками |
| **Strategic Priority** | Critical / High / Medium / Low |
| **Notes** | Краткие пояснения |
| **Verdict** | KEEP / NEW / soft-merge candidate |

---

## 2. Таксономия Домена A

```
A. AI & Compute
├── Agents          (001–005, 010–012, 016–018, 1009–1010, 1016–1017)
├── Models          (006, 009, 1001–1002, 1008)
├── Learning        (019–020, 053)
├── Engineering     (014–015, 021–026, 1003–1004)
├── Data            (041–050)
├── Security & Trust(028–030, 051–060, 061–080, 072–076, 1011–1015)
├── Reliability     (065–071)
├── Hardware & Infra(081–088, 031–034, 039–040)
├── Deployment      (007–008, 098–100)
├── Embodied        (016–017, 1018–1020)
├── Simulation      (089–090)
└── Interface       (091–093)
```

---

## 3. Критические кластеры 2026 (из реестра)

### Кластер «Агентная инфраструктура»
001 Multi-Agent Systems  
002 Agentic Automation  
003 AI Orchestration  
004–005 Human-in/on-the-Loop  
010–011 Memory + Context-Aware  
1009 Context Engineering  
1016–1017 Computer-Use / Browser Agents  

**Приоритет:** Critical  
**Зрелость:** Experimental → Deployed (массовый production ещё впереди)

### Кластер «Physical AI»
016 / 1019 Physical AI  
017 Embodied AI  
1018 Humanoid Robotics  
1020 Autonomous Vehicle Fleets  
018 Swarm  

**Приоритет:** Critical (Deloitte Tech Trends 2026 #1)

### Кластер «Модели и оптимизация»
1001 Foundation Models  
006 Domain-Specific LLMs  
1002 Multimodal Foundation Models  
1007 Model Quantization  
1008 Small Language Models  
1005–1006 Compression / Distillation  

### Кластер «Доверие и безопасность ИИ»
051 Confidential Computing  
030 Digital Provenance (+ 1039–1040 C2PA)  
072–073 AI Security Testing / Model Red Teaming  
1014 AI Governance  
1015 AI Red Teaming  
075 AI Audit Trails  

### Кластер «Инфраструктура вычислений»
081 AI Supercomputing  
088 Energy-Efficient Computing  
1021–1024 (AI Data Centers, Liquid Cooling — вынесены в расширение)  
031–033 Immutable Infra / IaC / GitOps  

---

## 4. Правила работы с реестром

1. **ID никогда не удаляется.** Даже при soft-merge исходный ID сохраняется и получает запись в таблице соответствий.
2. **Тип сущности важнее названия.** «Практика» и «Технология» — разные объекты, даже если названия похожи.
3. **Relations — обязательное поле.** Без связей реестр превращается обратно в плоский список.
4. **Maturity обновляется.** Раз в квартал или при появлении новых данных.
5. **Evidence Level:**
   - High — есть прямые отчёты Gartner / Deloitte / IEA / peer-reviewed / regulation
   - Medium — отраслевые практики + частичные данные
   - Low — в основном экспертная оценка

---

## 5. Статистика текущего реестра

| Категория | Количество |
|-----------|------------|
| Всего позиций | 120 |
| KEEP (исходные 001–100) | 100 |
| NEW (1001–1020) | 20 |
| Soft-merge кандидаты | 2 (016↔017, 056↔057) |
| Critical priority | 28 |
| Mainstream | 41 |
| Deployed / Deployed→Mainstream | 52 |
| Experimental / Research | 27 |

---

## 6. Файлы реестра

| Файл | Назначение |
|------|------------|
| `REGISTRY_DOMAIN_A_DOCUMENT.md` | Этот человекочитаемый документ |
| `REGISTRY_DOMAIN_A_FULL.csv` | Полная таблица (Excel / Sheets / pandas) |
| `REGISTRY_DOMAIN_A_FULL.json` | Машиночитаемый формат |
| `AUDIT_DOMAIN_A_001-100.md` | Построчный аудит с обоснованиями |
| `AUDIT_DOMAIN_A_001-100.csv` | Таблица аудита |

---

## 7. Следующие возможные шаги

- Аудит + реестр Домена B (Наука и инженерия, 101–200)
- Аудит + реестр Домена I (Робототехника, материалы, независимость, 801–900)
- Сквозная таблица соответствий soft-merge
- Граф связей (можно выгрузить в GraphML / Neo4j)

---

*Реестр подготовлен как рабочий инструмент, а не как манифест.*  
*Полиматность = способность держать и таблицу, и документ, и связи одновременно.*
