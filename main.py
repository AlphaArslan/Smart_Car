########################### IMPORT
import zmq
from time import sleep

import config
import indicate
import motor

########################### obj
status_led_obj = indicate.StatusLed(config.STATUS_LED_PIN)
car_obj = motor.Car(config.MTR_R_PIN, config.MTR_L_PIN)

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
    manual_f = False
    # print("main")
    ############ loop
    while True:
        # run line follower
        if not manual_f:
            auto_socket.send(b'play')
            print(auto_socket.recv())
        status_led_obj.indicate(config.FREE_STATUS_COLOR)
        # wait for manual
        task, loc = wait_for_tasks()
        #sleep(5)
        # stop line follower
        auto_socket.send(b'stop')
        print(auto_socket.recv())
        #exit()

        status_led_obj.indicate(config.BUSY_STATUS_COLOR)
        manual_f = True
        if task == config.TASK_CMD_FRWRD:
            car_obj.move_forward()
        elif task == config.TASK_CMD_BKWRD:
            car_obj.move_backward()
        elif task == config.TASK_CMD_TRN_R:
            car_obj.turn_right()
        elif task == config.TASK_CMD_TRN_L:
            car_obj.turn_left()
        elif task == config.TASK_CMD_STOP:
            car_obj.stop()
            manual_f = False
