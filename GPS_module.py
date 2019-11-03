"""
This module communicates with the GPS module
Ublox Neo 6m
https://www.instructables.com/id/Raspberry-Pi-the-Neo-6M-GPS/
"""

# serial interface is /dev/serial0
# it takes some seconds before getting results
# tested and working
# stty -F /dev/serial0 9600
# sudo gpsd /dev/serial0 -F /var/run/gpsd.sock
# cgps -s

import serial
import pynmea2
import time
import config
class GPS():
    def __init__(self, dbg= config.DEBUG_MODE):
        self.dbg = dbg
        self.serial_port = serial.Serial("/dev/serial0", 9600, timeout=0.5)

    def get_location(self):
        """
        returns (latitude, longitude)
        """
        if self.dbg:
            print("[GPS] getting gps location")

        str = self.serial_port.readline().decode("utf-8")
        #print(str)

        while not "$GPRMC" in str:
            str = self.serial_port.readline().decode("utf-8")
            #print(str)

        msg = pynmea2.parse(str)

        loc = (0, 0)
        if self.dbg:
            print("[GPS] gps location: {}".format(loc))

        return msg

##########################################


if __name__ == '__main__':
    gps = GPS(dbg=False)
    while True:
        data = gps.get_location()
        print(data)
        print(data.lat, data.lat_dir, "  ", data.lon, data.lon_dir)
        #print(data.lon, data.lon_dir)
