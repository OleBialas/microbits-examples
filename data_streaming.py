import struct
from random import randint
from microbit import *
import time

uart.init(baudrate=9600)
while True:
    display.clear()    
    val = display.read_light_level()
    display.scroll(val)
    uart.write(struct.pack("h", val))
    time.sleep(0.000001)
        
    