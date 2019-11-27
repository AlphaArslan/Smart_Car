########################## import
import numpy as np
import cv2
import camera

########################## controls
slash = "/"
IMAGE_SIZE = (800, 600)
line_cam = camera.Camera(0, dbg=False)

########################## func
def get_direction():
    global line_cntr
    """
    returns: [-10:10] for [left : right]
    """
    # get image
    img = line_cam.get_image_rgb()
    # img = cv2.imread("test"+slash+"camera.jpg")
    img = cv2.resize(img, (800, 600), interpolation = cv2.INTER_AREA)
    #cv2.imshow("resize", img)
    #cv2.waitKey(0)

    # ROI
    roi = img[400:450,0:800]
    #cv2.imshow("cropped", roi)
    #cv2.waitKey(0)
    
    # image inhancement
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (9,9), 0)
    #_, thresh = cv2.threshold(blur, 90,255, cv2.THRESH_BINARY_INV)
    _, thresh = cv2.threshold(blur, 180,255, cv2.THRESH_BINARY)

    #cv2.imshow("enhanced", thresh)
    #cv2.waitKey(0)
    # find line
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #print(len(contours))
    if len(contours) == 0:
        print("[LINE] couldn't find the line")
        return None
    elif contours == 1:
        line_cntr = contours[0]
    else:
        # find biggest contour
        cntr_area = 0
        for cntr in contours:
            ca = cv2.contourArea(cntr)
            # print(ca)
            if ca > cntr_area:
                cntr_area = ca
                line_cntr = cntr
                
    # print(cntr_area)               
    M = cv2.moments(line_cntr)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    line_center = (cX, cY)
    # print(line_center)

    cv2.drawContours(roi, contours, -1, (0,255,0), 3)
    cv2.circle(roi, (cX, cY), 7, (0, 255, 255), -1)
    #cv2.imshow("line", roi)
    #cv2.waitKey(0)

    # take decision
    return ((cX - 400)/40)

########################## main
if __name__ == '__main__':
    
    print(get_direction())
    cv2.destroyAllWindows()
