import pandas as pd
from zermelo import Client


cl = Client("keizerkarelcollege")
#token = cl.authenticate("281 290 789 391")

#acc_token = token["access_token"]
acc_token = "8jcm5uhbpn9nogsl7kcickuaq1"

appointment = cl.get_appointments(acc_token, 1736492400, 1736546400)
usercode = cl.get_user(acc_token)["response"]["data"][0]["code"]
enroll = cl.get_liveschedule(acc_token, 202502, usercode)

print(acc_token)
print(appointment)
print(enroll)
