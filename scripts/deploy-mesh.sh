#!/!/bin/bash
echo "Запуск mesh‑узла СемантикМеш..."
cd src/mesh-network
python3 discovery.py &
python3 sync.py
echo "Mesh‑узел запущен!"
