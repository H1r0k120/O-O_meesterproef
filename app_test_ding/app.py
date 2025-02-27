#!/usr/bin/env python3
from flask import Flask, render_template
from flask_socketio import SocketIO
import time
import threading
from lln import read_rfid
from lln2atk import get_authenticationtoken
from table import get_tabledata

app = Flask(__name__)
socketio = SocketIO(app)

previous_token = None
x = None

@app.route("/")
def index():
    return render_template("index.html")

def rfid_loop():
    global x, previous_token
    while True:
        lln = read_rfid()
        atoken = get_authenticationtoken(lln)
        if atoken and atoken != previous_token:
            x = get_tabledata(atoken)
            previous_token = atoken
        time.sleep(1)


if __name__ == "__main__":
    # Start RFID in een aparte thread
    threading.Thread(target=rfid_loop, daemon=True).start()

    # Start de Flask-server
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
    