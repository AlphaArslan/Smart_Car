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
auto_socket = context.socket(zmq.REQ)
auto_socket.connect("tcp://localhost:"+ config.AUTO_PORT)

# cam socket
soc_cam0 = context.socket(zmq.REQ)
soc_cam0.connect("tcp://localhost:"+ config.CAM_PORT)

moto_socket = context.socket(zmq.REQ)
moto_socket.connect("tcp://localhost:"+ config.MOTO_PORT)


class CarMapper():
    def __init__(self):
        pass
    def move_forward(self):
        moto_socket.send(b"f")
        print(moto_socket.recv())
    def move_backward(self):
        moto_socket.send(b"b")
        print(moto_socket.recv())
    def turn_right(self):
        moto_socket.send(b"r")
        print(moto_socket.recv())
    def turn_left(self):
        moto_socket.send(b"l")
        print(moto_socket.recv())
    def stop(self):
        moto_socket.send(b"s")
        print(moto_socket.recv())
    def line_follow(self, dir):
        moto_socket.send(b"l")
        print(moto_socket.recv())
        dir = str(dir) #convert from float to string
        dir = dir.encode() #convert from string to bytes
        moto_socket.send(dir)
        print(moto_socket.recv())

car_obj = CarMapper()




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
    auto_socket.send(b'stop')
    print(auto_socket.recv())
    if control == "forward":
        car_obj.move_forward()
        return "ok"

    if control == "backward":
        car_obj.move_backward()
        return "ok"

    if control == "right":
        car_obj.turn_right()
        return "ok"

    if control == "left":
        car_obj.turn_left()
        return "ok"

    if control == "stop":
        car_obj.stop()
        auto_socket.send(b'play')
        print(auto_socket.recv())
        return "ok"


########################## main
if __name__ == '__main__':
    app.run(host= '0.0.0.0')
    print("s")
