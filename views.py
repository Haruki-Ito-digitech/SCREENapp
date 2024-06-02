from __init__ import app
from flask import Flask, request, render_template, send_from_directory
from flask_socketio import SocketIO, emit
from __init__ import app, socketio

# 最初の画面への遷移
@app.route('/')
def index():
    # return send_from_directory('static', 'index.html') # staticフォルダのindex.html
    return render_template('test.html') # templateフォルダのindex.html

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

# @socketio.on('message', namespace='/demo')
# def handle_message(message):
#     emit('message', f'{request.sid} => {message}', namespace='/demo', broadcast=True)

@socketio.on('screenshot')
def handle_screenshot(data):
    screenshot_data = data['data']
    print("Received screenshot data of length:", len(screenshot_data))
    emit('screenshot', {'data': screenshot_data}, broadcast=True)

