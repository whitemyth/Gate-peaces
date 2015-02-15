#!/usr/bin/python
#gate_keypad_run.py

#a script to run for the keypad - this will need "gate_keypad_config.py" in the same folder to work.

from time import sleep


kp = RPi_GPIO.keypad()   # this did have a variable to select the type of keypad but since we do not need to select, I took it out, don't know if that was bad or not.

def digit():
	r= None
	while r==None:   # keeps running until R has a value
		r - kp.get()
	return r

print "Please enter your passcode"

d1 = digit()
print d1
sleep(.5)

d2 = digit()
print d2					#get and print digits - after testing is complete the printing should be changed to ****
sleep(.5)

d3 = digit()
print d3
sleep(.5)

d4 = digit()
print d4
sleep(.5)

print "you entered %s%s%s%s "%(d1,d2,d3,d4)  # use ?s instead of % when using sqlite
