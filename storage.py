########################### IMPORT
import zmq
from config import *

########################### FUNC
def wait_for_task():
    pass

########################### MAIN
if __name__ == '__main__':

    ########### SETUP
    # socket to send tasks
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect(TASK_PORT)

    while True:
        wait_for_task()
        socket.send(b"TASK")
        message = socket.recv()
        print(message)
