import machine
import math, time
from machine import Pin
from machine import PWM
from ir_rx.nec import NEC_8 # Use the NEC 8-bit class
from ir_rx.print_error import print_error # for debugging
pwm_rate = 2000
ain1_ph = Pin(12, Pin.OUT) # Initialize GP14 as an OUTPUT
ain2_en = PWM(13, freq = pwm_rate, duty_u16 = 0)
bin1_ph = Pin(14, Pin.OUT) # Initialize GP14 as an OUTPUT
bin2_en = PWM(15, freq = pwm_rate, duty_u16 = 0)
pwm = min(max(int(2**16 * abs(1)), 0), 65535)
#pins for rf reciever pullup
p18 = Pin(18, Pin.IN, Pin.PULL_UP)
p19 = Pin(19, Pin.IN, Pin.PULL_UP)
p20 = Pin(20, Pin.IN, Pin.PULL_UP)
p21 = Pin(21, Pin.IN, Pin.PULL_UP)
IR_t = 0
RF_int = 0
IR_int = 0

#####################################################################################
# Callback function to execute when an IR code is received
def ir_callback(data, addr, _):
    print(f"Received NEC command! Data: 0x{data:02X}, Addr: 0x{addr:02X}")
    if (data == 1 and IR_t):
        #Led1.toggle()
        motor_Forward()
    elif (data == 2 and IR_t):
        #Led2.toggle()
        motor_Reverse()
    elif (data == 3 and IR_t):
        #Led3.toggle()
        motor_Left()
    elif (data == 4 and IR_t):
        motor_right()
    elif data == 5:
        global IR_int
        global RF_int
        RF_int = False
        IR_int = True
        print("IR selected")
    elif data == 6:
        global IR_int
        global RF_int
        RF_int = 1
        IR_int = 0
        print("RF selected")
    
# Setup the IR receiver
ir_pin = Pin(17, Pin.IN, Pin.PULL_UP) # Adjust the pin number based on your wiring
ir_receiver = NEC_8(ir_pin, callback=ir_callback)
# Optional: Use the print_error function for debugging
ir_receiver.error_function(print_error)

######################################################################################
#input 1 callback
def callback1(p18):
    if RF_int:
        motor_Forward()

p18.irq(trigger=Pin.IRQ_RISING, handler=callback1)

#input 2 callback
def callback2(p19):
    if RF_int:
        motor_Reverse()

p19.irq(trigger=Pin.IRQ_RISING, handler=callback2)

#input 3 callback
def callback3(p20):
    if RF_int:
        motor_Left()

p20.irq(trigger=Pin.IRQ_RISING, handler=callback3)

#input 4 callback
def callback4(p21):
    if RF_int:
        motor_right()

p21.irq(trigger=Pin.IRQ_RISING, handler=callback4)

# Motor control (0x1, 0x2, 0x3, 0x4)
def motor_Forward():
    print("Motor Forward") # Print to REPL
    ain1_ph.low()
    ain2_en.duty_u16(pwm)
    bin1_ph.low()
    bin2_en.duty_u16(pwm)

def motor_Reverse():
    print("Motor Reverse") # Print to REPL
    ain1_ph.high()
    ain2_en.duty_u16(pwm)
    bin1_ph.high()
    bin2_en.duty_u16(pwm)


def motor_Left():
    print("Motor Left") # Print to REPL
    ain1_ph.high()
    ain2_en.duty_u16(pwm)
    bin1_ph.low()
    bin2_en.duty_u16(pwm)

def motor_right():
    print("motor_right")
    ain1_ph.low()
    ain2_en.duty_u16(pwm)
    bin1_ph.high()
    bin2_en.duty_u16(pwm)

# Main loop to keep the script running
while True:
    if IR_int:
        IR_t = 1
    else:
        IR_t = 0