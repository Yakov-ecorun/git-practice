import subprocess
import json
import logging
from pathlib import Path
import sys

# 1. Логирование
logging.basicConfig(
    filename="logs/monitor.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

# 2. Проверка конфигурации
config_file = Path("servers.json")

if not config_file.exists():
    logging.error("servers.json not found")
    sys.exit(1)

# 3. Чтение JSON → dict / list
with open(config_file) as f:
    sites = json.load(f)

failed = False

# 4. ОДИН проход проверки
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

# 5. Exit code для Bash / CI
if failed:
    sys.exit(1)
else:
    sys.exit(0)

