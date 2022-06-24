#!/usr/bin/env python
from sense_hat import SenseHat
import time, datetime
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from time import sleep

sense = SenseHat()
hat = SenseHat()

hour_color = (0, 255, 0)
minute_color = (0, 0, 255)
second_color = (255, 0, 0)
off = (0, 0, 0)

hat.clear()

def display_binary(value, row, color):
    binary_str = '{0:8b}'.format(value)
    for x in range(0, 8):
        if binary_str[x] == "1":
            hat.set_pixel(x, row, color)
        else:
            hat.set_pixel(x, row, off)


def pushed_up(event):
    t = datetime.datetime.now()
    display_binary(t.hour, 3, hour_color)
    display_binary(t.minute, 4, minute_color)
    display_binary(t.second, 5, second_color)
    for event in sense.stick.get_events():
        print(event.direction, event.action)
        if event.direction == 'down':
            pushed_down(event)
            
        
def pushed_down(event):
    print("Clear")
    hat.clear()
    event.direction == 'down' 


while True:
    for event in sense.stick.get_events():
        print(event.direction, event.action)
            
        while event.direction == 'up':
            pushed_up(event)
            break
            
                
                
        
         
            
        #else:
            #hat.clear()


