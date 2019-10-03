import time
import sys
sys.path.append('..')

import config
import indicate

################ MAIN
led = indicate.StatusLed(config.STATUS_LED_PIN)

led.indicate((1, 0, 0))
time.sleep(3)
led.indicate((0, 1, 0))
time.sleep(3)
led.indicate((0, 0, 1))
time.sleep(3)

led.test()
