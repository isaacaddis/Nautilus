
import time
import serial
import math
import numpy as np
import PySide.QtCore as q

class SerialUtil():
    #Start serial coms
    def __init__(self):
        print("initalized ser")
        self.ser = serial.Serial('/dev/ttyUSB0',57600,timeout=1)
        self.ser.isOpen()
        self.state = False
        self.mic_on = ['O','N']
        self.mic_off = ['O','F','F']
    def exit(self):
        self.ser.close()

    '''
        Loop for capturing serial output of Arduino and passing it to the GUI
    '''
    def clean_up(self, text):
        #print("String: {}".format(text)) # for debugging
        #print("Type: {}".format(type(text)))
        if type(text) == str and not (text == 'NAN'):
            try:
                return float(text.replace(" ",""))
            except ValueError:
                return ""
        else:
            return 0.00
    def leak_text(self, text):
        if text.isdigit(): 
            if int(text) is 0:
                return 'Not leaking'
            elif int(text) is 1:
                return 'Leaking!'
        else:
            return 'NaN'
    def send(self):
        msg = 1
        self.ser.write(msg)
        print("Sent: "+ str(msg))
    def get(self):
        
        msg = self.ser.readline().decode('utf-8')
        if msg is not None:
            #print(msg)
            msg = msg.replace('X', ',')
            msg = msg.replace('Y', ',')
            split = msg.split(",")
            if len(split) == 6 and not ' \r\n' in split:
                t_housing_in = split[0]
                t_housing_out = split[1]
                h_housing_in = split[2] #humidity
                leak_sensor = split[3]
                x = split[4]
                y = split[5]
                cleaned_t_housing_in = round(self.clean_up(t_housing_in), 1)
                cleaned_t_housing_out = self.clean_up(t_housing_out)
                cleaned_h_housing_in = round(self.clean_up(h_housing_in), 1)
                #print("Temperature inside housing: {}°C".format(cleaned_t_housing_in))
                #print("Temperature outside housing: {}°C".format(cleaned_t_housing_out))
                #print("Humidity inside housing: {}%".format(cleaned_h_housing_in))
                #print("Leak sensor: {}".format(self.leak_text(leak_sensor)))
                #print("X: {}".format(x))
                #print("Y: {}".format(y))
                return str(cleaned_t_housing_in),str(cleaned_t_housing_out), str(cleaned_h_housing_in), str(self.leak_text(leak_sensor)), str(x), str(y)
        else:
            return '0','0','0','0','0','0'