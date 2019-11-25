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

    def move_forward(self, dbg = config.DEBUG_MODE):
        if dbg :
            print("[CAR] moving forward")
        self.right_motor.forward()
        self.left_motor.forward(diff= config.MTR_RL_DIFF)

    def move_backward(self, dbg = config.DEBUG_MODE):
        if dbg :
            print("[CAR] moving backward")
        self.right_motor.backward()
        self.left_motor.backward(diff= config.MTR_RL_DIFF)

    def turn_right(self, dbg = config.DEBUG_MODE):
        if dbg :
            print("[CAR] turning forward right")
        self.right_motor.backward()
        self.left_motor.forward(diff= config.MTR_RL_DIFF)

    def turn_left(self, dbg = config.DEBUG_MODE):
        if dbg :
            print("[CAR] turning forward left")
        self.right_motor.forward()
        self.left_motor.backward(diff= config.MTR_RL_DIFF)

    def stop(self, dbg = config.DEBUG_MODE):
        if dbg :
            print("[CAR] stopping ")
        self.right_motor.stop()
        self.left_motor.stop()

    def line_follow(self, dir):
        if dbg :
            print("[CAR] following line")
        self.right_motor.forward(speed= config.MTR_FRWRD_SPD//2 - dir*5)
        self.left_motor.forward(speed= config.MTR_FRWRD_SPD//2 + dir*5 ,diff= config.MTR_RL_DIFF)

    def test_move(self, prnt= False):
        if prnt:
            print("Forward")
        self.move_forward()
        sleep(5)

        if prnt:
            print("Backward")
        self.move_backward()
        sleep(5)

        if prnt:
            print("Right")
        self.turn_right()
        sleep(5)

        if prnt:
            print("Left")
        self.turn_left()
        sleep(5)


        self.stop()

################################################
if __name__ == '__main__':

    car_obj = Car(config.MTR_R_PIN, config.MTR_L_PIN)

    car_obj.move_forward()
