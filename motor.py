import config
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

class Motor():
    def __init__(self, pins_tuble):
        self.dir_pin, self.pwm_pin = pins_tuble
        GPIO.setup(self.dir_pin, GPIO.OUT)
        GPIO.setup(self.pwm_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pwm_pin, config.MTR_PWM_FREQ)
        self.pwm.start(0)

    def forward(self, speed= config.MTR_FRWRD_SPD ,diff = 0 ):
        GPIO.output(self.dir_pin, config.MTR_DIR_FORWARD)
        self.pwm.ChangeDutyCycle(speed + diff)

    def backward(self, speed= config.MTR_BKWRD_SPD ,diff = 0 ):
        GPIO.output(self.dir_pin, config.MTR_DIR_BACKWARD)
        self.pwm.ChangeDutyCycle(speed+ diff)

    def stop(self):
        self.pwm.ChangeDutyCycle(0)



class Car():
    def __init__(self, right, left):
        self.right_motor = Motor(right)
        self.left_motor = Motor(left)

    def move_forward(self, sped= config.MTR_FRWRD_SPD , dbg = config.DEBUG_MODE):
        if dbg :
            print("[CAR] moving forward")
        self.right_motor.forward(speed = sped)
        self.left_motor.forward(speed = sped, diff= config.MTR_RL_DIFF)

    def move_backward(self, dbg = config.DEBUG_MODE):
        if dbg :
            print("[CAR] moving backward")
        self.right_motor.backward()
        self.left_motor.backward(diff= config.MTR_RL_DIFF)

    def turn_right(self, dbg = config.DEBUG_MODE):
        if dbg :
            print("[CAR] turning right ")
        self.right_motor.backward()
        self.left_motor.forward(diff= config.MTR_RL_DIFF)

    def turn_left(self, dbg = config.DEBUG_MODE):
        if dbg :
            print("[CAR] turning left ")
        self.right_motor.forward()
        self.left_motor.backward(diff= config.MTR_RL_DIFF)

    def stop(self, dbg = config.DEBUG_MODE):
        if dbg :
            print("[CAR] stopping ")
        self.right_motor.stop()
        self.left_motor.stop()

    def line_follow(self, dir, dbg = config.DEBUG_MODE):
        if dbg :
            print("[CAR] following line")
        x = 10       
        if dir > 0:
            self.right_motor.backward(speed= x*dir)
            self.left_motor.forward(speed= x*dir )
        else:
            self.right_motor.forward(speed= -x*dir)
            self.left_motor.backward(speed= -x*dir )
            
    def test_move(self, prnt= False):
        if prnt:
            print("Forward")
        self.move_forward()
        sleep(3)
        self.stop()
        sleep(1)

        if prnt:
            print("Backward")
        self.move_backward()
        sleep(3)
        self.stop()
        sleep(1)

        if prnt:
            print("Right")
        self.turn_right()
        sleep(3)
        self.stop()
        sleep(1)

        if prnt:
            print("Left")
        self.turn_left()
        sleep(3)
        
        self.stop()

################################################
if __name__ == '__main__':

    car_obj = Car(config.MTR_R_PIN, config.MTR_L_PIN)

    car_obj.line_follow(-8)
    #car_obj.move_forward()
    #car_obj.turn_right()
    sleep(3.2)
    car_obj.stop()
