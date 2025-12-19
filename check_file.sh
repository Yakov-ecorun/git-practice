#!/bin/bash

FILE="servers.json"

if [ -f "$FILE" ]; then
    echo "File $FILE exists"
    exit 0
else
    echo "File $FILE not found"
    exit 1
fi
