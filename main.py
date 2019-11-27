########################### IMPORT
import zmq
from time import sleep

import config
import indicate
import auto

########################### obj
status_led_obj = indicate.StatusLed(config.STATUS_LED_PIN)
pilot_obj = auto.Pilot()
pilot_obj.line_follow()

############ setup
# media socket
context = zmq.Context()
media_socket = context.socket(zmq.REQ)
media_socket.connect("tcp://localhost:"+config.MEDIA_PORT)

# control socket
control_socket = context.socket(zmq.REP)
control_socket.bind("tcp://*:"+config.CTRL_PORT)

# auto socket
auto_socket = context.socket(zmq.REQ)
auto_socket.connect("tcp://localhost:"+ config.AUTO_PORT)

########################### functions
def wait_for_tasks():
    if config.DEBUG_MODE:
        print("[MAIN] waiting for tasks")
    # listen for tasks from web
    loc = (0, 0)
    task = control_socket.recv()
    control_socket.send(b'OK')
    if config.DEBUG_MODE:
        print("[MAIN] Got task: {} {}".format(task, loc))
    return task , loc

########################### MAIN
if __name__ == '__main__':
    # print("main")
    ############ loop
    while True:
        # run line follower
        auto_control.send(b'play')
    	print(auto_control.recv())
        status_led_obj.indicate(config.FREE_STATUS_COLOR)
        # wait for manual
        task, loc = wait_for_tasks()

        # stop line follower
        auto_control.send(b'stop')
    	print(auto_control.recv())

        status_led_obj.indicate(config.BUSY_STATUS_COLOR)
        if task == config.TASK_CMD_FRWRD:
            pilot_obj.forward()
        elif task == config.TASK_CMD_BKWRD:
            pilot_obj.backward()
        elif task == config.TASK_CMD_TRN_R:
            pilot_obj.right()
        elif task == config.TASK_CMD_TRN_L:
            pilot_obj.left()
        elif task == config.TASK_CMD_STOP:
            pilot_obj.stop()
