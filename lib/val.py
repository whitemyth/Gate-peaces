from time import sleep

import board
import busio
from digitalio import Direction, Pull
from RPi import GPIO
from adafruit_mcp230xx.mcp23017 import MCP23017
import smbus

output_map = {
    
}

i2c = busio.I2C(board.SCL, board.SDA)

mcp = MCP23017(i2c, address=0x21)

pins = []
for pin in range(0, 16):
    pins.append(mcp.get_pin(pin))

for pin in pins:
    pin.direction = Direction.INPUT
    pin.pull = Pull.UP

mcp.interrupt_enable = 0xFFFF  # Enable Interrupts in all pins

mcp.interrupt_configuration = 0x0000  # interrupt on any change
mcp.io_control = 0x44  # Interrupt as open drain and mirrored
mcp.clear_ints()  # Interrupts need to be cleared initially

bus = smbus.SMBus(1)

def setup():
    GPIO.add_event_detect(interrupt, GPIO.FALLING, callback = print_interrupt, bouncetime=100)

def handle_bottom_row(col):
    if col == 1:
        return 0
    else:
        pass #clear screen or whatever
    return -1


def print_interrupt(port):
    """Callback function to be called when an Interrupt occurs."""
    sleep(0.1)
    #output = bus.read_i2c_block_data(0x21, 0x01)
    
    #print(output[17])
    
    #row = pins[mcp.int_flag[0]]
    #if not row.value:
    #    print("Release")
    #else:
    #    col = pins[mcp.int_flag[1]]
    #    if row == 3:
    #        num = handle_bottom_row(col)
    #    else:
    #        num = (row - 4) * 3 + (3 - col)
    #    print(num)
    #for pin_flag in mcp.int_flag:
    #    print("Interrupt connected to Pin: {}".format(port))
    #    print("Pin number: {} changed to: {}".format(pin_flag, pins[pin_flag].value))
    
    vals = []
    for i, pin in enumerate(pins[0:7]):
        if pin.value:
            vals.append(i)
    if len(vals) > 0:
        row = vals[0]
        col = vals[1]
        print(row, col)
    else:
        pass
    mcp.clear_ints()
    sleep(0.1)


# connect either interrupt pin to the Raspberry pi's pin 17.
# They were previously configured as mirrored.
GPIO.setmode(GPIO.BCM)
interrupt = 16
GPIO.setup(interrupt, GPIO.IN, GPIO.PUD_UP)  # Set up Pi's pin as input, pull up

# The add_event_detect fuction will call our print_interrupt callback function
# every time an interrupt gets triggered.
setup()

# The following lines are so the program runs for at least 60 seconds,
# during that time it will detect any pin interrupt and print out the pin number
# that changed state and its current state.
# The program can be terminated using Ctrl+C. It doesn't matter how it
# terminates it will always run GPIO.cleanup().
try:
    print("When button is pressed you'll see a message")
    sleep(60)  # You could run your main while loop here.
    print("Time's up. Finished!")
finally:
    GPIO.cleanup()