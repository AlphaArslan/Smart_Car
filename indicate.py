import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

class StatusLed():
    def __init__(self, pins_tuble):
        self.rpin, self.gpin, self.bpin = pins_tuble
        GPIO.setup(self.rpin, GPIO.OUT)
        GPIO.setup(self.gpin, GPIO.OUT)
        GPIO.setup(self.bpin, GPIO.OUT)

    def indicate(self, color_tuple):
        """
        light RGB color
        """
        r, g, b = color_tuple
        GPIO.output(self.rpin, r)
        GPIO.output(self.gpin, g)
        GPIO.output(self.bpin, b)

    def test(self):
        for i in [0, 1]:
            for j in [0, 1]:
                for h in [0, 1]:
                    self.indicate((i, j, h))
                    time.sleep(2)
        self.off()

    def off(self):
        self.indicate((0,0,0))
# try to pass tuples to functions
