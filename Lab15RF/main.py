from machine import Pin
import time
import random
interruptFlag = 0
#pins for rf reciever pullup
px1 = Pin(x1, Pin.IN, Pin.PULL_UP)
px2 = Pin(x2, Pin.IN, Pin.PULL_UP)
px3 = Pin(x3, Pin.IN, Pin.PULL_UP)
px4 = Pin(x4, Pin.IN, Pin.PULL_UP)
#instantiating leds
led1 = Pin(x, Pin.OUT) #LED1
led2 = Pin(x, Pin.OUT) #LED2
led3 = Pin(x, Pin.OUT) #LED3
led4 = Pin(x, Pin.OUT) #LED4

#input 1 callback
def callback1(px1):
    global interruptFlag
    led1.toggle()
    interruptFlag = 0

px1.irq(trigger=Pin.IRQ_RISING, handler=callback1)

#input 2 callback
def callback2(px2):
    global interruptFlag
    led2.toggle()
    interruptFlag = 0

px2.irq(trigger=Pin.IRQ_RISING, handler=callback2)

#input 3 callback
def callback3(px3):
    global interruptFlag
    led3.toggle()
    interruptFlag = 0

px3.irq(trigger=Pin.IRQ_RISING, handler=callback3)

#input 4 callback
def callback4(px4):
    global interruptFlag
    led4.toggle()
    interruptFlag = 0

px4.irq(trigger=Pin.IRQ_RISING, handler=callback4)

#loop
while True:
    