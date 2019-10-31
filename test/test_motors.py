import time
import sys
sys.path.append('..')

import motor

# dir_pin = 11
# pwm_pin = 12
#
# ## test single motor
# m = motor.Motor((dir_pin, pwm_pin))
#
# print("forward")
# m.forward()
# time.sleep(5)
# m.stop()
#
# print("backward")
# m.backward()
# time.sleep(5)
# m.stop()

car_obj = motor.Car((35, 37), (36, 38))

car_obj.move_forward()
time.sleep(5)
car_obj.move_backward()
time.sleep(5)
