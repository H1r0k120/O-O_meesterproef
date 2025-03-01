#!/usr/bin/env python3
#import MFRC522
import json
import time

# RFID Scanner Setup
#mfrc = MFRC522.MFRC522()

# RFID Database
llnJSON = '{"C3FBA9D140":"08060", "338F0A71B":"Blauwe chip", "F31538ED0":"Witte kaart", "None":"Datiskut", "F3E9ACD167":"08099", "54E7B74044":"08078", "3081AF31D":"08153"}'
llnPy = json.loads(llnJSON)

def right_CardID(cardID):
    """Formatteer de kaart-ID naar hexadecimaal"""
    return "%2X%2X%2X%2X%2X" % (cardID[0], cardID[1], cardID[2], cardID[3], cardID[4])


'''
def read_rfid():
    """Leest een RFID-kaart en geeft de ID en naam terug"""
    while True:
        (status, _) = mfrc.MFRC522_Request(mfrc.PICC_REQIDL)
        if status == mfrc.MI_OK:
            pass

        (status, uid) = mfrc.MFRC522_Anticoll()
        if status == mfrc.MI_OK:
            card_str = right_CardID(uid)
            student = llnPy.get(card_str, "Onbekende kaart")

            print(f"Gescannde kaart: {card_str} - {student}")
            return {"card_id": card_str, "student": student}

        time.sleep(1)  # Voorkomt CPU-overbelasting
'''

def read_rfid():
    return "08078"

