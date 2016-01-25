#!/usr/bin/env python3

#from .usr.local.include.python2.7 
import wiringpi2 as wiringpi
from time import sleep

pin_base = 65       # lowest available starting number is 65
i2c_addr = 0x24     # A0, A1, A2 pins all wired to GND

wiringpi.wiringPiSetup()                    # initialise wiringpi
wiringpi.mcp23017Setup(pin_base,i2c_addr)   # set up the pins and i2c address

#wiringpi.pinMode(65, 1)         # sets GPA0 to output
#wiringpi.digitalWrite(65, 0)    # sets GPA0 to 0 (0V, off)

wiringpi.pinMode(73, 0)         # sets GPB7 to input
wiringpi.pinMode(74, 0)
wiringpi.pinMode(75, 0)
wiringpi.pinMode(76, 0)
wiringpi.pinMode(65, 0)
wiringpi.pinMode(66, 0)
wiringpi.pinMode(67, 0)

wiringpi.pullUpDnControl(73, 2) # set internal pull-up
wiringpi.pullUpDnControl(74, 2)
wiringpi.pullUpDnControl(75, 2)
wiringpi.pullUpDnControl(76, 2)
wiringpi.pullUpDnControl(65, 2)
wiringpi.pullUpDnControl(66, 2)
wiringpi.pullUpDnControl(67, 2) 

# Note: MCP23017 has no internal pull-down, so I used pull-up and inverted
# the button reading logic with a "not"

try:
    while True:
        if not wiringpi.digitalRead(73): # inverted the logic as using pull-up
            #wiringpi.digitalWrite(65, 1) # sets port GPA1 to 1 (3V3, on)
            print ('test')
        else:
            wiringpi.digitalWrite(65, 0) # sets port GPA1 to 0 (0V, off)
        sleep(0.05)
finally:
    wiringpi.digitalWrite(65, 0) # sets port GPA1 to 0 (0V, off)
    wiringpi.pinMode(65, 0)      # sets GPIO GPA1 back to input Mode
    # GPB7 is already an input, so no need to change anything
