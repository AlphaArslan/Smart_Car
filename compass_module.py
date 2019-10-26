"""
this module communicates with the compass (magnetometer) module QCM5883l
"""
import py_qmc5883l

class Compass():
    def __init__(self):
        self.compass = py_qmc5883l.QMC5883L()


    def get_heading_angle(self):
        return self.compass.get_magnet()
