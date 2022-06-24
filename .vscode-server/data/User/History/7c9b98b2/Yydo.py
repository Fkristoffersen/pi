#!/usr/bin/env python
from sense_hat import SenseHat
import time, datetime
import signal
import sys

hat = SenseHat() #Raspberry features

class AdventureDone(Exception): pass # Try catch exception
#Colours used to show the time/message
blue = (0, 0, 255)
yellow = (255, 255, 0)
day_color = (255, 0, 0)
green = (0, 255, 0)
dark_yellow = (127, 127, 0)
red = (255, 0, 0)
off = (0, 0, 0)

hat.show_message("Program starting", text_colour=yellow, back_colour=blue, scroll_speed=0.05) #Message shown on startup

def display_binary(value, row, color): #Function for the 3 digit clock
    binary_str = '{0:8b}'.format(value)
    for x in range(0, 8): #For loop for which pixels to turn on
        if binary_str[x] == "1":
            hat.set_pixel(x, row, color)
        else:
            hat.set_pixel(x, row, off)

def down(event): #Function for shutting down the program
    print("Clear") 
    hat.clear() #Turns off all the lights on the clock
    raise AdventureDone #Try catch exception

def pushed_left(): #Function for the 3 digit clock
    hat.clear() #Clears raspberry pi
    t = datetime.datetime.now() #Current time
    display_binary(t.hour, 3, green)
    display_binary(t.minute, 4, yellow)
    display_binary(t.second, 5, red)
    for event in hat.stick.get_events(): #For loop to check for direction
        print(event.direction, event.action) #Console print for direction
        if event.direction == 'down': #If down is pushed go to down function
            down(event)

def main_watch(): #6 digit clock
    try:
        while True:
            acceleration = hat.get_accelerometer_raw() #Used to check angled of raspberry
            x = acceleration['x']
            y = acceleration['y']
            z = acceleration['z']

            if(z > 0.5): #If raspberry is angled run code:
                t = datetime.datetime.now() #Current time
                s = t.strftime("%H %M %S")#Hour Minutes and seconds
                s = s.split() #Splits to get 2 digits of Hour, min and sec each
                f_hour = list(s[0])
                f_minute = list(s[1])
                f_second = list(s[2])

                #Where to colour
                display_binary(int(f_hour[1]), 5, green) 
                display_binary(int(f_hour[0]), 6, green)
                display_binary(int(f_minute[0]), 4, yellow)
                display_binary(int(f_minute[1]), 3, yellow)
                display_binary(int(f_second[1]), 1, red)
                display_binary(int(f_second[0]), 2, red)
              
                print("x={0}, y={1}, z={2}".format(x, y, z))
                for event in hat.stick.get_events(): #Checks for user input
                    if event.direction == 'down':
                        down(event)
           
            elif (x > 0.5):
                hat.clear()
                pushed_left()

            elif (y < -0.5 and x < 0.0): #If Raspberry postion is: 12hour clock is shown
                t = datetime.datetime.now() #Current time
                s = t.strftime("%H %M %S")#Hour Minutes and seconds
                s = s.split()#Splits to get 2 digits of Hour, min and sec each
                f_hour = list(s[0])
                f_minute = list(s[1])
                f_second = list(s[2])
                
                #Where to colour
                display_binary(int(f_hour[1]), 5, dark_yellow)
                display_binary(int(f_hour[0]), 6, green)
                display_binary(int(f_minute[0]), 4, yellow)
                display_binary(int(f_minute[1]), 3, yellow)
                display_binary(int(f_second[1]), 1, red)
                display_binary(int(f_second[0]), 2, red)
                print(s)
                
    except AdventureDone: #Exit program
            hat.show_message("program finishing")
        
def handler(signum, frame):
    print('Shutting down...')
    hat.show_message("program finishing")
    sys.exit(1)
signal.signal(signal.SIGTERM, handler)
while True: #Main loop
    for event in hat.stick.get_events(): #Looks for user input
        hat.stick.direction_up = main_watch() #If user input = up main-watch function is called
        hat.stick.direction_down = down(event) #Down function called 
 