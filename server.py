from __init__ import app, socketio
import os

if __name__ == '__main__':
    socketio.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))