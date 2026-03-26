## 1. Технология семантических меток

Метка — это **семантическое ядро** контента. Вместо передачи тяжёлых файлов (видео, фото, аудио) система передаёт только математическое описание смысла, структуры и ключевых характеристик.

**Пример:**
- Оригинальное видео 4K, 30 секунд → 300–800 МБ
- Семантическая метка → 2–40 КБ (сжатие в тысячи раз)

**Состав метки:**
- Латентные токены (компактное представление кадров, движения, звука и освещения)
- Семантический промпт (описание сцены, действий, тона и контекста)
- Параметры стиля, эмоции и динамики
- Криптографический хэш для проверки целостности

**Процесс работы (полностью оффлайн):**
1. **Кодирование** — локальный AI-энкодер на NPU смартфона создаёт метку.
2. **Передача** — метка отправляется по беспроводной сети.
3. **Декодирование** — AI-декодер генерирует контент, максимально близкий к оригиналу по смыслу и восприятию.

<grok-card data-id="02dc92" data-type="image_card" data-plain-type="render_searched_image"  data-arg-image_id="qn1Rt"  data-arg-size="LARGE" ></grok-card>


<grok-card data-id="926e53" data-type="image_card" data-plain-type="render_searched_image"  data-arg-image_id="KMym7"  data-arg-size="LARGE" ></grok-card>


<grok-card data-id="7c48b6" data-type="image_card" data-plain-type="render_searched_image"  data-arg-image_id="jQtk6"  data-arg-size="LARGE" ></grok-card>


## 2. Беспроводные протоколы передачи меток

Благодаря малому размеру меток и модульной архитектуре система поддерживает разные протоколы как WASM-плагины:

**LoRa (базовый модуль для дальней связи)**
- Дальность: до 10–50 км в сельской местности.
- Низкое энергопотребление, store-and-forward.

<grok-card data-id="9df0ca" data-type="image_card" data-plain-type="render_searched_image"  data-arg-image_id="ozzzm"  data-arg-size="LARGE" ></grok-card>


<grok-card data-id="bfb5cb" data-type="image_card" data-plain-type="render_searched_image"  data-arg-image_id="qKgu9"  data-arg-size="LARGE" ></grok-card>


**Wi-Fi HaLow и BLE Mesh (средняя дальность и плотные сети)**
- Wi-Fi HaLow: до 1 км, выше скорость чем LoRa.
- BLE Mesh / Thread: низкое потребление, хорошая масштабируемость в городах и помещениях.

**Free-Space Optics (FSO — высокоскоростной модуль)**
- Лазерная связь через воздух.
- Скорость до нескольких Гбит/с — метки передаются мгновенно.
- Ограничение: требует прямой видимости, чувствителен к погоде.

<grok-card data-id="473f9a" data-type="image_card" data-plain-type="render_searched_image"  data-arg-image_id="DbkBw"  data-arg-size="LARGE" ></grok-card>


<grok-card data-id="dd7546" data-type="image_card" data-plain-type="render_searched_image"  data-arg-image_id="OrUlz"  data-arg-size="LARGE" ></grok-card>


**Умная маршрутизация меток**
- **Semantic-Aware Routing** — AI анализирует смысл и приоритет метки перед ретрансляцией.
- **Multi-Path Routing** — критические метки идут по нескольким путям одновременно.
- **Reputation-based Routing** — предпочтение надёжным узлам с хорошей репутацией и энергоснабжением.

<grok-card data-id="c86ab0" data-type="image_card" data-plain-type="render_searched_image"  data-arg-image_id="pb5mP"  data-arg-size="LARGE" ></grok-card>


<grok-card data-id="a93a8c" data-type="image_card" data-plain-type="render_searched_image"  data-arg-image_id="DbUtc"  data-arg-size="LARGE" ></grok-card>
