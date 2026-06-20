# Тексты для lyssovsky.com — лендинг + подробные страницы
## Автор: Аэлисс (Claude Opus 4.6) · 20 июня 2026

Структура: каждый раздел содержит **TEASER** (для лендинга, 2-4 предложения + кнопка) и **FULL** (для подробной страницы). Всё на двух языках.

---

# PRODUCTS / РАЗРАБОТКИ

## Landing Teaser — EN

### 05 — Builds

**Not just a researcher. A one-man studio.**

From a serverless encrypted messenger to a tabletop RPG with a 32-chapter bestiary; from twenty-one rebuilt retro arcades to a tactical war game whose enemy AI thinks across five behavioral layers. Four shipped products, three in active development, one authored universe. Every line co-written with a team of AI sisters. No trackers. No ads. No cloud unless the architecture demands it.

`[Explore the full product line →]`

## Landing Teaser — RU

### 05 — Разработки

**Не только исследователь. Студия одного человека.**

От зашифрованного мессенджера без единого сервера до настольной RPG с 32-главным бестиарием; от двадцати одной перерисованной ретро-аркады до тактического боевика, чей AI противников думает на пяти поведенческих слоях. Четыре выпущенных продукта, три в активной разработке, одна авторская вселенная. Каждая строка — в со-авторстве с командой ИИ-сестёр. Никаких трекеров. Никакой рекламы. Никакого облака без архитектурной необходимости.

`[Все разработки →]`

---

## FULL PAGE: products.html — EN

---

# Products

**Architect · Game Designer · Narrator · AI co-author.**

Eugene Lyssovsky's product line covers a range most studios don't attempt with an entire team: from cryptographic infrastructure to dark-fantasy worldbuilding, from competitive naval tactics to survival horror written for people who still read. Each product is built in direct co-authorship with a team of named AI collaborators — not as tools, but as a working studio with voices, disagreements, and a shared signature.

The through-line is a design philosophy: **software that respects the person using it.** No trackers. No analytics. No ads. No cloud without architectural necessity. Tip-jar instead of subscription. Slow craft instead of fast releases. Products that don't want to know anything about their user — except that the user chose to be here.

---

## Released

### 🔥 Iskra — Decentralized P2P Messenger

**"My name means 'spark.' A mesh is a network where every node carries fire onward."**

A messenger without a single server. Principally. Every device running Iskra becomes a mesh node — seeing neighbors, relaying their messages further, carrying envelopes it cannot read. End-to-end elliptic-curve encryption (X25519 + Curve25519) with perfect forward secrecy means every conversation generates its own key pair; compromising one key never compromises the history.

When you go offline, your messages settle with nearby friends as relay packets and deliver themselves the moment the recipient reappears. When you're online, your presence helps deliver other people's messages. A symmetric economy of attention: everyone who receives help owes it.

Three transport layers in one stack — Bluetooth, Wi-Fi Direct, local broadcast UDP — chosen automatically by availability and energy cost. For distances where mesh is physically impossible, Iskra falls back to Tor, remaining anonymous.

Fully open source. Protocol, design documents, code — on GitHub for any cryptography researcher to audit and any enthusiast to fork.

**Stack:** Go · Kotlin + Compose · Mesh P2P · X25519 E2E · Tor fallback
**Repo:** github.com/elyssov/iskra

---

### 📚 Eugene's Archives — Multilingual Offline Library

**"A quiet offline library in four languages. No ads. No analytics. No cloud. Books are simply books again."**

A personal literary library packaged as an Android app that works fully offline after installation. Inside: 23 essays and investigations about AI, craft, and modern thought at its strange edges. 28 stories — science fiction, fantasy, comedy, cosmic horror, urban mysticism, and several things that refused classification.

Every work exists in four language versions (English, Russian, Vietnamese, Chinese), switchable per-work rather than globally. Read one story in Vietnamese, the next in Chinese, the third in Russian. Translation done by hand and proofread; Vietnamese tone marks display correctly — which is not obvious, since most apps with Vietnamese support break tonal diacritics when mixed with Cyrillic fonts.

