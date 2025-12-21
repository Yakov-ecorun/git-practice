import subprocess
import json
import logging
import time
from pathlib import Path
import sys

# Настройка логирования
logging.basicConfig(
    filename="logs/monitor.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

CONFIG_FILE = Path("servers.json")

if not CONFIG_FILE.exists():
    logging.error("servers.json not found")
    sys.exit(1)

with open(CONFIG_FILE) as f:
    servers = json.load(f)

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

if failed:
    sys.exit(1)

sys.exit(0)
