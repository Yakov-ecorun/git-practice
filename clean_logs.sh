#!/bin/bash

LOG="logs/monitor.log"
MAX_SIZE=10485760  # 10 MB

if [ -f "$LOG" ]; then
    SIZE=$(stat -c%s "$LOG")

    if [ "$SIZE" -gt "$MAX_SIZE" ]; then
        echo "Log is too big, cleaning"
        > "$LOG"
    else
        echo "Log size is OK"
    fi
else
    echo "Log file not found"
fi
