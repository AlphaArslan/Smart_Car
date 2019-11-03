########################### IMPORT
import zmq
from time import sleep

import config
# import indicate
# import auto

########################### obj
# status_led_obj = indicate.StatusLed(config.STATUS_LED_PIN)
# pilot_obj = auto.Pilot()

############ setup
# media socket
context = zmq.Context()
media_socket = context.socket(zmq.REQ)
media_socket.connect("tcp://localhost:"+config.MEDIA_PORT)

# control socket
control_socket = context.socket(zmq.REP)
control_socket.bind("tcp://*:"+config.CTRL_PORT)

########################### functions
def wait_for_tasks():
    if config.DEBUG_MODE:
        print("[MAIN] waiting for tasks")

    # listen for tasks from web
    task = control_socket.recv()
    control_socket.send(b'OK')

    if task == config.TASK_CMD_FRWRD:
        print("forward")

    if config.DEBUG_MODE:
        print("[MAIN] Got task: {}".format(task))
    return task

########################### MAIN
if __name__ == '__main__':

    ############ loop
    while True:
        # status_led_obj.indicate(config.FREE_STATUS_COLOR)
        task = wait_for_tasks()
        # status_led_obj.indicate(config.BUSY_STATUS_COLOR)
        # pilot_obj.go_to_locaion(loc)
