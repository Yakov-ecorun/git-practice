#!/bin/bash

FILE="servers.json"

if [ -f "$FILE" ]; then
    echo "File $FILE exists"
else
    echo "File $FILE not found"
fi
