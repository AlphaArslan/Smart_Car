########################### IMPORT
import zmq
from time import sleep

import config
import indicate
import auto

########################### obj
status_led_obj = indicate.StatusLed(config.STATUS_LED_PIN)
pilot_obj = auto.Pilot()

########################### functions
def wait_for_tasks():
    # listen for tasks from web
    location = (0,0)
    return location

########################### MAIN
if __name__ == '__main__':
    while True:
        status_led_obj.indicate(config.FREE_STATUS_COLOR)
        loc = wait_for_tasks()
        status_led_obj.indicate(config.BUSY_STATUS_COLOR)
        pilot_obj.go_to_locaion(loc)
