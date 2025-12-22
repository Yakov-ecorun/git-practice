#!/bin/bash

# Run the monitoring script once
python3 src/app.py --once
STATUS=$?

# Check exit code
if [ $STATUS -ne 0 ]; then
  echo "Problems detected"
  exit 1
fi

echo "All services are healthy"
exit 0
