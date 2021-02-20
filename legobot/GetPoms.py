#!/usr/bin/python
import os, sys
import ctypes
KIPR=ctypes.CDLL("/usr/lib/libkipr.so")

r_motor = 0
l_motor = 1

top_pos = 0
capture_pos = 400
bottom_pos = 900

toph_right = 0
toph_left = 1
    
black = 2000
    
# def time_follow(time):


def stop(sleep_time=0):
    move(0, 0)
    KIPR.msleep(sleep_time)

def move(l_power, r_power):
    KIPR.motor(l_motor, l_power)
    KIPR.motor(r_motor, r_power)
    KIPR.msleep(5)

def go_to_black(l_power=45, r_power=50):
    while(KIPR.analog(toph_left) < black or KIPR.analog(toph_right) < black):
        move(l_power, r_power)
    stop()
def line_follow(time):
    end_time = KIPR.seconds()+time
    while(KIPR.seconds() < end_time):
        if(KIPR.analog(toph_right) > black):
            move(37, 50)
        else:
            move(50, 37)
        print(KIPR.seconds(), end_time)
        

def main():
    KIPR.enable_servos()
    KIPR.set_servo_position(0, top_pos)
    
    go_to_black()
    
    move(50, 50)
    KIPR.msleep(500)
    stop(100)
    
    move(0, 50)
    KIPR.msleep(3000)
        
    line_follow(6200)
    stop(500)
        
    KIPR.set_servo_position(0, capture_pos)
    move(-50, -50)
    KIPR.msleep(2000)
    stop(100)
        
    KIPR.set_servo_position(0, bottom_pos)
    move(50, 50)
    KIPR.msleep(3000)
if __name__== "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
    main()
