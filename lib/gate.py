import time
from dateutil.parser import parse
import datetime
import os
from .TelegramGateBot import TelegramGateBot

#from lib.Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
import RPi.GPIO as GPIO
#from lib.MCP23017_I2C import *
#from lib.MCP23017_I2C import MCP23017_I2C
import configparser
import sqlite3
import sys
import smbus

#new imports
import board
import busio
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd

#for the keypad
from time import sleep
from digitalio import Direction, Pull
from adafruit_mcp230xx.mcp23017 import MCP23017

class Gate:
    
    def __init__(self, config_location):
        self.config = configparser.ConfigParser()
        self.config.read(config_location)
        self.db_path = self.config["DEFAULT"]["dbpath"]
        
        self.lcd = Lcd()
        self.keypad = KeypadI2C()
        self.db = ClientDatabase(self.db_path)
        
        self.keypad.set_lcd(self.lcd)
        self.keypad.set_db(self.db)
        
        self.gate_control = GateControl()
        
        self.telegram_bot = TelegramGateBot(self.config["DEFAULT"]["secret"], self.db, self.gate_control)
        
    def run(self):
        print('Hello, Pony.')

        try:
            self.telegram_bot.start()
        except:
            GPIO.cleanup()

        return 0

    @staticmethod
    def display_message_method(message):
        print(message)

class Lcd:
    def __init__(self, n_cols=16, n_rows=2):
        i2c = busio.I2C(board.SCL, board.SDA)
        self.n_cols = n_cols
        self.n_rows = n_rows
        self.lcd = character_lcd.Character_LCD_RGB_I2C(i2c, self.n_cols, self.n_rows)
        self.default_color = (0,0,100)
        
    def display_message(self, msg, color=None, duration=1, clear=True):
        self.lcd.clear()
        self.lcd.color = color or self.default_color
        self.lcd.message = msg
        time.sleep(duration)
        if clear:
            self.lcd.clear()

    def standby(self):
        self.display_message("Enter code.", )

    def awake(self):
        self.display_message("Waking up...")

    def valid_code_lcd(self, name):
        self.display_message(f"Welcome\n{name}")

    def invalid_code(self):
        self.display_message("Invalid code")

    def display(self, message):
        self.display_message(f"Code: {message}")


class GateControl:
    EXIT_PIN = 17
    HOLD_PIN = 15
    CYCLE_PIN = 14

    def open(self):
        GPIO.output(EXIT_PIN, True)
        time.sleep(0.5)
        GPIO.output(EXIT_PIN, False)

    def hold_open(self):
        GPIO.output(HOLD_PIN, True)
        self.open()

    def close(self):
        GPIO.output(HOLD_PIN, False)
        time.sleep(0.5)
        #self.open()
        #self.cycle()
        
    def cycle(self):
        GPIO.output(CYCLE_PIN, True)
        time.sleep(0.5)
        GPIO.output(CYCLE_PIN, False)


class GateMonitor:
    GATE_IS_CLOSED = 0
    GATE_IS_OPEN = 1
    GATE_CLOSING = 2
    GATE_OPENING = 3

    def __init__(self):
        self.state = self.GATE_IS_CLOSED

    def gate_is_open(self):
        if GPIO.input(29, True):
            self.state = self.GATE_IS_OPEN

    def gate_is_closed(self):
        if GPIO.input(17, True):
            self.state = self.GATE_IS_CLOSED

    def gate_is_moving(self):  # I took a stab at this one - for: gate is opening, or closing
        if GPIO.input(22, True) and self.state is self.GATE_IS_CLOSED:
            self.state = self.GATE_OPENING
        elif GPIO.input(22, True) and self.state is self.GATE_IS_OPEN:
            self.state = self.GATE_CLOSING



