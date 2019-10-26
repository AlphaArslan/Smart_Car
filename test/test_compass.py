# compass component is actually a QMC5883L (address 0x0d)
# it not a HMC5883L as the seller claims
# tested and working

# do calibration first from lib/py-qcm.../calibration

import sys
sys.path.append('..')
import compass_module
import time

compass_obj = compass_module.Compass(0x1e)


while True:
    num = compass_obj.get_heading_angle()
    print(num)
    time.sleep(1)
