import pandas as pd
from zermelo import Client


cl = Client("keizerkarelcollege")
token = cl.authenticate("116 447 098 208")

acc_token = token["access_token"]

appointment = cl.get_appointments(acc_token, 1736492400, 1736546400)
usercode = cl.get_user(acc_token)["response"]["data"][0]["code"]
enroll = cl.get_liveschedule(acc_token, 202502, usercode)

print(acc_token)
print(appointment)
print(enroll)
