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
    def __init__(self, dbg = config.DEBUG_MODE ):
        self.dbg = dbg
        self.target_loc = None
        self.current_loc = None
        self.distance = None
        self.target_direction = None

    def forward(self):
        if self.dbg:
            print("[AUTO] moving forward")
        car_obj.move_forward()

    def backward(self):
        if self.dbg:
            print("[AUTO] moving backward")
        car_obj.move_backward()

    def right(self):
        if self.dbg:
            print("[AUTO] turning right")
        car_obj.turn_right()

    def left(self):
        if self.dbg:
            print("[AUTO] turning left")
        car_obj.turn_left()

    def stop(self):
        if self.dbg:
            print("[AUTO] stopped")
        car_obj.stop()

    def go_to_locaion(self, final_location):
        """
        pass location you want (lat, long)
        wait until I reach it
        """
        if self.dbg:
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
                if self.dbg:
                    print("[AUTO] BLOCKED!!")
                car_obj.turn_forward_right()
                time.sleep(config.TURN_DELAY/4)

            car_obj.move_forward()
            time.sleep(config.STEP_DELAY)
            car_obj.stop()

            # update current_loc and distance
            self.current_loc = gps_obj.get_location()
            self.distance = geopy.distance.geodesic(self.current_loc, self.target_loc).m


    def get_target_direction(self):
        if self.dbg:
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

        if self.dbg:
            print("[AUTO] target direction: {}".format(compass_bearing))

        return compass_bearing


    def set_heading_direction(self):
        """
        sets the pointing direction of the car
        """
        if self.dbg:
            print("[AUTO] setting robot direction")

        angle_differnce = compass_obj.get_heading_angle() - self.target_direction
        while ( abs(angle_differnce) > config.ANGLE_TOLERANCE ):
            # turn right
            car_obj.turn_backward_right()
            # delay for a little bit
            time.sleep(config.TURN_DELAY/6)
            #update angle angle_differnce
            self.target_direction = self.get_target_direction()
            angle_differnce = compass_obj.get_heading_angle() - self.target_direction


##############################################
if __name__ == '__main__':
    p = Pilot()
    p.go_to_locaion((0,0))
