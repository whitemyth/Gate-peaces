
#!/usr/bin/python

from datetime import datetime
import time

from lib.LCD_Python2 import Adafruit_CharLCD as LCD


lcd = LCD.Adafruit_CharLCDPlate()


lcd_columns = 16
lcd_rows = 2




#clock set to refresh on the minute  -precisely
while True:
	t = datetime.utcnow()
	sleeptime = 60 - (t.second + t.microsecond/1000000.0)
	lcd.clear()
	lcd.set_color(1.0,0.0,0.0)
	lcd.message(datetime.now().strftime('    %x\n     %I:%M%p'))
	time.sleep(sleeptime)

#clock set to refresh every 2seconds instead of on the minute 
'''
while 1:
	#if datetime.now().strftime(%S) == 0: 
	lcd.clear()
	lcd.set_color(1.0,0.0,0.0)
	lcd.message(datetime.now().strftime('    %x\n     %I:%M%p'))
	sleep(2)
'''	
	
	
	