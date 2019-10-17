import sys
sys.path.append('..')

import ultrasonic
import config
import time

us_obj = ultrasonic.UltraSonic(config.US_TRIG_PIN, config.US_ECHO_PIN)

while True:
    print(us_obj.get_distance())
    time.sleep(1)
