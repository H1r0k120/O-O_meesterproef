import time
import threading
import webview
from lln import read_rfid
from lln2atk import get_authenticationtoken
from table import get_tabledata
import json


class Api:
    def __init__(self):
        self.previous_token = None

    def start_rfid_loop(self):
        #print("starting rfid loop")
        threading.Thread(target=self._rfid_loop, daemon=True).start()

    def _rfid_loop(self):
        while True:
            #print("enter loop")
            lln = read_rfid()
            #print(lln)
            atoken = get_authenticationtoken(lln)
            #print(atoken)
            if atoken and atoken != self.previous_token:
                data = get_tabledata(atoken)
                #print(data)
                self.previous_token = atoken

                json_data = json.dumps(data) if isinstance(data, str) else data.to_json(orient="records")
                
                webview.windows[0].evaluate_js(f"updateTable({json_data})")

            time.sleep(2)  # Prevent excessive looping

if __name__ == "__main__":
    api = Api()
    window = webview.create_window("Schedule", "templates/index.html", js_api=api)

    webview.start(api.start_rfid_loop)