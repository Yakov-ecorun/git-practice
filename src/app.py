import subprocess
import json
import logging
import subprocess
import json
import logging
import time
from pathlib import Path
import sys
import yaml

# ==============================
# 1. Загружаем YAML-конфиг
# ==============================

CONFIG_YAML = Path("config/app.yml")

if not CONFIG_YAML.exists():
    print("config/app.yml not found")
    sys.exit(1)

with open(CONFIG_YAML) as f:
    app_config = yaml.safe_load(f)

# ==============================
# 2. Настройка логирования из YAML
# ==============================

LOG_FILE = app_config["logging"]["file"]
LOG_LEVEL = app_config["logging"]["level"]

logging.basicConfig(
    filename=LOG_FILE,
    level=LOG_LEVEL,
    format="%(asctime)s %(levelname)s %(message)s"
)

# ==============================
# 3. Читаем interval из YAML
# ==============================

INTERVAL = app_config["app"]["interval"]

# ==============================
# 4. Загружаем servers.json
# ==============================

SERVERS_FILE = Path(app_config["data"]["servers_file"])

if not SERVERS_FILE.exists():
    logging.error("servers.json not found")
    sys.exit(1)

with open(SERVERS_FILE) as f:
    servers = json.load(f)

# ==============================
# 5. Функции проверок
# ==============================

def ping_host(host):
    result = subprocess.run(
        ["ping", "-c", "1", host],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    return result.returncode == 0


def check_http(url):
    result = subprocess.run(
        ["curl", "-I", "-s", url],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL
    )
    return b"200" in result.stdout or b"301" in result.stdout


# ==============================
# 6. Основная проверка
# ==============================

def run_checks():
    failed = False

    for server in servers:
        name = server["name"]
        host = server["host"]
        url = server["url"]

        if not ping_host(host):
            logging.error(f"{name} PING FAIL")
            failed = True
            continue

        if not check_http(url):
            logging.error(f"{name} HTTP FAIL")
            failed = True
            continue

        logging.info(f"{name} OK")

    return failed


# ==============================
# 7. Определяем режим запуска
# ==============================

MODE = "once"

if "--loop" in sys.argv:
    MODE = "loop"

# ==============================
# 8. Запуск
# ==============================

if MODE == "once":
    failed = run_checks()
    sys.exit(1 if failed else 0)

if MODE == "loop":
    while True:
        run_checks()
        time.sleep(INTERVAL)
