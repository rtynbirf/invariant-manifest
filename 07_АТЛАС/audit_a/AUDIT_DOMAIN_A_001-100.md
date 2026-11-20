# Построчный аудит Домена A
## ИИ, агенты и цифровые системы (позиции 001–100)

**Дата аудита:** 20 ноября 2026  
**Метод:** сравнение исходной формулировки, типа сущности, связей, зрелости 2026, наличия доказательной базы.

### Легенда статусов

| Статус | Значение |
|--------|----------|
| **KEEP** | Самостоятельная сущность, оставить |
| **MERGE** | Дубликат / синоним → объединить с указанным ID |
| **RECLASSIFY** | Сущность самостоятельна, но тип/область указаны неточно |
| **SPLIT** | В одной позиции смешаны несколько сущностей |
| **RELATED** | Родственная, но не дубликат |
| **UNKNOWN** | Недостаточно данных для окончательного вердикта |

### Типы сущностей
Практика · Технология · Метод · Архитектура · Принцип · Стандарт · Организационная модель · Инструмент

### Уровни зрелости (2026)
Research → Experimental → Deployed → Mainstream

---

## Таблица аудита 001–100

| ID | Normalized Name | Type | Relations | Maturity 2026 | Evidence | Verdict |
|----|-----------------|------|-----------|---------------|----------|---------|
| 001 | Multi-Agent Systems (MAS) | Архитектура | RELATED to 002, 003, 931; IS-A of Agentic Systems | Deployed | Gartner 2026 Top Trends (Multiagent Systems); Deloitte 2026 | **KEEP** |
| 002 | Agentic Automation | Практика | PART-OF 001; RELATED to 1016 (Computer-Use Agents) | Experimental → Deployed | Deloitte 2026 “agentic reality check”; 11% production | **KEEP** |
| 003 | AI Orchestration | Практика / Архитектура | RELATED to 001, 002; COMPLEMENTARY to 820 | Deployed | Platform engineering + agent frameworks 2025–26 | **KEEP** |
| 004 | Human-in-the-Loop (HITL) | Принцип | COMPLEMENTARY to 005, 924; RELATED to 940 | Mainstream | Классика safety-critical систем | **KEEP** |
| 005 | Human-on-the-Loop (HOTL) | Принцип | RELATED to 004; DIFFERENT level of control | Deployed | Military & high-autonomy systems literature | **KEEP** |
| 006 | Domain-Specific LLMs / DSLMs | Технология | IS-A of 1001 (Foundation Models); RELATED to Gartner DSLMs | Deployed → Mainstream | Gartner 2026: Domain-Specific Language Models | **KEEP** |
| 007 | Local AI / On-Device AI | Архитектура | RELATED to 008, 099, 1008 (SLM) | Deployed → Mainstream | Edge AI growth 2025–26 | **KEEP** |
| 008 | Hybrid AI | Архитектура | COMPLEMENTARY to 007 + cloud | Deployed | Common production pattern | **KEEP** |
| 009 | Multimodal AI | Технология | RELATED to 1002 (Multimodal Foundation Models) | Mainstream | GPT-4o, Gemini, Claude multimodal | **KEEP** |
| 010 | Persistent AI Memory | Метод / Компонент | RELATED to 011, 1009 (Context Engineering) | Experimental → Deployed | Memory layers in agent frameworks | **KEEP** |
| 011 | Context-Aware Agents | Практика | RELATED to 010, 1009 | Deployed | Context engineering trend 2025–26 | **KEEP** |
| 012 | Self-Verifying AI Systems | Метод | RELATED to 072–074, 891–893 | Experimental → Deployed | Self-consistency, tool-use verification | **KEEP** |
| 013 | AI for Scientific Discovery | Применение | RELATED to 114, 116 | Deployed | AlphaFold, materials discovery, etc. | **KEEP** |
| 014 | AI Software Engineering | Практика | RELATED to 021, 1003 (MLOps) | Deployed → Mainstream | GitHub Copilot, Cursor, Devin-class tools | **KEEP** |
| 015 | AI Interface Generation | Практика | RELATED to 014 | Deployed | Generative UI tools | **KEEP** |
| 016 | Physical AI / Embodied AI | Архитектура | SAME family as 1019; RELATED to 017, 809 | Experimental → Deployed | Deloitte 2026 #1 trend “AI goes physical” | **KEEP** (уточнить границы с 1019) |
| 017 | Embodied AI | Архитектура | CLOSE to 016; often used interchangeably | Experimental → Deployed | Research + early industrial | **KEEP** (можно MERGE с 016 при строгой дедупликации) |
| 018 | Swarm Intelligence / Swarm Robotics | Метод / Архитектура | RELATED to 802–803 | Experimental → Deployed | Multi-robot systems literature | **KEEP** |
| 019 | Reinforcement Learning | Метод | FOUNDATION for many agents | Mainstream | Classic + modern RL | **KEEP** |
| 020 | Continual Learning | Метод | RELATED to 1000 | Experimental → Deployed | Catastrophic forgetting research → production | **KEEP** |
| 021 | AI-Native Development | Практика | RELATED to 014; Gartner AI-Native Platforms | Deployed | Gartner 2026 | **KEEP** |
| 022 | Spec-Driven Development | Практика | RELATED to 023 | Deployed | Growing with LLM code gen | **KEEP** |
| 023 | Test-Driven Development (TDD) | Практика | CLASSIC; RELATED to 024–026 | Mainstream | Established | **KEEP** |
| 024 | Property-Based Testing | Метод | RELATED to 023, 891 | Deployed | Hypothesis, QuickCheck family | **KEEP** |
| 025 | Mutation Testing | Метод | RELATED to 023 | Deployed | Quality of test suites | **KEEP** |
| 026 | Differential Testing | Метод | RELATED to 893 | Deployed | Compiler & LLM testing | **KEEP** |
| 027 | Reproducible Builds | Практика | RELATED to 868, 900 | Deployed → Mainstream | Supply-chain security | **KEEP** |
| 028 | Software Supply Chain Security | Практика | RELATED to 029, 030 | Mainstream | SLSA, SBOM mandates | **KEEP** |
| 029 | Software Bill of Materials (SBOM) | Стандарт / Артефакт | PART-OF 028 | Mainstream | NTIA, EU CRA | **KEEP** |
| 030 | Digital Provenance | Принцип / Практика | RELATED to 1039–1040 (C2PA) | Deployed | Growing regulation | **KEEP** |
| 031 | Immutable Infrastructure | Архитектура | RELATED to 032, 033 | Mainstream | Cloud-native standard | **KEEP** |
| 032 | Infrastructure as Code | Практика | RELATED to 031, 033 | Mainstream | Terraform, Pulumi, etc. | **KEEP** |
| 033 | GitOps | Практика | IS-A of 032 + declarative | Mainstream | ArgoCD, Flux | **KEEP** |
| 034 | Platform Engineering | Организационная модель / Практика | RELATED to 003 | Deployed → Mainstream | Internal developer platforms | **KEEP** |
| 035 | Microservices Architecture | Архитектура | CLASSIC | Mainstream | Still dominant pattern | **KEEP** |
| 036 | Event-Driven Architecture | Архитектура | RELATED to 037, 038 | Mainstream | Kafka, event buses | **KEEP** |
| 037 | CQRS | Паттерн | RELATED to 036, 038 | Deployed | Established | **KEEP** |
| 038 | Event Sourcing | Паттерн | RELATED to 036, 037 | Deployed | Established | **KEEP** |
| 039 | WebAssembly (WASM) | Технология | RELATED to 098 | Deployed → Mainstream | Edge, browsers, plugins | **KEEP** |
| 040 | Edge Computing | Архитектура | RELATED to 007, 093 | Mainstream | Widespread | **KEEP** |
| 041 | Data Mesh | Архитектура | RELATED to 042 | Deployed | Zhamak Dehghani | **KEEP** |
| 042 | Data Fabric | Архитектура | RELATED to 041 | Deployed | Overlaps with Mesh; different emphasis | **KEEP** |
| 043 | Knowledge Graphs | Технология | RELATED to 046, 784 | Deployed → Mainstream | Enterprise + RAG | **KEEP** |
| 044 | Vector Databases | Технология | RELATED to 045 | Mainstream | Core of RAG stacks | **KEEP** |
| 045 | Retrieval-Augmented Generation (RAG) | Метод | RELATED to 044, 046 | Mainstream | Default pattern 2024–26 | **KEEP** |
| 046 | GraphRAG | Метод | IS-A of 045 + 043 | Deployed | Microsoft Research et al. | **KEEP** |
| 047 | Semantic Search | Метод | RELATED to 044, 045 | Mainstream | | **KEEP** |
| 048 | Data Lineage | Практика | RELATED to 049, 050, 790 | Deployed → Mainstream | Governance requirement | **KEEP** |
| 049 | Data Contracts | Практика | RELATED to 048 | Deployed | Data Mesh companion | **KEEP** |
| 050 | Data Observability | Практика | RELATED to 048 | Deployed | Monte Carlo, etc. | **KEEP** |
| 051 | Confidential Computing | Технология | Gartner 2026 trend | Deployed | TEEs, confidential VMs | **KEEP** |
| 052 | Privacy-Enhancing Technologies (PETs) | Класс технологий | RELATED to 053, 054 | Deployed | Broad category | **KEEP** |
| 053 | Federated Learning | Метод | RELATED to 591 | Deployed | Cross-silo / cross-device | **KEEP** |
| 054 | Differential Privacy | Метод | RELATED to 052 | Deployed | Apple, Google, US Census | **KEEP** |
| 055 | Zero-Knowledge Proofs | Технология | RELATED to 056 | Deployed | Blockchain + identity | **KEEP** |
| 056 | Decentralized Identity | Архитектура | RELATED to 057, 593 | Deployed | DID, Verifiable Credentials | **KEEP** |
| 057 | Self-Sovereign Identity | Принцип / Модель | CLOSE to 056 | Deployed | | **KEEP** (можно RECLASSIFY как принцип 056) |
| 058 | Passkeys | Технология / Стандарт | RELATED to 056 | Mainstream | FIDO2 / WebAuthn | **KEEP** |
| 059 | Post-Quantum Cryptography | Технология | RELATED to 051 | Deployed (migration phase) | NIST standards 2024+ | **KEEP** |
| 060 | Zero Trust Architecture | Архитектура | Mainstream | Mainstream | NIST, CISA | **KEEP** |
| 061 | Preemptive Cybersecurity | Практика | Gartner 2026 | Deployed | Shift-left + predictive | **KEEP** |
| 062 | Continuous Security Validation | Практика | RELATED to 063 | Deployed | BAS, continuous red team | **KEEP** |
| 063 | Adversarial Testing | Метод | RELATED to 064, 072 | Deployed | | **KEEP** |
| 064 | Red Team / Blue Team | Практика | CLASSIC | Mainstream | | **KEEP** |
| 065 | Chaos Engineering | Практика | RELATED to 887 | Deployed → Mainstream | Netflix, Gremlin | **KEEP** |
| 066 | Fault-Tolerant Architecture | Архитектура | RELATED to 067, 880 | Mainstream | | **KEEP** |
| 067 | Self-Healing Systems | Архитектура / Свойство | RELATED to 914, 974 | Deployed | | **KEEP** |
| 068 | Observability Engineering | Практика | RELATED to 069 | Mainstream | OpenTelemetry | **KEEP** |
| 069 | Distributed Tracing | Метод | PART-OF 068 | Mainstream | | **KEEP** |
| 070 | Site Reliability Engineering (SRE) | Организационная модель / Практика | RELATED to 068 | Mainstream | Google origin | **KEEP** |
| 071 | Incident Response Automation | Практика | RELATED to 070 | Deployed | SOAR platforms | **KEEP** |
| 072 | AI Security Testing | Практика | RELATED to 073, 1015 | Deployed | Growing fast | **KEEP** |
| 073 | Model Red Teaming | Практика | IS-A of 072; RELATED to 1015 | Deployed | Anthropic, OpenAI, etc. | **KEEP** |
| 074 | Model Evaluation Frameworks | Метод / Инструмент | RELATED to 072 | Deployed → Mainstream | HELM, OpenAI Evals, etc. | **KEEP** |
| 075 | AI Audit Trails | Практика | RELATED to 030, 986 | Deployed | Governance requirement | **KEEP** |
| 076 | Cryptographic Attestation | Технология | RELATED to 051 | Deployed | | **KEEP** |
| 077 | Secure-by-Design | Принцип | RELATED to 078 | Mainstream | | **KEEP** |
| 078 | Least Privilege | Принцип | RELATED to 079, 060 | Mainstream | | **KEEP** |
| 079 | Capability-Based Security | Архитектура | RELATED to 861–862 | Deployed | | **KEEP** |
| 080 | Fail-Safe Defaults | Принцип | RELATED to 935 | Mainstream | | **KEEP** |
| 081 | AI Supercomputing | Инфраструктура | RELATED to 1021–1022; Gartner 2026 | Deployed → Mainstream | | **KEEP** |
| 082 | Neuromorphic Computing | Технология | Research → Experimental | Research → Experimental | Energy-efficient AI path | **KEEP** |
| 083 | Quantum Computing | Технология | Experimental (specialized) | Experimental | NISQ era | **KEEP** |
| 084 | Photonic Computing | Технология | Research → Experimental | Research → Experimental | | **KEEP** |
| 085 | Application-Specific Semiconductors (ASICs) | Технология | RELATED to 086 | Mainstream (for AI) | TPU, Inferentia, etc. | **KEEP** |
| 086 | Chiplet Architecture | Архитектура | RELATED to 085 | Deployed → Mainstream | AMD, Intel, etc. | **KEEP** |
| 087 | Heterogeneous Computing | Архитектура | RELATED to 081, 085 | Mainstream | CPU+GPU+NPU | **KEEP** |
| 088 | Energy-Efficient Computing | Принцип / Практика | RELATED to 1023–1024 | Deployed | Critical for AI infra | **KEEP** |
| 089 | Digital Twins | Технология / Метод | RELATED to 145, 579, 882 | Deployed → Mainstream | Industry + urban | **KEEP** |
| 090 | Simulation-First Development | Практика | RELATED to 881–900 | Deployed | | **KEEP** |
| 091 | Spatial Computing | Архитектура | RELATED to 092 | Deployed | Apple Vision, Meta | **KEEP** |
| 092 | Extended Reality (XR) | Технология | RELATED to 091 | Deployed | | **KEEP** |
| 093 | Ambient Computing | Архитектура | RELATED to 040, 945 | Experimental → Deployed | | **KEEP** |
| 094 | Internet of Things (IoT) | Архитектура | CLASSIC | Mainstream | | **KEEP** |
| 095 | Digital Product Passports | Стандарт / Практика | RELATED to 555 | Deployed (EU regulation) | ESPR, battery passport | **KEEP** |
| 096 | Interoperability by Design | Принцип | RELATED to 097 | Deployed | | **KEEP** |
| 097 | Open Standards | Принцип | RELATED to 096 | Mainstream | | **KEEP** |
| 098 | Portable Computing Environments | Архитектура | RELATED to 039, 867 | Deployed | WASM, containers | **KEEP** |
| 099 | Offline-First Architecture | Архитектура | RELATED to 007, 871–872 | Deployed | Local-first software movement | **KEEP** |
| 100 | User-Controlled Digital Ecosystems | Принцип / Архитектура | RELATED to 870, 876 | Experimental → Deployed | Sovereignty trend | **KEEP** |

