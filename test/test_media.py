import zmq
import time
import sys
sys.path.append('..')

import config

# socket
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:"+config.MEDIA_PORT)

# send play command
socket.send(config.MEDIA_CMD_PLAY)
print(socket.recv())
socket.send("vid.mp4".encode('utf-8'))
print(socket.recv())
# input("press any key to stop media")
time.sleep(20)
socket.send(config.MEDIA_CMD_STOP)
print(socket.recv())
# input("press any key to terminate")
socket.send(config.MEDIA_CMD_TERMINATE)
