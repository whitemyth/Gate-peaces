#!/usr/bin/python
#lcd_test.py

#LCD hardware test for the Gtate system

#requires Adafruit_CharLCD and Adafruit_GPIO.MCP230xx

import time

from lib.LCD_Python2 import Adafruit_CharLCD as LCD
import Adafruit_GPIO.MCP230xx as MCP

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

#initialize i2c chip using default 0x20 address

gpio = MCP.MCP23017()

#Initialize LCD
lcd = LCD.Adafruit_RGBCharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
							lcd_columns, lcd_rows, lcd_red, lcd_green, lcd_blue, gpio=gpio)


# LCD commands

# time.sleep(1.0)  - wait x seconds

#lcd.clear()  -clear the screen

#lcd.show_cursor(True) - show/hide lcd cursor
#lcd.show_cursor(False)

#lcd.blink(True)  - blink lcd cursor
#lcd.blink(False) - stop lcd cursor blinking

#lcd.message('your message here')   - prints on lcd

# scrolling message  right & left
#message = 'your message here'
#lcd.message(message)
#for i in range(lcd_columns-len(message)):
#	time.sleep(0.5)
#	lcd.move_right()
#for i in range(lcd_columns-len(message)):
#	time.sleep(0.5)
#	lcd.move_left()

#turn backlight off /on
#lcd.set_backlight(0)
#lcd.set_backlight(1)

#backlight color
#lcd.set_color(1.0,0.0,0.0)   - (red value, green value, blue value)

#test of the LCD :
lcd.set_color(1.0,0.0,1.0)
lcd.message ('this is a test/n of the LCD')
time.sleep(2.0)
lcd.clear()


lcd.set_color(0.0,0.0,5.0)
lcd.message('standby mode')
time.sleep(2.0)
lcd.clear()

lcd.set_color(1.0,0.0,0.0)
lcd.message('Invalid code')
time.sleep(0.2)
lcd.set_backlight(0)
time.sleep(0.5)
lcd.set_backlight(1)
time.sleep(0.5)
lcd.set_backlight(0)
time.sleep(0.5)
lcd.set_backlight(1)
lcd.clear()
lcd.set_color(0.0,0.0,1.0)

time.sleep(2.0)
lcd.set_color(0.0,1.0,0.0)
lcd.message("welcome/nGuest's name")
time.sleep(2.0)
lcd.clear()

lcd.set_color(0.0,0.0,0.5)
lcd.message('standby')
