#!/bin/bash
FLASK_DEBUG=1 \
python3 -m flask -A flaskr/main.py -e .env run