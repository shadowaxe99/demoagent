
import os
import subprocess
from flask import Flask, request, jsonify
from utils import compile_code

app = Flask(__name__)

@app.route('/compile', methods=['POST'])
def compile():
    data = request.get_json()
    language = data.get('language')
    code = data.get('code')

    if not language or not code:
        return jsonify({'error': 'Missing language or code'}), 400

    try:
        result = compile_code(language, code)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
