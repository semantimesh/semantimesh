#!/bin/bash
echo "Запуск блокчейн‑ноды СемантикМеш..."
cd src/blockchain
python3 consensus.py &
python3 storage.py
echo "Блокчейн‑нода запущена!"
