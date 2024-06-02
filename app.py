from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")
CORS(app, supports_credentials=True, responses={r"/*": {"origins": "*"}})

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('screenshot')
def handle_screenshot(data):
    screenshot_data = data['data']
    print("Received screenshot data of length:", len(screenshot_data))
    emit('screenshot', {'data': screenshot_data}, broadcast=True)

if __name__ == '__main__':
    socketio.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
