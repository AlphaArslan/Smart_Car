"""
this module communicates with the compass (magnetometer) module QCM5883l
follow X-axis
"""
# tested and working
# follow x direction

import py_qmc5883l
import math
import config

class Compass():
    def __init__(self):
        self.compass = py_qmc5883l.QMC5883L()
        self.compass.calibration = [[ 1.00000814e+00, -8.66306613e-04,  4.36383467e+03],
                                    [-8.66306613e-04,  1.09225136e+00,  3.61884567e+03],
                                    [ 0.00000000e+00,  0.00000000e+00,  1.00000000e+00]]
        self.compass.declination = 22.5

    def get_heading_angle(self, dbg = config.DEBUG_MODE):
        angle = self.compass.get_bearing()
        if dbg:
            print("[COMPASS] compass angle: {0:.2f}".format(angle))
        return angle
