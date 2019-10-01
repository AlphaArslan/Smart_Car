from config import *

class Motor():
    def __init__(self):
        pass

    def forward(self, speed = MTR_FRWRD_SPD ):
        pass

    def backward(self, speed = MTR_BKWRD_SPD ):
        pass

    def stop(self):
        pass

class CarFourMotors():
    def __init__(self):
        self.mtr_rf = motor.Motor()              # right front motor
        self.mtr_lf = motor.Motor()              # left front motor
        self.mtr_rb = motor.Motor()              # right back motor
        self.mtr_lb = motor.Motor()              # left back motor

    def move_forward(self):
        self.mtr_rf.forward()
        self.mtr_lf.forward()
        self.mtr_rb.forward()
        self.mtr_lb.forward()

    def move_backward(self):
        self.mtr_rf.backward()
        self.mtr_lf.backward()
        self.mtr_rb.backward()
        self.mtr_lb.backward()

    def turn_forward_right(self):
        self.mtr_rf.stop()
        self.mtr_lf.forward()
        self.mtr_rb.stop()
        self.mtr_lb.forward()

    def turn_forward_left(self):
        self.mtr_rf.forward()
        self.mtr_lf.stop()
        self.mtr_rb.forward()
        self.mtr_lb.stop()

    def turn_backward_right(self):
        self.mtr_rf.stop()
        self.mtr_lf.backward()
        self.mtr_rb.stop()
        self.mtr_lb.backward()

    def turn_backward_left(self):
        self.mtr_rf.backward()
        self.mtr_lf.stop()
        self.mtr_rb.backward()
        self.mtr_lb.stop()

    def stop(self):
        self.mtr_rf.stop()
        self.mtr_lf.stop()
        self.mtr_rb.stop()
        self.mtr_lb.stop()

    def test_move(self):
        self.move_forward()
        sleep(5)
        self.move_backward()
        sleep(5)
        self.turn_forward_right()
        sleep(5)
        self.turn_forward_left()
        sleep(5)
        self.turn_backward_right()
        sleep(5)
        self.turn_backward_left()
        sleep(5)
