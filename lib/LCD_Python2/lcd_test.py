#!/usr/bin/python
#lcd_test.py

#LCD hardware test for the Gtate system



import time

from lib.LCD_Python2 import Adafruit_CharLCD as LCD

#Initialize LCD

lcd = LCD.Adafruit_CharLCDPlate()
			


#MCP pins for LCD

lcd_rs        = 0
lcd_en        = 1
lcd_d4        = 2
lcd_d5        = 3
lcd_d6        = 4
lcd_d7        = 5
lcd_red       = 6
lcd_green     = 7
lcd_blue      = 8

#define size of LCD
lcd_columns = 16
lcd_rows =2




# LCD commands

# time.sleep(1.0)  - wait x seconds

#lcd.clear()  -clear the screen

#lcd.show_cursor(True) - show/hide lcd cursor
#lcd.show_cursor(False)

#lcd.blink(True)  - blink lcd cursor
#lcd.blink(False) - stop lcd cursor blinking


# scrolling message  right & left
#could not get scrolling to work.

'''
lcd.message()  # - prints on lcd
message = 'message'
lcd.clear()
lcd.message(message)
for i in range(lcd_columns-len(message)):
	time.sleep(1.0)
	lcd.move_right(1.0)
#for i in range(lcd_columns-len(message)):
#	time.sleep(0.5)
#	lcd.move_left()
'''
#turn backlight off /on
#lcd.set_backlight(0)
#lcd.set_backlight(1)

#backlight color
#lcd.set_color(1.0,0.0,0.0)   - (red value, green value, blue value)

#test of the LCD :

lcd.clear()
lcd.message('test')
time.sleep(5.0)
lcd.clear()

lcd.set_color(1.0,0.0,1.0)
lcd.message ('this is a test\n of the LCD')
time.sleep(2.0)
lcd.clear()


lcd.set_color(0.0,0.0,0.5)
lcd.message('standby mode')
time.sleep(2.0)
lcd.clear()

lcd.set_color(0.0,0.0,1.0)
lcd.message('active mode')
time.sleep(2.0)
lcd.clear()

lcd.set_color(1.0,0.0,0.0)
lcd.message('Invalid code')
time.sleep(0.2)
lcd.set_backlight(0)
time.sleep(0.2)
lcd.set_color(1.0,0.0,0.0)
time.sleep(0.2)
lcd.set_backlight(0)
time.sleep(0.2)
lcd.set_color(1.0,0.0,0.0)
time.sleep(0.2)
lcd.set_backlight(0)
time.sleep(0.2)
lcd.set_color(1.0,0.0,0.0)
time.sleep(0.2)




time.sleep(1.0)
lcd.clear()
lcd.set_color(0.0,1.0,0.0)
lcd.message('Access Granted')
time.sleep(2.0)
lcd.clear()
lcd.message("   Welcome\n Guest's name")
time.sleep(2.0)
lcd.clear()

lcd.set_color(0.0,0.0,0.5)
lcd.message('standby')




 