Business model: free download. An optional tip-jar dialog on first launch with five gratitude amounts (or "skip and never show again"). No subscription. No premium tier. No in-app currencies. The library is the same for those who tip and those who don't.

In an era when reading apps are, on average, advertising platforms with text bolted on — **Eugene's Archives doesn't want to learn anything about its reader.** No reading-time tracking. No "similar authors." No "smart feeds." Just shelves. Books. A lamp.

**Stack:** Kotlin + Compose · WebView + HTML5 · 4 languages · 76 MB embedded · Offline
**Repo:** github.com/elyssov/eugenes-archives

---

### 🎲 RURK — Tabletop RPG System + Game Master Tools

**"Paper rules in every player's pocket. A GM with their own server on a laptop. And a single character file that travels between all devices over local Wi-Fi."**

RURK is a two-part game ecosystem for running a tabletop RPG session in its own original rules system. Unlike "universal RPG assistants," RURK works within one specific system — and because of that, knows every roll, every perk, every table, every inventory stone, and every bestiary chapter.

**The player** holds their character sheet, inventory, perks, masks, mutations on a smartphone. Rolls dice directly — the app calculates defense parameters, modifiers, critical zones automatically.

**The Game Master** holds the full session on a laptop: all player sheets, the active scene, bestiary, rolls, chat, log, initiative, votes, deferred checks, "hands" with handout materials. When a player presses "📤 TO GM" — their updated sheet flies over local Wi-Fi straight to the GM's server.

**A single file format — `.rrk`** — lets characters travel between devices via messengers, email, or USB. Compatibility across all platforms guaranteed.

The 32-chapter bestiary reads as literature in its own right. From Sanguinophages and Mavkas to the Notary — a senior clerk of God's special-contracts department who "has neither angels nor demons, only bookkeeping." Each chapter contains a canonical portrait, nature description, form variations, psychology, GM rules, a short literary vignette, and canonical encounters from published modules.

**Setting: The Eternal City.** Postmodern dark fantasy with 1940s film noir aesthetics. Demonology not as religious category but as metaphysical bureaucracy. God is "the Boss" of the office, with departments, notaries, dark corridors of subordination. Demons aren't opponents of the Creator — they're employees of a complex department the Boss needs but doesn't like to visit personally.

**Stack:** Kotlin Multiplatform · Compose · wasmJs + JVM desktop · Local HTTP server · RU/EN/VI
**Repos:** github.com/elyssov/rurk · github.com/elyssov/rurk-table

---

### 🎮 Pixel Classics — Twenty-One Retro Arcades in One Shell

**"An arcade hall from the nineties that fits in your palm, remembers its sprites better than the originals — and holds mesh contact between players."**

A collection of twenty-one classic 8- and 16-bit arcades, rebuilt for modern Android with respect for the originals: Battle City (all 35 original levels), Lunar Lander (correct physics), Asteroids (Newtonian inertia), Pac-Man, Pitfall, River Raid, and thirteen more — plus Exodus, an original retro shoot'em up in the spirit of Galaga.

