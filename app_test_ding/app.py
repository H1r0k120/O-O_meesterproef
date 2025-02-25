#!/usr/bin/env python3
from flask import Flask, render_template
from flask_socketio import SocketIO
import threading
import time
import lln
from lln2atk import get_authenticationtoken

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

def rfid_loop():
    """Blijft RFID lezen en stuurt het via WebSockets naar de frontend"""
    while True:
        lln = lln.read_rfid()
        atoken = get_authenticationtoken(lln)
        time.sleep(1)  # Vermijd overbelasting


if __name__ == "__main__":
    # Start RFID in een aparte thread
    threading.Thread(target=rfid_loop, daemon=True).start()

    # Start de Flask-server
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
