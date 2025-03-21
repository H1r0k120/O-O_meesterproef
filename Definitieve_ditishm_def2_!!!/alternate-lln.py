#!/usr/bin/env python3
########################################################################
# Filename    : RFID.py
# Description : Use MFRC522 read and write Mifare Card.
# auther      : www.freenove.com
# modification: 2021/1/1
########################################################################
from gpiozero import OutputDevice
import MFRC522
import json
import sys
import os

# Create an object of the class MFRC522
mfrc = MFRC522.MFRC522()

#Create database
llnJSON =  '{"C3FBA9D140":"8060", "338F 0A71B":"Blauwe chip", "F31538 ED0":"Witte kaart", "None":"Datiskut"}'

#parse lln
llnPy = json.loads(llnJSON)

def dis_ConmandLine():
	print ("RC522>",end="")
def dis_CardID(cardID):
	print ("%2X%2X%2X%2X%2X>"%(cardID[0],cardID[1],cardID[2],cardID[3],cardID[4]),end="")
def right_CardID(cardID):
	print ("%2X%2X%2X%2X%2X"%(cardID[0],cardID[1],cardID[2],cardID[3],cardID[4]),end="")


def loop():
	global mfrc3s
	while(True): 
		dis_ConmandLine()
		inCmd = input()
		if (inCmd == "scan"):
			print ("Scanning ... ")
			mfrc = MFRC522.MFRC522()
			isScan = True
			while isScan:
				# Scan for cards    
				(status,TagType) = mfrc.MFRC522_Request(mfrc.PICC_REQIDL)
				# If a card is found
				if status == mfrc.MI_OK:
					pass
				# Get the UID of the card
				(status,uid) = mfrc.MFRC522_Anticoll()				
				# If we have the UID, continue
				if status == mfrc.MI_OK:
					isscan = False
					# Select the scanned tag
					if mfrc.MFRC522_SelectTag(uid) == 0:
						print ("MFRC522_SelectTag Failed!")
					if cmdloop(uid) < 1 :
						isScan = False
			
		elif inCmd == "quit":
			destroy()
			exit(0)
		else :
			print ("\tUnknown command\n"+"\tscan:scan card and dump\n"+"\tquit:exit program\n")
				
def cmdloop(cardID):
	pass
	while(True):
		isScan = False
		
		#dis_ConmandLine()
		#dis_CardID(cardID)
		x = str("%2X%2X%2X%2X%2X"%(cardID[0],cardID[1],cardID[2],cardID[3],cardID[4]))
		#declare lln
		#lln = llnPy[x]
		print (x)
		print (llnPy[x])
		return 0.5
		
	
		
def destroy():
    print("Ending program")

if __name__ == "__main__":
	try:
		loop()
	except KeyboardInterrupt:  # Ctrl+C captured, exit
		destroy()
 
	

