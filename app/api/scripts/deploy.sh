#!/bin/bash

echo "-- deploying to production"

python -m uvicorn main:app --port 8000 --host 0.0.0.0