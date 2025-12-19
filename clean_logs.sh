#!/bin/bash

LOG="logs/monitor.log"
MAX_SIZE=10485760  # 10 MB

if [ ! -f "$LOG" ]; then
    echo "Log file not found"
    exit 1
fi

SIZE=$(stat -c%s "$LOG")

if [ "$SIZE" -gt "$MAX_SIZE" ]; then
    echo "Log is too big, cleaning"
    > "$LOG"
    exit 0
else
    echo "Log size is OK"
    exit 0
fi
