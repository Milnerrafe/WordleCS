#!/bin/bash

echo "Installing dependencies globally..."
pip install Flask

echo "Starting Flask server..."
export FLASK_APP=app.py
export FLASK_ENV=production
flask run
