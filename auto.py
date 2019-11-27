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

################# objects
car_obj = motor.Car(config.MTR_R_PIN, config.MTR_L_PIN)
us_obj = ultrasonic.UltraSonic(config.US_TRIG_PIN, config.US_ECHO_PIN)

################# pilot class

class Pilot():
    def __init__(self, dbg = config.DEBUG_MODE ):
        self.dbg = dbg

    def follow_line(self):
        f = 0
        ft = 0
        for i in range(150):
             
            print(">>{}".format(i))
            dir = line_follower_cv.get_direction()
            if dir == None:
                print("Can't find the line")
                if f == 0:
                    car_obj.move_backward()
                    time.sleep(0.4)
                    car_obj.stop()
                    time.sleep(1.5)
                    f =1
                elif f == 1:
                    car_obj.turn_right()
                    time.sleep(1)
                    car_obj.stop()
                    time.sleep(1.5)
                    f = 2
                elif f == 2:
                    car_obj.turn_left()
                    time.sleep(1.4)
                    car_obj.stop()
                    time.sleep(1.5)
                    f = 3
                elif f == 3 :
                    f = 0
                    ft = ft + 1
                    dir = line_follower_cv.get_direction()
                    dir = line_follower_cv.get_direction()
                    dir = line_follower_cv.get_direction()
                    if ft == 3:
                        break
                    time.sleep(3)
                continue
            f = 0
            ft = 0
            x = 8
            if dir > x:
                dir = x
            elif dir < -x:
                dir = -x
            print(dir)
            car_obj.line_follow(dir)
            time.sleep(0.5 + 0.36*abs(dir))
            car_obj.move_forward(sped= 18 + (x-abs(dir))*1.3)
            time.sleep(0.18 + (x-abs(dir))*0.1)
            
    def follow_line2(self):
        for _ in range(10):
            car_obj.turn_left()
            while line_follower_cv.get_direction() < -1:
                print("left")
                time.sleep(0.1)
            car_obj.turn_right()
            while line_follower_cv.get_direction() > 1:
                print("right")
                time.sleep(0.1)
            car_obj.move_forward()
            while abs(line_follower_cv.get_direction()) < 1.01:
                print("forward")
                time.sleep(0.1)
        

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
    print("m")
    p = Pilot()
    #p.follow_line()
    #car_obj.stop()
    #exit()
    try:
        p.follow_line()
    except Exception as e:
        print(e)
    car_obj.stop()
    p.stop()


