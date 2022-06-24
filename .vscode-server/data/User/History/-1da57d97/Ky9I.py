#!/usr/bin/env python
from sense_hat import SenseHat
import time, datetime

hat = SenseHat()

blue = (0, 0, 255)
yellow = (255, 255, 0)

class AdventureDone(Exception): pass
year_color = (0, 255, 0)
month_color = (0, 0, 255)
day_color = (255, 0, 0)
green = (0, 255, 0)
dark_yellow = (127, 127, 0)
red = (255, 0, 0)

off = (0, 0, 0)
#hat.show_message("Program starting", text_colour=yellow, back_colour=blue, scroll_speed=0.05)

def display_binary(value, row, color):
    binary_str = '{0:8b}'.format(value)
    for x in range(0, 8):
        if binary_str[x] == "1":
            hat.set_pixel(x, row, color)
        else:
            hat.set_pixel(x, row, off)

def down(event):
    print("Clear")
    hat.clear()
    raise AdventureDone

def main_watch():
    try:
        while True:
            acceleration = hat.get_accelerometer_raw()
            x = acceleration['x']
            y = acceleration['y']
            z = acceleration['z']

            if(z > 0.5):
                t = datetime.datetime.now() 
                s = t.strftime("%H %M %S")
                s = s.split()
                f_hour = list(s[0])
                f_minute = list(s[1])
                f_second = list(s[2])

                display_binary(int(f_hour[1]), 5, green)
                display_binary(int(f_hour[0]), 6, green)
                display_binary(int(f_minute[0]), 4, yellow)
                display_binary(int(f_minute[1]), 3, yellow)
                display_binary(int(f_second[1]), 1, red)
                display_binary(int(f_second[0]), 2, red)
              
                print("x={0}, y={1}, z={2}".format(x, y, z))

    except AdventureDone:
        hat.show_message("program finishing")

def main_watch2():
    pass


while True:
    for event in sense.stick.get_events():
    hat.stick.direction_up = main_watch
    hat.stick.direction_down = down(event)

        


            