#!/usr/bin/python
#lckey.py
#combination of LCD and Keypad used together


import math, sys
from time import sleep
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate

import RPi.GPIO as GPIO

#LCD init and screen size
lcd = Adafruit_CharLCDPlate()
lcd.begin(16, 2)

#keypad GPIO setup
GPIO.setmode(GPIO.BCM)

# Keypad pin variables:
r1=14
r2=15
r3=18
r4=23
c1=17
c2=27
c3=22
# Set as input and pulled down  - connected to 3V3 on button press
GPIO.setup(r1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  #Row1
GPIO.setup(r2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  #Row2
GPIO.setup(r3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  #Row3
GPIO.setup(r4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  #Row4
GPIO.setup(c1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  #column A
GPIO.setup(c2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  #column B
GPIO.setup(c3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  #column C

GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #dummy pin to keep code alive - remove later


#body


class keyValue:

    def getDigit(self, name):
        self.name=name
        return(self.name)

    def digit(channel):
        return(name.channel)
        if GPIO.input(r1) and GPIO.input(c1):
            channel == 1
        return (channel)


button1 =keyValue()
button1.getDigit(1)
number1 = button1.digit
print(number1)







'''

class digit():    # finds key pad digits



    def key(channel):
        if GPIO.input(r1) and GPIO.input(c1):
            print("1")
            lcd.message("1")


        if GPIO.input(r1) and GPIO.input(c2):
            print("2")
            lcd.message("2")

        if GPIO.input(r1) and GPIO.input(c3):
            print("3")
            lcd.message("3")

        if GPIO.input(r2) and GPIO.input(c1):
            print("4")
            lcd.message("4")

        if GPIO.input(r2) and GPIO.input(c2):
            print("5")
            lcd.message("5")

        if GPIO.input(r2) and GPIO.input(c3):
            print("6")
            lcd.message("6")

        if GPIO.input(r3) and GPIO.input(c1):
            print("7")
            lcd.message("7")

        if GPIO.input(r3) and GPIO.input(c2):
            print("8")
            lcd.message("8")

        if GPIO.input(r3) and GPIO.input(c3):
            print("9")
            lcd.message("9")

        if GPIO.input(r4) and GPIO.input(c1):
            print("*")
            lcd.message("*")

        if GPIO.input(r4) and GPIO.input(c2):
            print("0")
            lcd.message("0")

        if GPIO.input(r4) and GPIO.input(c3):
            print("#")
            lcd.message("#")
 '''







#keypad detetcs

GPIO.add_event_detect(r1, GPIO.RISING, callback=keyValue.digit, bouncetime=300)
GPIO.add_event_detect(r2, GPIO.RISING, callback=keyValue.digit, bouncetime=300)
GPIO.add_event_detect(r3, GPIO.RISING, callback=keyValue.digit, bouncetime=300)
GPIO.add_event_detect(r4, GPIO.RISING, callback=keyValue.digit, bouncetime=300)




#GPIO.add_event_detect(r1, GPIO.RISING, callback=digit.key, bouncetime=300)
#GPIO.add_event_detect(r2, GPIO.RISING, callback=digit.key, bouncetime=300)
#GPIO.add_event_detect(r3, GPIO.RISING, callback=digit.key, bouncetime=300)
#GPIO.add_event_detect(r4, GPIO.RISING, callback=digit.key, bouncetime=300)




#dumy code to keep program running
try:
	print("waiting for button")
	GPIO.wait_for_edge(24, GPIO.RISING)
except KeyboardInterrupt:
	GPIO.cleanup()
GPIO.cleanup()







'''pass objects in
[6:40:11 PM] Alexander Reitzel: and call functions
[6:40:31 PM] Alexander Reitzel: use the constructor of the class containing the key method
'''










