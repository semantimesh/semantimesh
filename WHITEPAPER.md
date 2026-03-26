<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SemantiMesh — Семантическая беспроводная сеть будущего</title>
    <style>
        body { 
            font-family: system-ui, -apple-system, BlinkMacSystemFont, sans-serif; 
            margin: 0; 
            padding: 0; 
            background: #0a0a0f; 
            color: #e0e0e0; 
            line-height: 1.7;
        }
        .container { 
            max-width: 960px; 
            margin: 0 auto; 
            padding: 60px 20px; 
        }
        header {
            text-align: center;
            padding: 80px 20px 60px;
            border-bottom: 1px solid #222;
        }
        h1 { 
            font-size: 2.8rem; 
            margin: 0 0 12px 0; 
            color: #ffffff;
        }
        .subtitle {
            font-size: 1.35rem;
            color: #a0a0c0;
            max-width: 680px;
            margin: 0 auto;
        }
        .section {
            margin: 80px 0;
        }
        h2 {
            font-size: 1.85rem;
            margin-bottom: 24px;
            color: #ffffff;
        }
        .card-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 28px;
        }
        .card {
            background: #111118;
            padding: 32px 28px;
            border-radius: 12px;
            border: 1px solid #222;
        }
        .btn {
            display: inline-block;
            background: #00d4aa;
            color: #000;
            padding: 14px 32px;
            font-size: 1.1rem;
            font-weight: 600;
            border-radius: 8px;
            text-decoration: none;
            margin: 12px 8px 12px 0;
        }
        .btn-secondary {
            background: transparent;
            color: #00d4aa;
            border: 1px solid #00d4aa;
        }
        footer {
            text-align: center;
            padding: 60px 20px 40px;
            color: #666;
            font-size: 0.95rem;
        }
        a { color: #00d4aa; text-decoration: none; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>SemantiMesh</h1>
            <p class="subtitle">
                Семантическая беспроводная сеть для оффлайн-передачи информации и платежей
            </p>
            <div style="margin-top: 40px;">
                <a href="WHITEPAPER.md" class="btn" target="_blank">Читать Whitepaper</a>
                <a href="https://github.com/semantimesh" class="btn btn-secondary" target="_blank">GitHub</a>
            </div>
        </header>

        <div class="section">
            <h2>Технология семантических меток</h2>
            <p>
                SemantiMesh использует принципиально новый подход к передаче данных. 
                Вместо тяжёлых файлов система передаёт <strong>семантические метки</strong> — компактные математические представления смысла контента.
            </p>
            <p>
                AI-энкодер на устройстве отправителя сжимает видео, аудио или изображение в метку объёмом от нескольких сотен байт до десятков килобайт. 
                AI-декодер на приёмной стороне генерирует контент, который по смыслу и качеству максимально близок к оригиналу.
            </p>
            <p>
                Это позволяет передавать большие объёмы информации даже по низкоскоростным беспроводным каналам.
            </p>
        </div>

        <div class="section">
            <h2>Ключевые возможности</h2>
            <div class="card-grid">
                <div class="card">
                    <h3>Модульная архитектура</h3>
                    <p>Система построена как конструктор: любой протокол передачи (LoRa, оптические каналы и будущие технологии) подключается как плагин без перестройки всей сети.</p>
                </div>
                <div class="card">
                    <h3>AI Contributor Swarm</h3>
                    <p>Автономные AI-агенты анализируют вклад разработчиков и автоматически начисляют токены $SEMANTI.</p>
                </div>
                <div class="card">
                    <h3>SemantiPay</h3>
                    <p>Полностью оффлайн-платежи через беспроводную сеть с последующим settlement на блокчейне.</p>
                </div>
                <div class="card">
                    <h3>Гибкая этика</h3>
                    <p>Модуль гуманного поведения полностью настраивается пользователем — от полного отсутствия фильтров до строгих правил. Решение принимает сообщество через DAO.</p>
                </div>
            </div>
        </div>

        <div class="section">
            <h2>Fair Launch $SEMANTI</h2>
            <p>
                Токен-сэйл пройдёт только через сообщество. 55 % supply выделено на airdrop и points-программу. 
                Никаких предпродаж и инвесторов.
            </p>
            <p>
                Запускайте ноды, тестируйте модули, вносите вклад — получайте токены.
            </p>
        </div>

        <div class="section">
            <h2>Статус проекта</h2>
            <p>
                • US Provisional Patent Pending<br>
                • Разработка MVP и testnet (март–апрель 2026)<br>
                • Fair launch планируется на август 2026
            </p>
        </div>

        <footer>
            © 2026 SemantiMesh DAO • GPL-3.0 • 
            <a href="https://github.com/semantimesh">GitHub</a> • 
            Whitepaper • Семантическая беспроводная сеть будущего
        </footer>
    </div>
</body>
</html>
