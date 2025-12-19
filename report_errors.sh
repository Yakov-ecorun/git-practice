#!/bin/bash

LOG="logs/monitor.log"

# 1. Проверка наличия лога
if [ ! -f "$LOG" ]; then
    echo "Log file not found"
    exit 1
fi

# 2. Подсчёт ошибок
ERRORS=$(grep ERROR "$LOG" | wc -l)

# 3. Вывод и exit code
if [ "$ERRORS" -gt 0 ]; then
    echo "Errors detected: $ERRORS"
    exit 1
else
    echo "No errors detected"
    exit 0
fi

