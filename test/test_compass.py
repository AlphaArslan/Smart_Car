sys.path.append('..')
import compass_module
import time

compass_obj = compass_module.Compass(0x1e)

while True:
    print(compass_obj.get_heading_angle())
    time.sleep(1)
