"""
Drives the car to desires direction
communicates with compass and gps modules
"""
################# import
import config
import motor
import time
import ultrasonic
import line_follower_cv
import camera
import multiprocessing

################# objects
car_obj = motor.Car(config.MTR_R_PIN, config.MTR_L_PIN)
us_obj = ultrasonic.UltraSonic(config.US_TRIG_PIN, config.US_ECHO_PIN)
cam_obj = camera.Camera(0)
line_flag = multiprocessing.Value("i",0)

################# pilot class
def follow_line():
    while True:
        while line_flag.value == 1 && !us_obj.is_blocked():
            dir = line_follower_cv.get_direction()
            car_obj.line_follow(dir)
            print(dir)
        time.sleep(5)

class Pilot():
    def __init__(self, dbg = config.DEBUG_MODE ):
        self.dbg = dbg
        self.line_p = multiprocessing.Process(target= follow_line)
        self.line_p.start()


    def line_move(self):
        if self.dbg:
            print("[AUTO] moving on line")
        global line_flag
        line_flag.value = 1

    def line_stop(self):
        if self.dbg:
            print("[AUTO] stopped on line")
        global line_flag
        line_flag.value = 0
        car_obj.stop()

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
    p = Pilot()
    print("started")
    time.sleep(5)
    print("line move")
    p.line_move()
    time.sleep(5)
    print("line stop")
    p.line_stop()
