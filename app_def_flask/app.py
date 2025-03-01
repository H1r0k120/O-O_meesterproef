from flask import Flask, render_template
from flask_socketio import SocketIO
import time
import threading
from lln import read_rfid
from lln2atk import get_authenticationtoken
from table import get_tabledata
import webbrowser

app = Flask(__name__, static_folder='templates')
socketio = SocketIO(app)

previous_token = None
x = None

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("connect")
def send_initial_data(auth=None):
    global x
    if not x.empty:
        #print("Eerste data versturen:", x.to_json())  # Debug
        socketio.emit("update_data", {"data": x.to_json()}, to=None)

def rfid_loop():
    global x, previous_token
    while True:
        lln = read_rfid()
        atoken = get_authenticationtoken(lln)
        if atoken and atoken != previous_token:
            x = get_tabledata(atoken)
            previous_token = atoken
                    
            socketio.emit("update_data", {"schedule": x.to_json(orient="records")}) 

        time.sleep(1)



if __name__ == "__main__":
    threading.Thread(target=rfid_loop, daemon=True).start()
    webbrowser.open("http://127.0.0.1:5000")
    socketio.run(app, port=5000, debug=True)