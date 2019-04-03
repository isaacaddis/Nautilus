import time
import serial
import PySide.QtCore as q

#Start serial coms
ser = serial.Serial('/dev/ttyUSB0',57600,timeout=1)
ser.isOpen()

''' Remove whitespaces '''
def clean_up(text):
    return text.replace(" ", "")

#Execution     
while True:
	try:
            msg = ser.readline().decode('utf-8')
            if len(msg)>0:
                print("MSG: {}".format(msg))
                split = msg.split(',')#split by comma and remove whitespace
                tmp_inside_housing = clean_up(split[0])
                tmp_outside_housing = clean_up(split[1])
                hum_inside_housing = clean_up(split[2])
                leak_sensor = clean_up(split[3])
                x = clean_up(split[4])
                y = clean_up(split[5])
                print("Temperature Inside Housing: {}".format(tmp_inside_housing))
                print("Temperature Outside Housing: {}".format(tmp_outside_housing))
                print("Humidity Inside Housing: {}".format(hum_inside_housing))
                print("Leak Sensor: {}".format(leak_sensor))
                print("X: {}".format(x))
                print("Y: {}".format(y))
	except KeyboardInterrupt:
		print("There was an error!")
		ser.close()
