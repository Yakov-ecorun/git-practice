#!/bin/bash

ERRORS=$(grep ERROR logs/monitor.log | wc -l)

echo "Total errors: $ERRORS"
echo "$(date) Total errors: $ERRORS" >> logs/errors_summary.log
