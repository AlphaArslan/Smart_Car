########################## import
from flask import Flask, render_template, redirect, request, Response
import glob
import os
import camera
import cv2
import zmq

import sys
sys.path.append('..')
import config

########################## setup
app = Flask(__name__)
cam = camera.Camera(0)

# control socket
context2 = zmq.Context()
control_socket = context2.socket(zmq.REQ)
control_socket.connect("tcp://localhost:"+config.CTRL_PORT)

########################## routes
def img_gen():
    while True:
        img = cam.get_image_rgb()
        frame_bytes = cv2.imencode('.jpg',img)[1].tobytes()
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
    # if control == "forward":
    #     control_socket.send(config.TASK_CMD_FRWRD)
    #     print(control_socket.recv())
    return "ok"


########################## main
if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0')