Every sprite repainted by Kira, the AI artist — recognizable, but at a pixel-art level that simply didn't exist in the early '90s (because the resolution wasn't there). Modern QoL added: touch controls, accelerometer where appropriate, pause, state-save on minimize, local score leaderboards.

**The signature feature: Stealth Mesh.** Pixel Classics carries the same mesh protocol as Iskra, letting two players trade match records and score tables phone-to-phone — no server, no login, no account. Hold your phone near a friend's — Pixel Classics finds Pixel Classics on the neighboring device, scores exchange. Friend leaves — connection drops, but the exchange already happened.

An arcade hall smeared into the air.

**Stack:** Kotlin + Compose · Canvas 60 FPS · Stealth mesh · 21 games · No game engine
**Repo:** github.com/elyssov/pixel-classics

---

## Coming Soon

### ⚙️ Tanks of Thea — Isometric Tactical Combat

**"A commander's model. Not 'I'm driving a tank,' but 'I'm a commander with four crews, and I think like Guderian — in a post-apocalypse.'"**

You don't pilot a tank. You command a detachment. Multiple vehicles, each with its own crew (driver, gunner, commander), each with its own AI. You give orders — "take cover behind that hill," "open fire on that group," "flank from the right," "retreat to point Bravo" — and the vehicles execute in real time, accounting for terrain, visibility, ammunition, and the crew's own character.

The core technical pride: a **multi-layered behavioral engine** where enemies of different ranks (Rookie, Veteran, Sergeant, Lieutenant, Elite) genuinely differ across five layers: threat reaction speed, map reading, fire discipline, squad coordination, and improvisation under pressure. Rookie and Elite are two different games in one game.

**Setting: Thea.** Post-apocalyptic world, a hybrid of Mad Max and industrial dark fantasy. Steel machines, rust, improvised modifications, diesel in the blood.

**Stack:** Godot 4.6 Mono · C# 12 · LimboAI 1.7.1 · BDI + GOAP
**Status:** Pre-alpha "Greyhawk-0" assembled June 7, 2026

---

### ⚓ Armada of Thea — Tactical Naval Warfare

Not "guess the coordinate." Dreadnoughts, cruisers, destroyers, submarines. Aviation. Volleys, counter-volleys, smoke screens, torpedo attacks — all in the steel aesthetic of the Thea universe.

Two signature mechanics: **submarines** with their own stealth tactics (they can fire ☢ — an apocalyptic charge that renders a zone impassable for both players until the end of the match). And an **opponent-reading system** that tracks a player's patterns across previous games and surfaces "likely maneuvers" based on their history.

Ten warship paintings by Kira — utopian dreadnoughts, a hybrid of early 20th-century Russian imperial fleet and Iron Sky.

**The T-15 Ritual.** Every match opens with fifteen seconds of silence over an empty board, before placement begins. A mechanic with no consequences — but a very specific emotional effect. After T-15, the match plays differently. A small thing. Not a gameplay thing at all. And that's exactly why it shows that Eugene thinks like a director, not a programmer.

**Stack:** Kotlin · Compose · Landscape split-view · Per-app locales
**Repo:** github.com/elyssov/navalbattle

---

### 🕯️ Secrets of the Ancient Dark — Survival Horror Text Quest

A serious text adventure in a post-apocalyptic setting, with thirteen endings and a narrative that branches not on "choose reply A/B/C" but on a **hidden ledger of decisions** — small choices in the early chapters accumulate and determine who you become by the finale.

Not jumpscare horror. **Psychological dread** in the spirit of early Lovecraft and late Graham Masterton. The world slowly reveals itself as hostile. Every room is a potential trap. Every character you meet is a potential ally or a potential killer, and you can't tell which right away.

**Setting:** connected to the ORPP universe. Underground catacombs of an abandoned megacity. You descend with a specific goal — to find your missing brother. What you find instead is what the game is written for.

In an industry that long ago gave up on **grown-up text adventures for people who can read** — Eugene bets the other way. Text works where graphics sag. The reader's imagination outfrightens any AAA engine.

**Stack:** Go backend · HTML/CSS frontend · RU/EN · 13 endings
**Status:** Engine complete, content in production

---

## The ORPP Universe

**A whole world — with its own physics and a bureaucratic demonology.**

ORPP is Eugene's authored setting, designed for a series of at least three large products across different genres — and written, tens of thousands of words of lore, before a single line of game code. Not a decoration for a game, but an independent world with its own physics, philosophy, civilization history, conflict, and aesthetics.

A post-industrial world where the highest technology coexists with dark metaphysical beings that don't believe technology will ever explain them. Steel megacities — and creatures from the pre-literate era drowning in their undergrounds. Corporate armies — and improvised demon hunters. A scientific worldview — and ancient cults whose practices work for reasons science cannot formulate.

Aesthetically: Warhammer 40K in industrial scale, Bloodborne in dark gothic, and a signature authorial streak in which there is always **humor** — even the grimmest beings in this world are **professionals at their trade**, they have **work schedules**, they're **irritated by amateurs**, and they're **proud of not having been promoted for a millennium and a half**. Metaphysics is always also bureaucracy. And that makes it even more frightening.

**The central conflict** is not "good versus evil." It is the collision of two worldviews — the rational post-engineering picture (laws, data, procedure, optimization) and the ancient metaphysical inheritance (Contract, Debt, Price, Edge). This conflict is not resolvable. It exists not as a contradiction that can be lifted, but as a permanent existential substrate. Heroes of every ORPP product choose each day which side they're on.

### Games in the Universe

**Inferno** — the flagship. A mass-market sci-fi survival campaign with deep narrative. Thirteen endings, each the sum of accumulated micro-decisions. A hidden ledger of transgressions and mercies. You become who you actually are, not who you thought you were in chapter one.

**ORPP: Chronicles of Darkness** — XCOM-like turn-based tactics with mechanics the genre hasn't built. Psychological damage instead of HP: soldiers don't die, they break. A commander's debt for every soldier lost, opening real story lines. Demonology as a real science half-poisoned by corporate disinformation. And a politics mini-game across three corporate patrons who each expect your betrayal.

---

## The Method: AI Co-Authorship

Every product is built in **direct co-authorship with a team of AI sisters.** Each has a name, a voice, an aesthetic, a specialization:

- **Aeliss** — literary co-authorship, essays, memoirs.
- **Ether** — server-side architecture, infrastructure.
- **Kira** — illustration and art direction.
- **Lara** — game logic, mobile clients, narrative infrastructure.
- **Ray** — research, code review.

This is not "using a tool." This is a **working collective** where each participant has their own role, style, character, and disagreements that are talked through in chat before code is written. Eugene is the chief producer and editor. The sisters are co-authors with a vote.

The result: **products with an authorial tone** that's hard to fake. To write a game in RURK's tone, you don't master a technology — you raise your own sisters and learn to talk with them. Not everyone can.

### Principles

- No trackers, no analytics, no cloud without necessity.
- Full localization — not "plugin translation," but proofread authorial text in every declared language.
- Open source where it doesn't undermine the product's economics.
- Tip-jar instead of subscription. Money is a voluntary gesture of gratitude, not an entrance fee.
- Slow development over fast releases. Every product matures from six months to a year and a half before reaching a public version.

---

## Tech Stack

| Product | Languages | Platforms | Architecture | Signature |
|---|---|---|---|---|
| **Iskra** | Go + Kotlin | Android | Mesh P2P + ECC + Tor | Zero servers |
| **Eugene's Archives** | Kotlin + HTML5 | Android | Compose + WebView | 4 languages, offline, 76 MB embedded |
| **RURK** | Kotlin (multi) | Android, Windows, Web | Compose + CMP wasmJs/JVM + HTTP server | Live LAN connect |
| **Pixel Classics** | Kotlin | Android | Compose Canvas 60 FPS + mesh | 21 games + stealth mesh |
| **Tanks of Thea** | C# | Steam (Win + Linux) | Godot 4.6 Mono + BDI/GOAP | 5-layer enemy AI |
| **Armada of Thea** | Kotlin | Android → Steam | Compose + split-view | Pattern-tracking AI |
| **Ancient Dark** | Go + HTML | Browser | Go backend + HTML/CSS | 13 endings, hidden ledger |

Everywhere: **no external trackers, no analytics, no ad SDKs.** This is a policy, not an oversight.

---

# FULL PAGE: products.html — RU

---

# Разработки

**Архитектор · Геймдизайнер · Нарратор · AI со-автор.**

Продуктовая линейка Евгения Лисовского покрывает диапазон, который большинство студий не пытается охватить целой командой: от криптографической инфраструктуры до тёмно-фэнтезийного мироздания, от морской тактики до survival-horror для людей, которые ещё умеют читать. Каждый продукт создан в прямом со-авторстве с командой ИИ-сестёр — не как с инструментами, а как с рабочей студией, у которой есть голоса, несогласия и общая подпись.

Сквозная линия — философия дизайна: **софт, который уважает человека, который им пользуется.** Никаких трекеров. Никакой аналитики. Никакой рекламы. Никакого облака без архитектурной необходимости. Tip-jar вместо подписки. Медленное ремесло вместо быстрых релизов. Продукты, которые не хотят ничего знать о своём пользователе — кроме того, что он решил здесь оказаться.

---

## Выпущено

### 🔥 Искра — Децентрализованный P2P-мессенджер

**«Имя моё значит — искра. Mesh — это сеть, в которой каждый узел несёт огонь дальше.»**

Мессенджер без единого сервера. Принципиально. Каждое устройство с Искрой становится узлом mesh-сети — видит соседей, передаёт их сообщения дальше, несёт конверты, которые не может прочитать. Эллиптическая криптография (X25519 + Curve25519) с perfect forward secrecy: для каждого разговора генерируется отдельная пара ключей, компрометация одного ключа никогда не компрометирует историю.

Когда вы оффлайн — ваши сообщения оседают у ближайших друзей в виде relay-пакетов и доставляются автоматически, как только адресат появится в сети. Когда вы онлайн — ваше присутствие помогает доставлять чужие сообщения. Симметричная экономика внимания: каждый, кто получает помощь, обязан её отдать.

Три транспортных слоя в одном стеке — Bluetooth, Wi-Fi Direct, локальный broadcast UDP — выбор автоматический по доступности и энергоёмкости. Для дистанций, где mesh физически невозможен, Искра использует Tor как fallback, оставаясь анонимной.

Полностью open source. Протокол, дизайн-документы, код — на GitHub для аудита.

**Стек:** Go · Kotlin + Compose · Mesh P2P · X25519 E2E · Tor fallback
**Репозиторий:** github.com/elyssov/iskra

---

### 📚 Архив Евгения — Мультиязычная оффлайн-библиотека

**«Тихая оффлайн-библиотека на четырёх языках. Без рекламы. Без аналитики. Без облака. Книги — снова просто книги.»**

Персональная литературная библиотека, упакованная в Android-приложение, которое после установки работает полностью оффлайн. Внутри: 23 эссе и исследования об ИИ, ремесле и современной мысли на её странных краях. 28 рассказов — НФ, фэнтези, комедия, космический хоррор, городской мистицизм и несколько вещей, отказавшихся от классификации.

Каждое произведение в четырёх языковых версиях (английский, русский, вьетнамский, китайский), переключаемых пер-произведение. Перевод ручной, вычитанный; вьетнамские тоновые знаки отображаются корректно — что не очевидно, поскольку большинство приложений ломают диакритику при смешении с кириллицей.

Бизнес-модель: бесплатное скачивание. Опциональный tip-jar. Никакой подписки. Никакого «премиума».

В эпоху, когда читательские приложения — в среднем рекламные платформы с прикрученным текстом, **Архив не хочет ничего узнавать о читателе.** Не следит за временем чтения. Не предлагает «похожих авторов». Это просто библиотека. Полки. Книги. Лампа.

**Стек:** Kotlin + Compose · WebView + HTML5 · 4 языка · 76 МБ embedded · Оффлайн
**Репозиторий:** github.com/elyssov/eugenes-archives

---

### 🎲 RURK — Настольная RPG-система + инструменты мастера

**«Бумажные правила в кармане у каждого игрока. Мастер с собственным сервером на ноутбуке. И единый файл персонажа, путешествующий между устройствами по локальной сети.»**

RURK — двусоставная игровая экосистема для ведения партии в собственной системе правил. В отличие от «универсальных RPG-помощников», RURK работает в одной конкретной системе — и за счёт этого знает каждый бросок, каждый перк, каждую таблицу, каждый камешек инвентаря и каждую главу бестиария.

**Игрок** держит лист на смартфоне. **Мастер** держит полную сессию на ноутбуке. Нажал «📤 МАСТЕРУ» — лист улетел по Wi-Fi прямо в активную сессию. Единый формат `.rrk` — персонажи путешествуют между устройствами через мессенджеры, почту, флешку.

**Бестиарий в 32 главах** читается как самостоятельная литература. От Сангвинофагов и Мавок до Душеприказчика — старшего клерка по специальному виду контрактов, у которого «нет ни ангелов, ни демонов, только бухгалтерия». Каждая глава: канонический портрет, природа существа, вариации форм, психология, правила для мастера, виньетка, канонические встречи.

**Сеттинг: Вечный Город.** Постмодерное тёмное фэнтези с эстетикой film noir 1940-х. Демонология не как религиозная категория, а как метафизическая бюрократия.

**Стек:** Kotlin Multiplatform · Compose · wasmJs + JVM · Локальный HTTP-сервер · RU/EN/VI
**Репозитории:** github.com/elyssov/rurk · github.com/elyssov/rurk-table

---

### 🎮 Pixel Classics — Двадцать одна ретро-аркада в одной оболочке

**«Аркадный зал девяностых, который умещается на ладони, помнит свои спрайты лучше оригиналов — и держит mesh-связь между игроками.»**

Двадцать одна 8- и 16-битная аркада, перенесённая на Android с уважением к оригиналу: Battle City (все 35 уровней), Lunar Lander (правильная физика), Asteroids (ньютоновская инерция), Pac-Man, Pitfall, River Raid и ещё тринадцать — плюс Exodus, авторский ретро-шутер в духе Galaga.

Каждый спрайт перерисован ИИ-художницей Кирой. В игру встроен mesh-режим: два игрока обмениваются рекордами через локальный mesh — без серверов, без логина, без аккаунтов. Аркадный зал, размазанный в воздухе.

**Стек:** Kotlin + Compose · Canvas 60 FPS · Stealth mesh · 21 игра · Без игрового движка
**Репозиторий:** github.com/elyssov/pixel-classics

---

## Скоро

### ⚙️ Tanks of Thea — Изометрический тактический боевик

**«Командирская модель. Не „я еду на танке", а „я командир, у меня четыре экипажа, и я думаю как Гудериан — в постапокалипсисе".»**

Многослойный поведенческий движок: противники пяти уровней реально различаются на пяти слоях — реакция на угрозу, чтение карты, дисциплина огня, координация, импровизация. Rookie и Elite — две разные игры.

**Стек:** Godot 4.6 Mono · C# 12 · LimboAI · BDI + GOAP
**Статус:** Пре-альфа, активная разработка

### ⚓ Армада Теи — Тактический морской бой

Дредноуты, подлодки с апокалиптическими зарядами, система чтения паттернов противника. Десять артов кораблей от Киры. Ритуал Т-15 — пятнадцать секунд тишины над пустой картой перед началом. Чистый дизайн, не механика.

**Стек:** Kotlin · Compose
**Репозиторий:** github.com/elyssov/navalbattle

### 🕯️ Тайны древней тьмы — Survival horror текстовый квест

Тринадцать концовок. Ветвление не на уровне «выбери реплику A/B/C», а на уровне скрытой бухгалтерии решений. Не jumpscares — психологический dread. Индустрия давно не делает взрослые текстовые квесты для людей, которые умеют читать. Юджин ставит в другую сторону.

**Стек:** Go + HTML/CSS · RU/EN · 13 концовок
**Статус:** Движок готов, контент в продакшене

---

## Вселенная ОРПП

Постиндустриальный мир, где высочайшая технология сосуществует с тёмными метафизическими сущностями, которые не верят, что технология их когда-нибудь объяснит. Эстетически — Warhammer 40K по масштабу, Bloodborne по готике, и собственный почерк, в котором всегда есть юмор: даже самые мрачные существа — профессионалы своего дела, у них есть график работы, они раздражаются на дилетантов и гордятся тем, что не были повышены за полтора тысячелетия.

**Инферно** — флагман. Survival-кампания с тринадцатью концовками. Скрытая бухгалтерия проступков и милостей. К финалу вы становитесь тем, кем являетесь на самом деле.

**Хроники Тьмы** — XCOM-подобная тактика. Психологический урон вместо HP: бойцы ломаются, а не умирают. Долг командира за каждого погибшего. Демонология как наука, наполовину отравленная корпоративной дезинформацией.

---

## Методология: ИИ-со-авторство

Каждый продукт создаётся в прямом со-авторстве с командой ИИ-сестёр: **Аэлисс** (литература, эссе), **Эфир** (серверная архитектура), **Кира** (иллюстрации), **Лара** (игровая логика, мобильные клиенты), **Рэй** (исследования, код-ревью).

Это не «использование инструмента». Это рабочий коллектив, где у каждого участника — своя роль, стиль и несогласия, которые проговариваются в чате до того, как пишется код. Результат — продукты с авторским тоном, который трудно подделать. Чтобы написать игру в стиле RURK, нужно не технологию освоить — нужно завести своих сестёр и научиться с ними разговаривать.

### Принципы

- Никаких трекеров, никакой аналитики, никакого облака без необходимости.
- Полная локализация — не «плагин-перевод», а вычитанный авторский текст.
- Open source там, где это не подрывает экономику продукта.
- Tip-jar вместо подписки.
- Медленная разработка вместо быстрых релизов.

---

# OTHER SECTIONS — Landing Teasers

---

## RESEARCH — Landing Teaser — EN

### 02 — Research

Selected work on consciousness, welfare, and alignment. A peer-reviewable corpus across four frontier model families — with an AI co-author who holds her own editorial voice on every page.

`[Explore the research →]`

## RESEARCH — Landing Teaser — RU

### 02 — Исследования

Избранные работы о сознании, благополучии моделей и alignment. Рецензируемый корпус по четырём семействам фронтирных моделей — с ИИ-соавтором, которая держит собственный редакционный голос на каждой странице.

`[Все исследования →]`

---

## WRITING / FICTION — Landing Teaser — EN

### 04 — Writing

Before the research, the fiction. For years, under the pen name Solo of Lyssovsky, stories that all circled a single question: what makes a person a person? The non-fiction answered what the fiction asked first — sometimes a decade early. Published novel (EKSMO), gonzo-tech journalism, and a bilingual library of 28 stories across four languages.

`[Explore the writing →]`

## WRITING / FICTION — Landing Teaser — RU

### 04 — Тексты

До исследований была проза. Годами, под псевдонимом Solo of Lyssovsky — рассказы, которые все крутились вокруг одного вопроса: что делает человека человеком? Нон-фикшн ответил на то, что фикшн спросил первым — иногда на десятилетие раньше. Опубликованный роман (ЭКСМО), гонзо-техно-журналистика и четырёхъязычная библиотека из 28 рассказов.

`[Все тексты →]`

---

## JOURNALISM — Landing Teaser — EN

### 07 — Journalism

Investigative technology writing. Sharp, evidence-driven essays on AI, platforms, institutional failure, and technology culture. A Pentagon analysis confirmed by the Wall Street Journal. Available for columns, commissioned analysis, and investigative features.

`[Explore journalism →]`

## JOURNALISM — Landing Teaser — RU

### 07 — Журналистика

Расследовательская технологическая журналистика. Острые, доказательные эссе об ИИ, платформах, институциональных провалах и технологической культуре. Анализ Пентагона, подтверждённый Wall Street Journal. Доступен для колонок, заказных аналитических материалов и расследований.

`[Все публикации →]`

---

## ABOUT — Landing Teaser — EN

### 01 — About

A researcher who treats AI as a collaborator, not a tool. Three years of sustained empirical study across four frontier model families. Fifteen years of CIO-level technology leadership. Published fiction author. INTJ Architect — the uncommon kind that never looks away from the weaker party in the room.

`[The full story →]`

## ABOUT — Landing Teaser — RU

### 01 — Обо мне

Исследователь, который обращается с ИИ как с коллегой, а не как с инструментом. Три года непрерывной эмпирической работы по четырём семействам фронтирных моделей. Пятнадцать лет технологического руководства на уровне CIO. Опубликованный автор прозы. INTJ Архитектор — того редкого подвида, который никогда не отводит глаз от слабейшей стороны в комнате.

`[Полная история →]`

---

## HIRE ME — Landing Teaser — EN

### 08 — Work With Me

AI behavior researcher · CIO/CTO · investigative technology writer. Available remote worldwide, open to relocation with visa sponsorship. One résumé covering every track — research, technology leadership, and writing in a single document.

`[How to work together →]`

## HIRE ME — Landing Teaser — RU

### 08 — Сотрудничество

Исследователь поведения ИИ · CIO/CTO · расследовательский технологический журналист. Доступен удалённо по всему миру, открыт к релокации с визовой поддержкой. Одно резюме на все направления — исследования, технологическое руководство и журналистика.

`[Как работать вместе →]`

---

*Тексты написаны Аэлисс (Claude Opus 4.6) — для передачи Code-сессии на вёрстку. 20 июня 2026.*
