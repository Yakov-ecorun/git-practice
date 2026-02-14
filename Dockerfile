
FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y iputils-ping curl \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir logs

COPY src/ src/
COPY config/ config/
COPY servers.json .
COPY run_monitor.sh .

RUN pip install pyyaml

CMD ["python3", "src/app.py"]
