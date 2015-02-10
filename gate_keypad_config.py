#!usr/bin/python
#gate_keypad_config.py

#this is a config file for the keypad when using GPIO

import RPi.GPIO as GPIO
class keypad():					#class for keypad  lays out keyboard
	def __init__(self, .self):
		GPIO.setmode(GPIO.BCM)
		self.KEYPAD = [
		[1,2,3],
		[4,5,6],
		[7,8,9],
		["*",o,"#"]
		]
	self.ROW =[GPIO PINS FOR ROWS]				#gpio pins for rows
	self.COLUMN = [GPIO PINS FOR COLUMNS]   #gpio pins for columns
	

	def getKey(self):
	
	#set output for columns low
	for j in range (len(self.COLUMN)):  #returns number of items in sequence from column (I think)
		GPIO.setup(self.column[j], GPIO.OUT)
		GPIO.output(self.COLUMN[j], GPIO.LOW)
		
		
	#set input for rows
	for i in range (len(self.ROW)):  #returns number of items in sequence from row
		GPIO.setup(self.ROW[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)
		
		
	#button scan setup
	#  rows
	rowVal = -1
	for i in range(len(self.ROW)):					#if a row value is returned it sets the value to i (I think)
		tmpRead = GPIO.input(self.ROW[i])
		if tmpRead == 0
			rowVal = i
			
		if rowVal <0 or rowVal >3:     #if no push on row is detected - no button is pushed -start over.
			self.exit()
			return
			
		for j in range (len(self.COLUMN)):
				GPIO.setup(self.COLUMN[j], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)   #changes columns to input 
				
		GPIO.setup(self.ROW[rowVal], GPIO.OUT)
		GPIO.output(self.ROW[rowVal], GPIO.HIGH)    #changes the rowval (i) to ouput when detected
		
		#columns
		
		colVal=-1
		for jin range(len(self.COLUMN)):
		tmpRead = GPIO.input(self.COLUMN[j])    #if a value is detected in a column it sets it to J
		if tmpRead == 1:
			colVal=j
			
		if colVal <- or colVal >2:   # means no button pressed and exit
		sel.exit()
		return
			
		self.exit()
		return self.KEYPAD[rowVal][colVal]  #returns the key pressed cordinates for the index
		
	def exit(self):
		for i in range(len(self.ROW)):
			GPIO.setup(self.ROW[i], GPIO.IN, pull_up_down=GPIO.PUD_up)			#resets everything
		for j in range(len(self.COLUMN)):
			GPIO.setup(self.COLUMN[j], GPIO.IN, pull_up_down=GPIO.PUD_up)
			
			
if __name__ == '__main__':  #something to do with only initializing the part called, and not the whole function?

	kp = keypad()  # initializes the keypad class
	
	digit = None
	while digit == None:  #keeps it going
		digit =kp.getKey()
	

	print digit  #results
			
			
			
			
			
			
			
			
			
			
