from flask import Flask, request, render_template, redirect, json
from os import listdir
from time import time   
from pathlib import Path

app = Flask(__name__)

DATA_PATH = 'data'

@app.route('/', methods=["GET"])
def root():
    message_files = sorted(listdir(DATA_PATH))
    messages = map(lambda file: Path(DATA_PATH, file).read_text(), message_files)
    return render_template('index.html', messages = messages)

@app.route('/', methods=["POST"])
def post():
    data = request.get_data()
    Path(DATA_PATH, str(time())).write_text(data.decode())
    return '', 201

@app.route('/stats', methods=["GET"])
def stats_login():
    return render_template('stats_login.html', error = request.args.get('error') or "")

@app.route('/stats', methods=["POST"])
def stats():
    if request.form.get('login') !=  'szkola' or request.form.get('password') != 'security':
        return redirect('/stats?error=incorrect+login', code = 302)

    message_files = listdir(DATA_PATH)
    count = len(message_files)
    return render_template('stats.html', count = count)