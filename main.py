########################### IMPORT
import zmq
from time import sleep
import RPi.GPIO as GPIO

import config
import motor
import indicate


########################### FUNC
def wait_for_tasks():
    #  Wait for task
    message = socket.recv()
    # print("Received request: %s" % message)
    #  Send reply back to client
    socket.send(b"OK")

########################### MAIN
if __name__ == '__main__':

    ########### SETUP
    # to get tasks from other modules
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind(config.TASK_PORT)

    # motors
    car = motor.CarFourMotors()

    # status led
    status_led = indicate.StatusLed(config.STATUS_LED_PIN)

    while True:
        status_led.indicate(config.FREE_STATUS_COLOR)
        task = wait_for_tasks()
        status_led.indicate(config.BUSY_STATUS_COLOR)
        # execute task
