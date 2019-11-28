# microsoft live hd-3000 camera
import sys
sys.path.append('..')

import cv2
import config
import zmq

jpeg_quality = 70
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), jpeg_quality]

# socket
context = zmq.Context()
soc_cam0 = context.socket(zmq.REP)
soc_cam0.bind("tcp://*:"+ config.CAM_PORT)

def cam_gen0():
    cam0 = cv2.VideoCapture(0)
    while True:
        print("[CAM] waiting")
        # wait for request
        print(soc_cam0.recv())
        # send image
        ret, img = cam0.read()
        if ret:
            print("[CAM] returned an image")
            im_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            _ , im_enc = cv2.imencode('.jpg', img, encode_param)
            soc_cam0.send(im_enc.tobytes())
        else:
            print("[CAM] no image")
            soc_cam0.send(b'None')

############################################
if __name__ == '__main__':
    cam_gen0()
