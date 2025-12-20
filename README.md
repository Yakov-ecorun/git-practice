# DevOps Learning Project

## Project Overview

This repository is a **learning DevOps project** where I practice Linux, Bash, Git, and Python for automation and monitoring tasks.

The project demonstrates:
- Bash and Python automation
- basic service monitoring
- correct usage of **exit codes** for automation
- scripts ready for CI/CD, cron, and Docker usage
- clean and structured Git workflow

---

## Implemented Features

- Python script for server availability monitoring
- Bash scripts for orchestration and checks
- Logging of monitoring results
- Configuration via JSON file
- All scripts return meaningful exit codes (`0` / `1`)

Automation example:

```bash
./run_monitor.sh || echo "ALERT!"

## Project Structure

```
git-practice/
├── src/app.py        # Python monitoring script
├── *.sh              # Bash automation scripts
├── servers.json      # Configuration
├── logs/             # Logs
└── README.md
```

## Technologies Used

Linux

Bash

Git / GitHub

Python

JSON

subprocess, logging

## Result

The project is functional, automated, and ready for real DevOps workflows
such as CI/CD pipelines, cron jobs, and containerized environments.

