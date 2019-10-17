"""
this module communicates with the compass (magnetometer) module HMC5883L
- It uses I2C protocol
- https://github.com/ControlEverythingCommunity/HMC5883/blob/master/Python/HMC5883.py
"""

import smbus		#import SMBus module of I2C
from time import sleep  #import sleep
import math

# Registers and their Address
Register_A     = 0              #Address of Configuration register A
Register_B     = 0x01           #Address of configuration register B
Register_mode  = 0x02           #Address of mode register

X_axis_H    = 0x03              #Address of X-axis MSB data register
Z_axis_H    = 0x05              #Address of Z-axis MSB data register
Y_axis_H    = 0x07              #Address of Y-axis MSB data register
declination = -0.00669          #define declination angle of location where measurement going to be done
pi          = 3.14159265359     #define pi value


class Compass():
    def __init__(self, device_add):
        self.bus = smbus.SMBus(1) 	            # or bus = smbus.SMBus(0) for older version boards
        self.Device_Address = device_add        # HMC5883L magnetometer device address

        #write to Configuration Register A
        self.bus.write_byte_data(Device_Address, Register_A, 0x70)

        #Write to Configuration Register B for gain
        self.bus.write_byte_data(Device_Address, Register_B, 0xa0)

        #Write to mode Register for selecting mode
        self.bus.write_byte_data(Device_Address, Register_mode, 0)


    def read_raw_data(self, addr):
        #Read raw 16-bit value
        high = self.bus.read_byte_data(Device_Address, addr)
        low = self.bus.read_byte_data(Device_Address, addr+1)

        #concatenate higher and lower value
        value = ((high << 8) | low)

        #to get signed value from module
        if(value > 32768):
            value = value - 65536
        return value


    def get_heading_angle(self):
        """
        0 for north
        increases clockwise
        """
        #Read Accelerometer raw value
        x = self.read_raw_data(X_axis_H)
        z = self.read_raw_data(Z_axis_H)
        y = self.read_raw_data(Y_axis_H)

        heading = math.atan2(y, x) + declination

        #Due to declination check for >360 degree
        if(heading > 2*pi):
                heading = heading - 2*pi

        #check for sign
        if(heading < 0):
                heading = heading + 2*pi

        #convert into angle
        heading_angle = int(heading * 180/pi)

        print ("Heading Angle = %d°" %heading_angle)

        return heading_angle
