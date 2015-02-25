#!/usr/bin/python
__author__ = 'Scott'
#keypad_test2.py
#Secondary thought process to testing the keypad - new code style trial

#import GPIO
import RPi.GPIO as GPIO

#import time for debounce
import time

#set pinmode
GPIO.setmode(GPIO.BCM)

#pin variables:


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

#input('Press enter to start the test\n Press ctrl+c end the test')
#print('enter 4 digits')


class digit():


	def key(channel):
		if GPIO.input(r1) and GPIO.input(c1):
			print("1")

		if GPIO.input(r1) and GPIO.input(c2):
			print("2")

		if GPIO.input(r1) and GPIO.input(c3):
			print("3")

		if GPIO.input(r2) and GPIO.input(c1):
			print("4")

		if GPIO.input(r2) and GPIO.input(c2):
			print("5")

		if GPIO.input(r2) and GPIO.input(c3):
			print("6")

		if GPIO.input(r3) and GPIO.input(c1):
			print("7")

		if GPIO.input(r3) and GPIO.input(c2):
			print("8")

		if GPIO.input(r3) and GPIO.input(c3):
			print("9")

		if GPIO.input(r4) and GPIO.input(c1):
			print("*")

		if GPIO.input(r4) and GPIO.input(c2):
			print("0")

		if GPIO.input(r4) and GPIO.input(c3):
			print("#")





#	def row_1(channel):
#		if GPIO.input(r1) and GPIO.input(c1):
#			print("OMFG")

#		if GPIO.input(r1):
#			print("key1")



#	def column_a(channel):   #changed pin 14 to variable "ca"
#		if GPIO.input(c1):
#			print ("column_a")






GPIO.add_event_detect(r1, GPIO.RISING, callback=digit.key, bouncetime=300)
GPIO.add_event_detect(r2, GPIO.RISING, callback=digit.key, bouncetime=300)
GPIO.add_event_detect(r3, GPIO.RISING, callback=digit.key, bouncetime=300)
GPIO.add_event_detect(r4, GPIO.RISING, callback=digit.key, bouncetime=300)

def column(channel):
	GPIO.add_event_detect(c1, GPIO.RISING, callback=digit.column, bouncetime=300)
	GPIO.add_event_detect(c2, GPIO.RISING, callback=digit.column, bouncetime=300)
	GPIO.add_event_detect(c3, GPIO.RISING, callback=digit.column, bouncetime=300)







#GPIO.add_event_detect(r1, GPIO.RISING, callback=digit.row_1, bouncetime=300)
#GPIO.add_event_detect(r2, GPIO.RISING, callback=digit.row_1, bouncetime=300)
#GPIO.add_event_detect(r3, GPIO.RISING, callback=digit.row_1, bouncetime=300)
#GPIO.add_event_detect(r4, GPIO.RISING, callback=digit.row_1, bouncetime=300)

#GPIO.add_event_detect(c1, GPIO.RISING, callback=digit.column_a, bouncetime=300)
#GPIO.add_event_detect(c2, GPIO.RISING, callback=digit.column_a, bouncetime=300)
#GPIO.add_event_detect(c3, GPIO.RISING, callback=digit.column_a, bouncetime=300)


#dumy code to keep program running
try:
	print("waiting for button")
	GPIO.wait_for_edge(24, GPIO.RISING)
except KeyboardInterrupt:
	GPIO.cleanup()
GPIO.cleanup()
