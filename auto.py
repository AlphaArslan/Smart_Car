"""
Drives the car to desires direction
communicates with compass and gps modules
"""
################# import
import config
import motor
import time
import ultrasonic

################# objects
car_obj = motor.Car(config.MTR_R_PIN, config.MTR_L_PIN)
us_obj = ultrasonic.UltraSonic(config.US_TRIG_PIN, config.US_ECHO_PIN)


################# pilot class

class Pilot():
    def __init__(self, dbg = config.DEBUG_MODE ):
        self.dbg = dbg

    def forward(self):
        if self.dbg:
            print("[AUTO] moving forward")
        car_obj.move_forward()

    def backward(self):
        if self.dbg:
            print("[AUTO] moving backward")
        car_obj.move_backward()

    def right(self):
        if self.dbg:
            print("[AUTO] turning right")
        car_obj.turn_right()

    def left(self):
        if self.dbg:
            print("[AUTO] turning left")
        car_obj.turn_left()

    def stop(self):
        if self.dbg:
            print("[AUTO] stopped")
        car_obj.stop()

##############################################
if __name__ == '__main__':
    #print("m")

    #p = Pilot()
    car_obj.turn_left()
    time.sleep(2)
    car_obj.stop()
    #exit()
