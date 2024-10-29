import machine
import time
from machine import Pin
from time import sleep_ms
led1 = Pin(12, Pin.OUT)
led2 = Pin(12, Pin.OUT)
led3 = Pin(12, Pin.OUT)

led1.off()
led2.off()
led3.off()

while True:
    led1.toggle()
    led2.toggle()
    led3.toggle()
    sleep_ms(300)
