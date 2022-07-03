#!/bin/bash


echo "-- attempting to copy config.json to ./"
cp ../../config.json .

echo "-- attempting to copy local.config.json to ./"
cp ../../local.config.json .

port=${1:-8000}
echo "-- running uvicorn server on port {$port}"
python -m uvicorn --reload main:app --port "${port}"