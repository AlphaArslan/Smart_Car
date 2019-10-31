import time
import sys
sys.path.append('..')

import config
import GPS_module

gps_obj = GPS_module.GPS()

while True:
    print(gps_obj.get_location())
    time.sleep(5)
