#!/bin/bash

echo "Starting monitoring..."

python3 src/app.py
STATUS=$?

if [ "$STATUS" -eq 0 ]; then
    echo "All sites are OK"
else
    echo "Some sites are DOWN"
fi
