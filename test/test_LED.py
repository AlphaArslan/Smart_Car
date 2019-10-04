import time
import sys
sys.path.append('..')

import config
import indicate

################ MAIN
led = indicate.StatusLed(config.STATUS_LED_PIN[0], config.STATUS_LED_PIN[1], config.STATUS_LED_PIN[2])

print("MAGENTA")
led.indicate(1, 0, 1)
time.sleep(3)

print("YELLOW")
led.indicate(1, 1, 0)
time.sleep(3)

print("CYAN")
led.indicate(0, 1, 1)
time.sleep(3)

print("WHITE")
led.indicate(1, 1, 1)
time.sleep(3)


led.indicate(0, 0, 0)

led.test()
led.indicate(0, 0, 0)
