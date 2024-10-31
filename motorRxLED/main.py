import machine
import math, time
from machine import Pin
from machine import PWM
from ir_rx.nec import NEC_8 # Use the NEC 8-bit class
from ir_rx.print_error import print_error # for debugging
Led1 = Pin(15, Pin.OUT)
Led2 = Pin(14, Pin.OUT)
Led3 = Pin(11, Pin.OUT)
pwm_rate = 2000
ain1_ph = Pin(12, Pin.OUT) # Initialize GP14 as an OUTPUT
ain2_en = PWM(13, freq = pwm_rate, duty_u16 = 0)
pwm = min(max(int(2**16 * abs(1)), 0), 65535)
# Callback function to execute when an IR code is received
def ir_callback(data, addr, _):
    print(f"Received NEC command! Data: 0x{data:02X}, Addr: 0x{addr:02X}")
    if data == 1:
        Led1.toggle()
        motor_on()
    elif data == 2:
        Led2.toggle()
        motor_toggle()
    elif data == 3:
        Led3.toggle()
        motor_off()
# Motor control (0x1, 0x2, 0x3)
def motor_on():
    print("Motor ON") # Print to REPL
    ain1_ph.low()
    ain2_en.duty_u16(pwm)

def motor_off():
    print("Motor OFF") # Print to REPL
    ain1_ph.low()
    ain2_en.duty_u16(0)

def motor_toggle():
    print("Motor toggle") # Print to REPL
    ain1_ph.toggle()
    ain2_en.duty_u16(0)
# Setup the IR receiver
ir_pin = Pin(17, Pin.IN, Pin.PULL_UP) # Adjust the pin number based on your wiring
ir_receiver = NEC_8(ir_pin, callback=ir_callback)
# Optional: Use the print_error function for debugging
ir_receiver.error_function(print_error)
# Main loop to keep the script running
while True:
    pass # Execution is interrupt-driven, so just keep the script alive