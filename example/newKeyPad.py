import RPI.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(y,GPIO.OUT)
GPIO.setup(y,GPIO.HIGH)

GPIO.setup(x,GPIO.IN)
GPIO.setup(x,GPIO.LOW)
GPIO.setup(x,GPIO.IN)
GPIO.setup(x,GPIO.LOW)
GPIO.setup(x,GPIO.IN)
GPIO.setup(x,GPIO.LOW)
GPIO.setup(x,GPIO.IN)
GPIO.setup(x,GPIO.LOW)
GPIO.setup(x,GPIO.IN)
GPIO.setup(x,GPIO.LOW)
GPIO.setup(x,GPIO.IN)
GPIO.setup(x,GPIO.LOW)
GPIO.setup(x,GPIO.IN)
GPIO.setup(x,GPIO.LOW)
GPIO.setup(x,GPIO.IN)
GPIO.setup(x,GPIO.LOW)


#GPIO.Pin"X" donotes GPIO pin to be assigned later

GPIO.pinx = +3.3v
 
GPIO.pinx = ColA
GPIO.pinx = ColB
GPIO.pinx = ColC
GPIO.pinx = Row1
GPIO.pinx = Row2
GPIOp.inx = Row3
GPIO.pinx = Row4

Row1 + ColA = 1
Row1 + ColB = 2
Row1 + ColC = 3
Row2 + ColA = 4
Row2 + ColB = 5
Row2 + ColC = 6
Row3 + ColA = 7
Row3 + ColB = 8
Row3 + ColC = 9
Row4 + ColA = "*"
Row4 + ColB = 0
Row4 + ColC = "#"


#Could do something like  Row+Col = digit 
#or 12 lines of  gpip pin A +GPIO pin B  = digit
#then we need or something non processor heavy to wait for key press
#it needs to  stop after 4 digits   

#then at some point we need to tie it into sqlite3 and process the allows and denies 
#the LCD stuff is easy, it's "lcd.message('welcome Alex') " 


self.KEYPAD =[
[1,2,3],
[4,5,6],
[7,8,9],
["#",0,"#"]
]



GPIO.cleanup()

	
