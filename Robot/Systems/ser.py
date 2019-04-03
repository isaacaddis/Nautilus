
import time
import serial
import math
import numpy as np
import PySide.QtCore as q

#Start serial coms
ser = serial.Serial('/dev/ttyUSB0',57600,timeout=1)
ser.isOpen()

'''
    Loop for capturing serial output of Arduino and passing it to the GUI
'''
def clean_up(text):
    #print("String: {}".format(text)) # for debugging
    #print("Type: {}".format(type(text)))
    if type(text) == str and not (text == 'NAN'):
        try:
            return float(text.replace(" ",""))
        except ValueError:
            return ""
    else:
        return 0.00
def leak_text(text):
    if text.isdigit(): 
        if int(text) is 0:
            return 'Not leaking'
        elif int(text) is 1:
            return 'Leaking!'
    else:
        return 'NaN'
while True:
        try:
            msg = ser.readline().decode('utf-8')
        except UnicodeError:
            msg = ""
        if msg: 
            split = msg.split(",")
            if len(split) == 6 and not ' \r\n' in split:
                print("MSG: {}".format(msg))
                t_housing_in = split[0]
                t_housing_out = split[1]
                h_housing_in = split[2] #humidity
                leak_sensor = split[3]
                x = split[4]
                y = split[5]
                cleaned_t_housing_in = round(clean_up(t_housing_in), 1)
                cleaned_t_housing_out = clean_up(t_housing_out)
                cleaned_h_housing_in = round(clean_up(t_housing_out), 1)
                print("Temperature inside housing: {}°C".format(cleaned_t_housing_in))
                print("Temperature outside housing: {}°C".format(cleaned_t_housing_out))
                print("Humidity inside housing: {}%".format(cleaned_h_housing_in))
                print("Leak sensor: {}".format(leak_text(leak_sensor)))
                print("X: {}".format(clean_up(x)))
                print("Y: {}".format(clean_up(y)))
