"""
This module communicates with the GPS module
Ublox Neo 6m
https://www.instructables.com/id/Raspberry-Pi-the-Neo-6M-GPS/
"""

# serial interface is /dev/serial0
# it takes some seconds before getting results
# tested and working

import serial
import pynmea2
import time

class GPS():
    def __init__(self):
        self.serial_port = serial.Serial("/dev/serial0", 9600, timeout=0.5)

    def get_location(self):
        """
        returns (latitude, longitude)
        """
        str = self.serial_port.readline()
        while (str.find('GGA') == 0):
            print("waitng for GPS data")
            time.sleep(0.5)
            str = self.serial_port.readline()
            
        msg = pynmea2.parse(str)
        return msg
        # latitude = 0
        # longitude = 0
        #
        # return (latitude, longitude)
