"""
Drives the car to desires direction
communicates with compass and gps modules
"""
################# import
import compass_module
import gps_module
import config
import geopy.distance
import motor
import time
import math
import ultrasonic

################# objects
compass_obj = compass_module.Compass(0x1e)
gps_obj = gps_module.GPS()
car_obj = motor.Car(config.MTR_R_PIN, config.MTR_L_PIN)
us_obj = ultrasonic.UltraSonic(config.US_TRIG_PIN, config.US_ECHO_PIN)

################# pilot class
class Pilot():
    def __init__(self):
        pass

    def get_target_direction(self, dbg = config.DEBUG_MODE):
        if dbg:
            print("[AUTO] getting target direction")
        lat1 = math.radians(self.current_loc[0])
        lat2 = math.radians(self.target_loc[0])

        diffLong = math.radians(self.target_loc[1] - self.current_loc[1])

        x = math.sin(diffLong) * math.cos(lat2)
        y = math.cos(lat1) * math.sin(lat2) - (math.sin(lat1)
                * math.cos(lat2) * math.cos(diffLong))

        initial_bearing = math.atan2(x, y)

        initial_bearing = math.degrees(initial_bearing)
        compass_bearing = (initial_bearing + 360) % 360

        if dbg:
            print("[AUTO] target direction: {}".format(compass_bearing))

        return compass_bearing


    def set_heading_direction(self, dbg = config.DEBUG_MODE):
        """
        sets the pointing direction of the car
        """
        if dbg:
            print("[AUTO] setting robot direction")

        angle_differnce = compass_obj.get_heading_angle() - self.target_direction
        while ( abs(angle_differnce) > config.ANGLE_TOLERANCE ):
            # turn right
            car_obj.turn_backward_right()
            # delay for a little bit
            time.sleep(config.TURN_DELAY/6)
            #update angle angle_differnce
            self.target_direction = self.get_target_direction(dbg=False)
            angle_differnce = compass_obj.get_heading_angle() - self.target_direction


    # def step_forward():
    #     for i in range(0,8):
    #         # check if blocked
    #         if ultrasonic.is_blocked(config.US_BLOCKED_THRESH):
    #             car_obj.turn_backward_left()
    #             time.sleep(config.TURN_DELAY)
    #             car_obj.move_forward()
    #             time.sleep(config.STEP_DELAY/10)
    #             car_obj.stop()
    #
    #
    #         time.sleep(config.STEP_DELAY/10)

    def go_to_locaion(self, final_location, dbg = config.DEBUG_MODE):
        """
        pass location you want
        wait until I reach it
        """
        if dbg:
            print("[AUTO] going to location {}".format(final_location))

        self.target_loc = final_location
        self.current_loc = gps_obj.get_location()
        self.distance = geopy.distance.geodesic(self.current_loc, self.target_loc).m
        self.target_direction = self.get_target_direction()

        while (self.distance > config.DIST_TOLERANCE ):
            # set direction
            self.set_heading_direction()

            # avoid obstacles if exist
            while us_obj.is_blocked(config.US_BLOCKED_THRESH):
                if dbg:
                    print("[AUTO] BLOCKED!!")
                car_obj.turn_forward_right()
                time.sleep(config.TURN_DELAY/4)

            car_obj.move_forward()
            time.sleep(config.STEP_DELAY)
            car_obj.stop()

            # update current_loc and distance
            self.current_loc = gps_obj.get_location()
            self.distance = geopy.distance.geodesic(self.current_loc, self.target_loc).m
