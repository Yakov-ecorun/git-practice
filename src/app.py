import subprocess

sites = ["google.com", "github.com", "nosite.local"]

for site in sites:
    result = subprocess.run(
        ["ping", "-c", "1", site],
        stdout=subprocess.DEVNULL,
	stderr=subprocess.DEVNULL
    )

    if result.returncode == 0:
        print(site, "OK")
    else:
        print(site, "FAIL")
