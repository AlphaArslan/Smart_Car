# compass component is actually a QMC5883L (address 0x0d)
# it not a HMC5883L as the seller claims


import sys
sys.path.append('..')
import compass_module
import time

compass_obj = compass_module.Compass(0x1e)

while True:
    print(compass_obj.get_heading_angle())
    time.sleep(1)

# address 0x0d
# zero raw data
