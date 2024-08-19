#!/bin/bash


echo "The script you are running has:"
echo "basename: [$(basename "$0")]"
echo "dirname : [$(dirname "$0")]"
echo "pwd     : [$(pwd)]"
echo ""
echo "mkdir $(dirname "$0")/venv"

#mkdir venv
#python3 -m venv venv/
#pip install -r requirements.txt