import sys
import requests

URL = "https://example.com"

try:
    r = requests.get(URL, timeout=5, verify="/etc/ssl/certs/ca-certificates.crt")
    if r.status_code == 200:
        print(f"✅ {URL} is UP")
        sys.exit(0)
    else:
        print(f"⚠️ Status: {r.status_code}")
        sys.exit(1)
except Exception as e:
    print(f"❌ Error: {e}")
    sys.exit(1)