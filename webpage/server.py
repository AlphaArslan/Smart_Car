########################## import
from flask import Flask, render_template, redirect, request, Response
import glob
import os
import cv2
import zmq

import sys
sys.path.append('..')
import config

########################## setup
app = Flask(__name__)

# control socket
context = zmq.Context()
control_socket = context.socket(zmq.REQ)
control_socket.connect("tcp://localhost:"+config.CTRL_PORT)

# cam socket
soc_cam0 = context.socket(zmq.REQ)
soc_cam0.connect("tcp://localhost:"+ config.CAM_PORT)

########################## routes
def img_gen():
    while True:
        soc_cam0.send(b'get')
        answer = soc_cam0.recv()
        if answer == b'None':
            print("no image")
            continue
        frame_bytes = answer
        yield (b'--frame\r\n'
               b'Content-Type: image/jpg\r\n\r\n' + frame_bytes + b'\r\n\r\n')


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/stream')
def stream():
    return render_template("stream.html")

@app.route("/video_feed")
def video_feed():
    return Response(img_gen(),
        mimetype="multipart/x-mixed-replace; boundary=frame")

@app.route("/order")
def order():
    return render_template("order.html")

@app.route("/controls/<string:control>")
def controls(control):
    print(control)
    if control == "forward":
        print("sending command")
        control_socket.send(config.TASK_CMD_FRWRD)
        print(control_socket.recv())
        return "ok"

    if control == "backward":
        print("sending command")
        control_socket.send(config.TASK_CMD_BKWRD)
        print(control_socket.recv())
        return "ok"

    if control == "right":
        print("sending command")
        control_socket.send(config.TASK_CMD_TRN_R)
        print(control_socket.recv())
        return "ok"

    if control == "left":
        print("sending command")
        control_socket.send(config.TASK_CMD_TRN_L)
        print(control_socket.recv())
        return "ok"

    if control == "stop":
        print("sending command")
        control_socket.send(config.TASK_CMD_STOP)
        print(control_socket.recv())
        return "ok"


########################## main
if __name__ == '__main__':
    app.run(host= '0.0.0.0')
    print("s")
