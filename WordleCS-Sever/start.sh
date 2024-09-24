#!/bin/bash

if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

source venv/bin/activate

echo "Installing dependencies..."
pip install --require-virtualenv -q Flask==3.0.3


echo "Starting Flask server..."
export FLASK_APP=app.py  # Replace with the name of your Python file if not app.py
export FLASK_ENV=development  # Set to 'production' for production mode
flask run

deactivate
