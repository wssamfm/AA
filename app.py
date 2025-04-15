import os
from flask import Flask, request, jsonify
from subprocess import Popen

app = Flask(__name__)
current_process = None

@app.route('/')
def home():
    return "✅ API is running!"

@app.route('/attack', methods=['POST'])
def attack():
    global current_process
    try:
        data = request.get_json()
        method = data.get('method')
        host = data.get('host')
        port = data.get('port')

        if not all([method, host, port]):
            return jsonify({'error': 'Missing parameters'}), 400

        method_file = f"methods/{method}.py"
        if not os.path.exists(method_file):
            return jsonify({'error': f'Method {method} not found'}), 404

        if current_process is not None:
            return jsonify({'error': 'Attack already running'}), 400

        current_process = Popen(["python", method_file, host, str(port)])
        return jsonify({'status': 'attack_started'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/stop', methods=['POST'])
def stop():
    global current_process
    try:
        if current_process:
            current_process.kill()
            current_process = None
            return jsonify({'status': 'attack_stopped'})
        return jsonify({'error': 'No running attack'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)