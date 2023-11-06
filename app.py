from flask import Flask, render_template, request
import os
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run/<agent_name>', methods=['POST'])
def run_agent(agent_name):
    agent_dir = os.path.join('ai_agents', agent_name)
    subprocess.run(['python3', 'main.py'], cwd=agent_dir)
    return 'AI agent started'

if __name__ == '__main__':
    app.run(debug=True)