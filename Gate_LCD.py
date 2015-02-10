#!/usr/bin/python
#Gate_LCD.py
# LCD display hooked up with MCP23017 IC

#this is a simple start to the lcd commands for the gate - the commands should be able to be put right into one of the other scripts just referencing a setup file similar to this


import math
import time
import Adafruit_CharLCD as LCD
import Adafruit_GPIO.MCP230xx as MCP

#MCP pin layout

lcd_rs = 0
lcd_en = 1
lcd_d4 = 2
lcd_d5 =3
lcd_d6 = 4
lcd_d7 = 5
lcd_red =6
lcd_green = 7
lcd_blue = 8


#LCD size
lcd_columns = 16
lcd_rows = 2

gpio = MCP.MCP23017()   #sets MCP23017 to default addres on ic2 (0x20)

#initialize LCD variables?
lcd = LCD.Adafruit_RGBCharLCD(lcd+rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_red, lcd_green, lcd_blue, gpio=gpio)

display= raw=input('enter text to display on LCD: ' )
lcd.set_backlight(1) #turn on backlight
lcd.message('Welcome to\nOur Stables!')  #prints a two line message
time.sleep(3.0) #take a 3 second break
lcd.clear() # clear
lcd.message(display)  # should display what ever is set to "display" from keyboard imput

#fin