class ClientDatabase:

    def __init__(self, db_path):
        self.db_path = db_path
        if os.path.isfile(db_path):
            pass
        else:
            print(f"Creating new database at {db_path}")
            #db doesn't exist yet -- do the initialization
            db = sqlite3.connect(self.db_path)

            #create new table
            db.execute(
                '''
                    CREATE TABLE codes (
                    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
                    UserName text,
                    Code text UNIQUE,
                    Expiration datetime
                );
                '''
            )

            db.commit()
            db.close()
        
    def check_code(self, code):
        #check that the code is in the db, and return the associated name
        db = sqlite3.connect(self.db_path)
        cursor = db.execute(
            """SELECT * FROM codes WHERE Code=?""",
            (code, )
        )
        results = cursor.fetchall()
        db.close()
        del db
        if len(results) > 0:
            name = results[0][1]
            expiry = results[0][-1]
            if expiry:
                exp_time = datetime.datetime.strptime(expiry, "%Y-%m-%d %H:%M:%S")
                if exp_time > datetime.datetime.now():
                    return name
                else:
                    #expired code
                    return None
            else:
                #no expiration date, valid
                return name
        else:
            return None

    def add(self, name, code, expiry=None):
        if expiry:
            try:
                #try to parse expiration date, and add time if needed
                expiry_string = datetime.datetime.strftime(parse(expiry), "%Y-%m-%d %H:%M:%S")
            except:
                print("Bad datetime string")
                raise
        else:
            expiry_string = None
        db = sqlite3.connect(self.db_path)
        db.execute(
            '''INSERT INTO codes (UserName, Code, Expiration) VALUES(?,?,?)''', 
            (name, code, expiry_string)
        )
        db.commit()
        db.close()

    def delete(self, name):
        db = sqlite3.connect(self.db_path)
        print("attempting to remove", f"|{name}|")
        db.execute("""DELETE FROM codes WHERE UserName=?""", (name,))
        db.commit()
        db.close()

    def list(self):
        db = sqlite3.connect(self.db_path)
        cursor = db.execute('''SELECT UserName, Code, Expiration FROM codes''')
        results = cursor.fetchall()
        db.close()
        return results

class KeypadI2C:
    
    def parse(self, i):
        for idx in range(16):
            temp = i & 1
            if temp:
                return idx
            i = i >> 1
        return None
        
    def button_press(self, port):
        sleep(0.1)
        output = self.bus.read_i2c_block_data(0x21, 0x01)
        if output[13] == 0:
            print("Release")
        else:
            num = self.parse(output[13])
            print(num)
            self.buffer += str(num)
            self.lcd.display_message(self.buffer, duration=0, clear=False)
            if len(self.buffer) == 4:
                #this is taking place in a separate interrupt thread
                # so we can't pass in the main db context
                # this really smells :<
                print("send code")
                name = self.db.check_code(self.buffer)
                self.buffer = ""
                if name:
                    self.lcd.valid_code_lcd(name)
                else:
                    self.lcd.invalid_code()
        self.mcp.clear_ints()
        sleep(0.1)

    def __init__(self):
        print("setting up keypad...")
        self.buffer = ""
        
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.mcp = MCP23017(self.i2c, address=0x21)
        
        pins = []
        for pin in range(0, 16):
            pins.append(self.mcp.get_pin(pin))

        for pin in pins:
            pin.direction = Direction.INPUT
            pin.pull = Pull.UP

        self.mcp.interrupt_enable = 0xFFFF  # Enable Interrupts in all pins
        self.mcp.interrupt_configuration = 0x0000  # interrupt on any change
        self.mcp.io_control = 0x44  # Interrupt as open drain and mirrored
        self.mcp.clear_ints()  # Interrupts need to be cleared initially
        self.bus = smbus.SMBus(1)
        
        GPIO.setmode(GPIO.BCM)
        
        interrupt = 16
        GPIO.setup(interrupt, GPIO.IN, GPIO.PUD_UP)  # Set up Pi's pin as input, pull up
        
        GPIO.add_event_detect(interrupt, GPIO.FALLING, callback = self.button_press, bouncetime=200)

    def set_lcd(self, new_lcd):
        self.lcd = new_lcd
        
    def set_db(self, new_db):
        self.db = new_db

    def cleanup(self):
            GPIO.cleanup()
