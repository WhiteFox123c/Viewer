#!/bin/bash

if command -v python3 &> /dev/null
then
    python3 -m venv venv
else
    python -m venv venv
fi

chmod +x ./venv/bin/activate
./venv/bin/activate

pip install -r requirements.txt
