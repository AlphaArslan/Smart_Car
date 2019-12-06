print("0")

########################### IMPORT
import zmq
import multiprocessing
import line_follower_cv
import config
import time

print("1")

class CarMapper():
    def __init__(self):
        pass
    def move_forward(self):
        moto_socket.send(b"f")
        print(moto_socket.recv())
    def move_backward(self):
        moto_socket.send(b"b")
        print(moto_socket.recv())
    def turn_right(self):
        moto_socket.send(b"r")
        print(moto_socket.recv())
    def turn_left(self):
        moto_socket.send(b"l")
        print(moto_socket.recv())
    def stop(self):
        moto_socket.send(b"s")
        print(moto_socket.recv())
    def line_follow(self, dir):
        moto_socket.send(b"l")
        print(moto_socket.recv())
        dir = str(dir) #convert from float to string
        dir = dir.encode() #convert from string to bytes
        moto_socket.send(dir)
        print(moto_socket.recv())

car_obj = CarMapper()

################# objects
context = zmq.Context()
moto_socket = context.socket(zmq.REQ)
moto_socket.connect("tcp://localhost:"+ config.MOTO_PORT)

# shared var
sh_f = multiprocessing.Value("i",0)

# process
def p():
    print("[LNAT] parallel")
    # socket
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:"+ config.AUTO_PORT)
    # listen on socket
    while True:
        r = socket.recv()
        socket.send(b'OK')
        if r == b'play':
            sh_f.value = 1
        elif r == b'stop':
            sh_f.value = 0

# control process
prcs = multiprocessing.Process(target= p)
prcs.start()

def follow_line():
    print("[LNAT] started line follower")
    f = 0
    ft = 0
    while True:
        if sh_f.value == 1:
            print("[LNAT] line follower ON")
            dir = line_follower_cv.get_direction()
            if dir == None:
                print("Can't find the line")
                if f == 0:
                    car_obj.move_backward()
                    time.sleep(0.4)
                    car_obj.stop()
                    time.sleep(0.5)

                    f =1
                elif f == 1:
                    car_obj.turn_right()
                    #time.sleep(1)
                    time.sleep(0.6)
                    car_obj.stop()
                    time.sleep(0.5)

                    f = 2
                elif f == 2:
                    car_obj.turn_left()
                    #time.sleep(2.2)
                    time.sleep(1.4)
                    car_obj.stop()
                    time.sleep(0.5)

                    f = 3
                elif f == 3 :
                    f = 0
                    ft = ft + 1

                    time.sleep(3)
                continue
            f = 0
            ft = 0
            x = 8
            if dir > x:
                dir = x
            elif dir < -x:
                dir = -x
            print(dir)
            car_obj.line_follow(dir)
            #time.sleep(0.5 + 0.36*abs(dir))
            time.sleep(0.15 + 0.1*abs(dir))
            car_obj.move_forward(sped= 18 + (x-abs(dir))*1.3)
            #time.sleep(0.18 + (x-abs(dir))*0.1)
            time.sleep(0.15 + (x-abs(dir))*0.08)
        else:
            print("[LNAT] line follower OFF")
            time.sleep(2)

###################################
if __name__ == '__main__':
    car_obj.stop()
    #exit()
    #sh_f.value = 1
    follow_line()
