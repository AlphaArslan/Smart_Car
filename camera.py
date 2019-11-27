# microsoft live hd-3000 camera
import sys
sys.path.append('..')

import cv2
import config

class Camera():
    def __init__(self, id, dbg=config.DEBUG_MODE):
        """
        microsoft live hd-3000 camera
        """
        self.cam = cv2.VideoCapture(id)
        self.cam.set(cv2.CAP_PROP_BUFFERSIZE, 1)
        self.dbg = dbg

    def get_image_rgb(self):
        ret, img = self.cam.read()
        if ret:
            if self.dbg:
                print("[CAM] returned an image")
            im_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            return im_rgb
        if self.dbg:
            print("[CAM] no image")
        return None

    def __del__(self):
        self.cam.release()


###################### for testing
if __name__ == '__main__':
    cam_obj = Camera(0)
    while True:
        img = cam_obj.get_image_rgb()
        cv2.imshow('frame',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.imwrite("test/camera.jpg", img)
    cv2.destroyAllWindows()
