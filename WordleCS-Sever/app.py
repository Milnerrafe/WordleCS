from flask import Flask, jsonify
import sys
import subprocess
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_data():
    try:
        result = subprocess.run([sys.executable, 'database.py'], capture_output=True, text=True)
        json_data = json.loads(result.stdout)
        return jsonify(json_data), 200
    except FileNotFoundError:
        return jsonify({'error': 'File not found'}), 404
    except json.JSONDecodeError:
        return jsonify({'error': 'Invalid JSON format from script'}), 500

if __name__ == '__main__':
    app.run(debug=False)
