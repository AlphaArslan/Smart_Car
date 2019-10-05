########################### IMPORT
import zmq
import config

########################### FUNC
def wait_for_task():
    pass

########################### MAIN
if __name__ == '__main__':

    ########### SETUP
    # socket to send tasks
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:"+config.TASK_PORT)

    while True:
        wait_for_task()
        socket.send(b"TASK")
        message = socket.recv()
        print(message)
