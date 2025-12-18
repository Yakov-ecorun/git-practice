import subprocess
import json
import logging
import time
from pathlib import Path

# 1. Настройка логирования
logging.basicConfig(
    filename="logs/monitor.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

# 2. Проверка файла конфигурации
config_file = Path("servers.json")

if not config_file.exists():
    logging.error("servers.json not found")
    exit(1)

# 3. Чтение JSON → dict
with open(config_file) as f:
    sites = json.load(f)

# 4. Основной цикл мониторинга
try:
    while True:
        failed = False

        for site in sites:
            result = subprocess.run(
                ["ping", "-c", "1", site],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

            if result.returncode == 0:
                logging.info(f"{site} OK")
            else:
                logging.error(f"{site} FAIL")
                failed = True

        time.sleep(10)

except KeyboardInterrupt:
    logging.info("Monitoring stopped by user")

