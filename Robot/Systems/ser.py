
'''
    Modified serial intake code from 2018
'''
import time
import serial
import PySide.QtCore as q

#Start serial coms
ser = serial.Serial('/dev/ttyUSB0',57600,timeout=1)
ser.isOpen()

'''
    Loop for capturing serial output of Arduino and passing it to the GUI
'''
while True:
	try:
            msg = ser.readline().decode('utf-8')
            if len(msg)>0:
                print("MSG: {}".format(msg))
                if msg.startswith('['):
                    msg = msg[1:]
                    msg = msg[:len(msg)]
                #time.sleep(1)
	except KeyboardInterrupt:
		print("There was an error!")
		ser.close()
