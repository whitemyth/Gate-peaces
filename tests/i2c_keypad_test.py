#!/usr/bin/env python3

#from .usr.local.include.python2.7 
import wiringpi as wiringpi
from time import sleep   
import time #only need time_stamp funciton - unknown name to import just that

pin_base = 65       # lowest available starting number is 65 (65=A0, 73=B0 etc)
i2c_addr = 0x21     # A0, A1, A2 pins all wired to GND

wiringpi.wiringPiSetup()                    # initialise wiringpi
wiringpi.mcp23017Setup(pin_base,i2c_addr)   # set up the pins and i2c address

#wiringpi.pinMode(x, y)        x=pin number  y=input or output (1=output 0=input) "wiringpi.pinmode(65,0)" pin 65 input 
#wiringpi.digitalWrite(X, B)   X=pin number  B= 0ff/on (0v/3v3)  (0=off, 1=on)  "wiringpi.digitalWrite(65,0)"  pin 65 off
#wiringpi.pullUpDncontro(X, D) X=pin number  D= internal pull up/dn/clear  2=up 1=dn 0=deactivate  

wiringpi.pinMode(72, 0)         # sets GPB7 to input
wiringpi.pinMode(71, 0)
wiringpi.pinMode(70, 0)
wiringpi.pinMode(69, 0)
wiringpi.pinMode(68, 0)
wiringpi.pinMode(67, 0)
wiringpi.pinMode(66, 0)
wiringpi.pinMode(65, 1) #led for testing

time_stamp = time.time()

#wiringpi.pullUpDnControl(73, 0) # set internal pull-up/dn/clear
#wiringpi.pullUpDnControl(74, 0)
#wiringpi.pullUpDnControl(75, 0)
#wiringpi.pullUpDnControl(76, 0)
#wiringpi.pullUpDnControl(65, 0)
#wiringpi.pullUpDnControl(66, 0)
#wiringpi.pullUpDnControl(67, 0) 

#wiringpi.digitalWrite(80,0) # led on/off


try:
    while True:
        if  wiringpi.digitalRead(65) and wiringpi.digitalRead(68):
            time_stamp       # put in to debounce  
            time_now = time.time()  
            if (time_now - time_stamp) >= 0.3:  
                print ('1')
            time_stamp = time_now    
        elif wiringpi.digitalRead(66) and wiringpi.digitalRead(68):
            time_stamp       # put in to debounce  
            time_now = time.time()  
            if (time_now - time_stamp) >= 0.3:  
                print ('2')
            time_stamp = time_now
        elif wiringpi.digitalRead(67) and wiringpi.digitalRead(68):
            time_stamp       # put in to debounce  
            time_now = time.time()  
            if (time_now - time_stamp) >= 0.3:  
                print ('3')
            time_stamp = time_now
        elif wiringpi.digitalRead(65) and wiringpi.digitalRead(69):
            time_stamp       # put in to debounce  
            time_now = time.time()  
            if (time_now - time_stamp) >= 0.3:  
                print ('4')
            time_stamp = time_now
        elif wiringpi.digitalRead(66) and wiringpi.digitalRead(69):
            time_stamp       # put in to debounce  
            time_now = time.time()  
            if (time_now - time_stamp) >= 0.3:  
                print ('5')
            time_stamp = time_now
        elif wiringpi.digitalRead(67) and wiringpi.digitalRead(69):
            time_stamp       # put in to debounce  
            time_now = time.time()  
            if (time_now - time_stamp) >= 0.3:  
                print ('6')
            time_stamp = time_now
        elif wiringpi.digitalRead(65) and wiringpi.digitalRead(70):
            time_stamp       # put in to debounce  
            time_now = time.time()  
            if (time_now - time_stamp) >= 0.3:  
                print ('7')
            time_stamp = time_now
        elif wiringpi.digitalRead(66) and wiringpi.digitalRead(70):
            time_stamp       # put in to debounce  
            time_now = time.time()  
            if (time_now - time_stamp) >= 0.3:  
                print ('8')
            time_stamp = time_now
        elif wiringpi.digitalRead(67) and wiringpi.digitalRead(70):
            time_stamp       # put in to debounce  
            time_now = time.time()  
            if (time_now - time_stamp) >= 0.3:  
                print ('9')
            time_stamp = time_now
        elif wiringpi.digitalRead(65) and wiringpi.digitalRead(71):
            time_stamp       # put in to debounce  
            time_now = time.time()  
            if (time_now - time_stamp) >= 0.3:  
                print ('*')
            time_stamp = time_now
        elif wiringpi.digitalRead(66) and wiringpi.digitalRead(71):
            time_stamp       # put in to debounce  
            time_now = time.time()  
            if (time_now - time_stamp) >= 0.3:  
                print ('0')
            time_stamp = time_now            
        elif wiringpi.digitalRead(67) and wiringpi.digitalRead(71):
            time_stamp       # put in to debounce  
            time_now = time.time()  
            if (time_now - time_stamp) >= 0.3:  
                print ('#')
            time_stamp = time_now   
        else:
            wiringpi.digitalWrite(80, 0) 
        sleep(0.05)
finally:
    wiringpi.digitalWrite(80, 0) # sets port GPA1 to 0 (0V, off)
    wiringpi.pinMode(65, 0)      # sets GPIO GPA1 back to input Mode



'''
try:
    while True:
        if  wiringpi.digitalRead(72): 
            wiringpi.digitalWrite(80, 1) # sets port GPA1 to 1 (3V3, on)
            print ('test')
        else:
            wiringpi.digitalWrite(80, 0) 
        sleep(0.05)
finally:
    wiringpi.digitalWrite(80, 0) # sets port GPA1 to 0 (0V, off)
    wiringpi.pinMode(65, 0)      # sets GPIO GPA1 back to input Mode
'''
'''
try:
    while True:
        if  wiringpi.digitalRead(73): 
            wiringpi.digitalWrite(80, 1) # sets port GPA1 to 1 (3V3, on)
            print ('test')
        else:
            wiringpi.digitalWrite(80, 0) 
        sleep(0.05)
finally:
    wiringpi.digitalWrite(80, 0) # sets port GPA1 to 0 (0V, off)
    wiringpi.pinMode(65, 0)      # sets GPIO GPA1 back to input Mode
'''    
