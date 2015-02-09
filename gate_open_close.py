#!usr/bin/python
#gate_open_close.py

# a code to send GPIO open and close commands for gate control

import RPi.GPIO as GPIO   
GPIO.setmode(GPIO.BCM)    #importing GPIO library and setting pins to BCM numbering. 


# I am unsure if I have the down's and up's correct

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  #this pin will monitor for gate "closed" status
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  #this pin will monitor for gate "open" status
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  #this pin will monitor for gate "moving" status


GPIO.setup(26, GPIO.OUT, pull_up_down=GPIO.PUD_UP)  #this pin will activate the relay  to "open" or "lock open" the gate



def gate_status():
		
	try:
			GPIO.wait_for_edge(23, GPIO.RISING)    # this will notify when the gate is closed (hopefuly one time)
			print "Gate Closed\n"
	
			GPIO.wait_for_edge(pinY, GPIO.RISING)  # this will notify when the gate is open 
			print "Gate Open"
	
			GPIO.wait_for_edge(pinZ, GPIO.RISING)  # this will notify when the gate  is moving (if possible read previous status, and indicate if opening or closing)
			print "Gate Moving"
		
	 	
	
	
	
	
	
	except KeyboardInterrupt:
		GPIO.cleanup()   #clean up after ctrl+c exit
GPIO.cleanup()		# clean up after normal exit 
