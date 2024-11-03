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
# Callback function to execute when an IR code is received
def ir_callback(data, addr, _):
    print(f"Received NEC command! Data: 0x{data:02X}, Addr: 0x{addr:02X}")
    if data == 1:
        #Led1.toggle()
        motor_Forward()
    elif data == 2:
        #Led2.toggle()
        motor_Reverse()
    elif data == 3:
        #Led3.toggle()
        motor_Left()
    elif data == 4:
        motor_right()
# Motor control (0x1, 0x2, 0x3, 0x4)
def motor_Forward():
    print("Motor Forward") # Print to REPL
    ain1_ph.high()
    ain2_en.duty_u16(65535-pwm)
    bin1_ph.high()
    bin2_en.duty_u16(65535-pwm)

def motor_Reverse():
    print("Motor Reverse") # Print to REPL
    ain1_ph.low()
    ain2_en.duty_u16(pwm)
    bin1_ph.low()
    bin2_en.duty_u16(pwm)


def motor_Left():
    print("Motor Left") # Print to REPL
    ain1_ph.high()
    ain2_en.duty_u16(65535-pwm)
    bin1_ph.low()
    bin2_en.duty_u16(pwm)

def motor_right():
    print("motor_right")
    ain1_ph.low()
    ain2_en.duty_u16(pwm)
    bin1_ph.high()
    bin2_en.duty_u16(65535-pwm)
# Setup the IR receiver
ir_pin = Pin(17, Pin.IN, Pin.PULL_UP) # Adjust the pin number based on your wiring
ir_receiver = NEC_8(ir_pin, callback=ir_callback)
# Optional: Use the print_error function for debugging
ir_receiver.error_function(print_error)
# Main loop to keep the script running
while True:
    pass # Execution is interrupt-driven, so just keep the script alive