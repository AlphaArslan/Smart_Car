import RPi.GPIO as GPIO
import time

class StatusLed():
    def __init__(self, [R_pin, G_pin, B_pin]):
        self.rpin = R_pin
        self.gpin = G_pin
        self.bpin = B_pin
        GPIO.setup(R_pin, GPIO.OUT)
        GPIO.setup(G_pin, GPIO.OUT)
        GPIO.setup(B_pin, GPIO.OUT)

    def indicate(self, (r, g, b)):
        GPIO.output(self.rpin, r)
        GPIO.output(self.gpin, g)
        GPIO.output(self.bpin, b)

    def test(self):
        for i in [0, 1]:
            for j in [0, 1]:
                for h in [0, 1]:
                    self.indicate(self, (i, j, h))
                    time.sleep(2)
