#!usr/bin/python
# gate_open_close.py

# a code to send GPIO open and close commands for gate control

from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)  #importing GPIO library and setting pins to BCM numbering.


# I am unsure if I have the down's and up's correct

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  #this pin will monitor for gate "closed" status
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  #this pin will monitor for gate "open" status
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  #this pin will monitor for gate "moving" status

GPIO.setup(26, GPIO.OUT, pull_up_down=GPIO.PUD_UP)  #this pin will activate the relay  to "open" or "lock open" the gate

ledPin = 1


def open():
    GPIO.output(26, 1)
    sleep(0.5)
    GPIO.output(ledPin, 0)

def hold():
    GPIO.output(ledPin, 26)

key = {'X': 'open', 'Y': 'hold'}

def gate_status():
    while True:
        GPIO.wait_for_edge(23, GPIO.RISING)
        # this will notify when the gate is closed (hopefuly one time)
        print("Gate Closed\n")

        GPIO.wait_for_edge(24, GPIO.RISING)
        # this will notify when the gate is open
        print("Gate Open")

        GPIO.wait_for_edge(25, GPIO.RISING)
        # this will notify when the gate  is moving (if possible read previous status, and indicate if opening or closing)
        print("Gate Moving")


input = input("Type lock to hold gate open. Type open to momentarily open gate.")
for letter in input:
    for symbol in key:
        if key == 'X':
            hold()
        elif key == 'Y':
            open()
        else:
            sleep(0.5)
    sleep(0.5)

GPIO.cleanup()  # clean up after normal exit