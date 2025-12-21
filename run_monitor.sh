#!/bin/bash

echo "Starting monitoring..."

python3 src/app.py

STATUS=$?

if [ $STATUS -ne 0 ]; then
    echo "Some services are DOWN"
    exit 1
fi

echo "All services are UP"
exit 0
