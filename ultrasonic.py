# tested and working 

import RPi.GPIO as GPIO
import time
import config

GPIO.setmode(config.GPIO_MODE)

class UltraSonic():
    def __init__(self, trig_pin, echo_pin):
        self.trig = trig_pin
        self.echo = echo_pin
        # set GPIO input and output channels
        GPIO.setup(trig_pin, GPIO.OUT)
        GPIO.setup(echo_pin, GPIO.IN)

    def get_distance(self):
        """
        returns distance in cm
        """
    	# set Trigger to HIGH
    	GPIO.output(self.trig, True)
    	# set Trigger after 0.01ms to LOW
    	time.sleep(0.00001)
    	GPIO.output(self.trig, False)

    	startTime = time.time()
    	stopTime = time.time()

    	# save start time
    	while 0 == GPIO.input(self.echo):
    		startTime = time.time()

    	# save time of arrival
    	while 1 == GPIO.input(self.echo):
    		stopTime = time.time()

    	# time difference between start and arrival
    	TimeElapsed = stopTime - startTime
    	# multiply with the sonic speed (34300 cm/s)
    	# and divide by 2, because there and back
    	distance = (TimeElapsed * 34300) / 2
        return distance

    def is_blocked(self, threshold):
        return self.get_distance() < threshold
