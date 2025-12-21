# DevOps Learning Project

## Project Overview

This repository is a **hands-on DevOps learning project** built during the first 10 days of structured DevOps training.

The project focuses on **Linux fundamentals, Git workflows, Bash scripting, Python automation, and basic networking diagnostics**, and demonstrates how these tools work together in real DevOps-style automation.

The goal of the project is not only to learn individual tools, but to **build a complete automation workflow** similar to what is used in real production environments.

---

## What This Project Demonstrates

- Linux command-line proficiency
- Bash scripting for automation and orchestration
- Python scripting for monitoring and system checks
- Integration between Bash and Python
- Usage of **exit codes (`0` / `1`)** for automation logic
- Basic networking diagnostics (DNS, ICMP, HTTP)
- Logging and observability
- Separation of code and configuration
- Clean and structured Git workflow
- Scripts ready for **CI/CD, cron jobs, and Docker usage**

---

## Implemented Features

- Python-based monitoring script:
  - checks host availability using `ping`
  - checks HTTP services using `curl`
  - logs results to a file
  - returns proper exit codes for automation

- Bash scripts:
  - run and orchestrate Python scripts
  - react to failures using exit codes
  - prepare automation logic for cron / CI

- JSON-based configuration:
  - list of monitored services stored outside the code
  - easy to extend without code changes

- Logging:
  - all monitoring results written to log files
  - suitable for later analysis and alerting

---

## Automation Example

```bash
./run_monitor.sh || echo "ALERT!"
```

## Meaning

Run the monitoring system

If any service check fails (exit code ≠ 0), trigger an alert action

This pattern is commonly used in:

cron jobs

CI/CD pipelines

container health checks

## Project Structure

```
git-practice/
├── src/app.py        # Python monitoring script
├── *.sh              # Bash automation scripts
├── servers.json      # Configuration
├── logs/             # Logs
└── README.md
```

## Networking & Diagnostics

As part of this project, basic networking concepts and tools are used and understood:

DNS resolution (nslookup, dig)

Network reachability (ping)

HTTP diagnostics (curl, HTTP status codes)

Open ports inspection (ss)

## Git Workflow

The repository follows a clean and incremental Git workflow:

small, logical commits

clear commit messages describing what and why

separation of code, configuration, and documentation

Git history reflects real development steps

This approach makes the project easy to review for recruiters and engineers.

## Technologies Used

Linux

Bash

Git / GitHub

Python

JSON

Python modules:

subprocess

logging

pathlib

## Result

The project is functional, automated, and ready for real DevOps workflows
such as CI/CD pipelines, cron jobs, and containerized environments.

