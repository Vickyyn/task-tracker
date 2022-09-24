# !/bin/bash

if ! [[ -x "$(command -v python3)" ]]
then
    echo "Error:
        This program needs Python 3 to run. Please check out https://www.python.org/downloads/ to install" >&2 
    exit 1
elif ! [[ -x "$(command -v pip)" ]]
then
    echo "error:
        This program needs pip to help install dependencies. Please check out https://packaging.python.org/en/latest/tutorials/installing-packages/ to install" >&2
    exit 1
else
    python3 -m venv venv
    source venv/bin/activate
    pip install -r src/requirements.txt | grep -v 'already satisfied'
    python3 src/main.py
fi

