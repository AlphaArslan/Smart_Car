import time
import sys
sys.path.append('..')

import config
import indicate

################ MAIN
led = indicate.StatusLed(config.STATUS_LED_PIN)

led.test()
