import config
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

class Motor():
    def __init__(self, pins_tuble):
        self.dir_pin, self.pwm_pin = pins_tuble
        GPIO.setup(self.dir_pin, GPIO.OUT)
        GPIO.setup(self.pwm_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pwm_pin, config.MTR_PWM_FREQ)
        self.pwm.start(0)

    def forward(self, speed = config.MTR_FRWRD_SPD ):
        GPIO.output(self.dir_pin, config.MTR_DIR_FORWARD)
        self.pwm.ChangeDutyCycle(speed)

    def backward(self, speed = config.MTR_BKWRD_SPD ):
        GPIO.output(self.dir_pin, config.MTR_DIR_BACKWARD)
        self.pwm.ChangeDutyCycle(speed)

    def stop(self):
        self.pwm.ChangeDutyCycle(0)



class Car():
    def __init__(self, right, left):
        self.right_motor = motor.Motor(right)
        self.left_motor = motor.Motor(left)

    def move_forward(self):
        self.right_motor.forward()
        self.left_motor.forward()

    def move_backward(self):
        self.right_motor.backward()
        self.left_motor.backward()

    def turn_forward_right(self):
        self.right_motor.stop()
        self.left_motor.forward()

    def turn_forward_left(self):
        self.right_motor.forward()
        self.left_motor.stop()

    def turn_backward_right(self):
        self.right_motor.stop()
        self.left_motor.backward()

    def turn_backward_left(self):
        self.right_motor.backward()
        self.left_motor.stop()

    def stop(self):
        self.right_motor.stop()
        self.left_motor.stop()

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
            print("Forward Right")
        self.turn_forward_right()
        sleep(5)

        if prnt:
            print("Forward Left")
        self.turn_forward_left()
        sleep(5)

        if prnt:
            print("Backward Right")
        self.turn_backward_right()
        sleep(5)

        if prnt:
            print("Backward Left")
        self.turn_backward_left()
        sleep(5)

        self.stop()
