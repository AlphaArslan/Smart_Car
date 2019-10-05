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
socket.send("vid2.mp4".encode('utf-8'))
print(socket.recv())
input("press any key")
socket.send(config.MEDIA_CMD_STOP)
print(socket.recv())
input("press any key")
socket.send(config.MEDIA_CMD_TERMINATE)