---

## Сводка аудита Домена A

| Метрика | Значение |
|---------|----------|
| Всего позиций | 100 |
| **KEEP** | 98 |
| **MERGE-кандидаты** | 2 (016↔017 Embodied/Physical AI; 056↔057 Identity) |
| **RECLASSIFY** | 0 обязательных |
| **SPLIT** | 0 |
| Явные дубликаты | Нет |
| Связи с блоком 1001–1045 | Сильные (Foundation Models, MLOps, Physical AI, Computer-Use Agents, C2PA) |

### Ключевые наблюдения

1. **Нет массовых дубликатов** внутри 001–100. Большинство позиций — самостоятельные уровни абстракции (архитектура ↔ практика ↔ метод).
2. **016 и 017** (Physical AI / Embodied AI) — почти синонимы в текущем дискурсе 2026. Рекомендуется оставить оба ID, но в нормализованном реестре указать SAME/CLOSE.
3. **056 и 057** (Decentralized Identity / Self-Sovereign Identity) — SSI обычно рассматривается как принцип/модель внутри более широкой Decentralized Identity.
4. Самые “горячие” позиции 2026 по внешним источникам: 001 (Multi-Agent), 002 (Agentic), 006 (Domain-Specific LLMs), 016/1019 (Physical AI), 051 (Confidential Computing), 081 (AI Supercomputing).
5. Блок 1001–1045 закрывает реальные пробелы именно этого домена (MLOps, quantization, computer-use agents, AI data centers).

---

## Рекомендуемые действия после аудита

1. Создать таблицу соответствий для 016↔017 и 056↔057 (не удалять ID).
2. Добавить в нормализованный реестр явные ссылки на 1001–1020.
3. Для каждой KEEP-позиции в долгосрочной базе заполнить поля Evidence и Limitations из первичных источников.
4. Перейти к аудиту следующего домена по запросу (рекомендую B или I).

---

*Аудит выполнен 20.11.2026. Исходные формулировки сохранены.*
