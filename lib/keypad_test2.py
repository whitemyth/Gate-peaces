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

#pin variable declarations
ca=14


# Set as input and pulled down  - connected to 3V3 on button press
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  #Row1
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  #Row2
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  #Row3
GPIO.setup(ca, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  #Row4   pin 14 set to CA variable
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  #column A
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  #column B
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  #column C


GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #dummy pin to keep code alive - remove later

#input('Press enter to start the test\n Press ctrl+c end the test')
#print('enter 4 digits')



class rows_columns():


	def row_1(channel):
		print("Row 1")

#	def column_a(channel):
#		print(column_a)

	def column_a(channel):   #changed pin 14 to variable "ca"
		if GPIO.input(ca):
			print ("column_a")



#other ideas/fails

''''
class digit(x1,x2):
			row =x1
			col = x2

	def one():



class rows()

class columns()

class digits(rows, columns)
'''



			#class digit():

#	def __int__(self,col,row):

#	def one()
#		if GPIO.input(ca, 17):
#	print("1")


GPIO.add_event_detect(17, GPIO.RISING, callback=digit.row_1, bouncetime=300)

GPIO.add_event_detect(ca, GPIO.RISING, callback=digit.column_a, bouncetime=300)

#dumy code to keep program running
try:
	print("waiting for button")
	GPIO.wait_for_edge(24, GPIO.RISING)
except KeyboardInterrupt:
	GPIO.cleanup()
GPIO.cleanup()