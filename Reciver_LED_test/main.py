import machine
from machine import Pin
from ir_rx.nec import NEC_8 # Use the NEC 8-bit class
from ir_rx.print_error import print_error # for debugging
Led1 = Pin(15, Pin.OUT)
Led2 = Pin(14, Pin.OUT)
Led3 = Pin(13, Pin.OUT)
# Callback function to execute when an IR code is received
def ir_callback(data, addr, _):
    print(f"Received NEC command! Data: 0x{data:02X}, Addr: 0x{addr:02X}")
    if data == 1:
        Led1.toggle()
    elif data == 2:
        Led2.toggle()
    elif data == 3:
        Led3.toggle()
# Setup the IR receiver
ir_pin = Pin(17, Pin.IN, Pin.PULL_UP) # Adjust the pin number based on your wiring
ir_receiver = NEC_8(ir_pin, callback=ir_callback)
# Optional: Use the print_error function for debugging
ir_receiver.error_function(print_error)
# Main loop to keep the script running
while True:
    pass # Execution is interrupt-driven, so just keep the script alive