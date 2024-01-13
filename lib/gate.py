import time
#from lib.Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
import RPi.GPIO as GPIO
#from lib.MCP23017_I2C import *
#from lib.MCP23017_I2C import MCP23017_I2C
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
    @staticmethod
    def run():
        print('hello world')

        # This is where the main program flow will be.
        # Ideally, every part that we could isolate into a single working piece should be wrapped into classes
        # and methods that are easy to test.
        # Easy to test means it should be a function/method that receives arguments and returns values that we can
        # confirm true or false.

        lcd = Lcd()
        #bot = JabberBot()
        #control = GateControl()
        #listen = GateMonitor()
        #keypad = Keypad()
        
        keypad = KeypadI2C()
        keypad.set_lcd(lcd)
        
        db = ClientDatabase()
        
        db.add("Nanuk", "0123")
        #uncoment above later

        lcd.awake()
        #lcd.standby()
        #lcd.valid_code_lcd()
        #lcd.invalid_code()

        ##keypad.listen()

        #keypad.cleanup()

        #bot.listen()
        #bot.notify()

        #control.close()
        #control.hold_open()
        #control.open()

        #listen.gate_is_closed()
        #listen.gate_is_moving()
        #listen.gate_is_open()

        #keypad.press_key('1')
        #keypad.press_key('2')
        #keypad.press_key('3')
        #keypad.press_key('4')
        #keypad.press_key('5')
        #keypad.press_key('6')
        #keypad.press_key('7')
        #keypad.press_key('8')
        #keypad.press_key('9')
        #keypad.press_key('0')
        #keypad.press_key('*')
        #keypad.press_key('#')

        #db.access_code()
        #db.add_code()
        #db.remove_code()
        #db.list_code()

        # class
        # method
        # calls

        # variable = Class
        # control.open()  calling a method
        
        #testing loop
        
        try:
            print("When button is pressed you'll see a message")
            sleep(20)  # You could run your main while loop here.
            print("Time's up. Finished!")
        finally:
            GPIO.cleanup()

        return 0

    @staticmethod
    def display_message_method(message):
        print(message)
        # LCD command

        # logging in the bot
        # change bot "online" status every 10 min to avoid logout
        # get the status of the gate
        # listen for change in status from gate
        # initialize the keypad reader
        # show this message on the display  "time(hh.mm) /n enter access code
        # enter a loop
        # check if there is a new message from jabber
        # check if someone pressed a key, or entered a full code
        # verify code if entered
        # show LCD message "welcome(name)" / " Invalid Code"

        # send notice through jabber bot of attempt, or correct entry of code


class Lcd:
    def __init__(self, n_cols=16, n_rows=2):
        i2c = busio.I2C(board.SCL, board.SDA)
        self.n_cols = n_cols
        self.n_rows = n_rows
        self.lcd = character_lcd.Character_LCD_RGB_I2C(i2c, self.n_cols, self.n_rows)
        #self.lcd.color = [100,0,0] #TODO - adjustable?
        self.default_color = (0,0,100)
        #self.lcd = Adafruit_CharLCDPlate()
        #self.lcd.begin(16, 2)
        
    def display_message(self, msg, color=None, duration=1, clear=True):
        self.lcd.clear()
        self.lcd.color = color or self.default_color
        self.lcd.message = msg
        time.sleep(duration)
        if clear:
            self.lcd.clear()

    def standby(self):
        self.display_message("Enter code.", )
        #self.lcd.backlight(self.lcd.BLUE)
        #self.lcd.message('Enter Code.')
        #time.sleep(1)

    def awake(self):
        self.display_message("Waking up...")
        #self.lcd.backlight(self.lcd.YELLOW)
        #self.lcd.message('Waking up.')
        #time.sleep(1)

    def valid_code_lcd(self, name):
        self.display_message(f"Welcome\n{name}")
        #self.lcd.backlight(self.lcd.GREEN)
        #self.lcd.message('Welcome sir.')
        #time.sleep(1)
        #self.lcd.clear()

    def invalid_code(self):
        self.display_message("Invalid code")
        #self.lcd.backlight(self.lcd.RED)
        #self.lcd.message('Invalid code.')
        #time.sleep(1)
        #self.lcd.clear()

    def display(self, message):
        self.display_message(f"Code: {message}")
        #self.lcd.clear()
        #self.lcd.message('Code: ' + message)


class JabberBot:
    def listen(self):
        pass

    def notify(self):
        pass
        
class TelegramBot:
    
    def listen(self):
        pass
        
    def notify(self):
        pass


class GateControl:
    def open(self):
        GPIO.output(27, True)
        time.sleep(0.5)
        GPIO.output(27, False)

    def hold_open(self):
        GPIO.output(27, True)

    def close(self):
        GPIO.output(27, False)
        GPIO.output(28, True)
        time.sleep(0.5)
        GPIO.output(28, False)


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

    def __init__(self):
        self.db = sqlite3.connect("accessCodes.db")
        
    def check_code(self, code):
        #check that the code is in the db, and return the associated name
        cursor = self.db.execute(
            """SELECT * FROM codes WHERE client_code=?""",
            (code, )
        )
        results = cursor.fetchall()
        if len(results) > 0:
            #success
            return results[0][0] #name
        else:
            return None

    def add(self, name, code):
        self.db.execute(
            '''INSERT INTO codes (client_name, client_code) VALUES(?,?)''', 
            (name, code)
        )
        self.db.commit()

    def delete(self, name):
        self.db.execute('''DELETE FROM codes WHERE client_name=?''', name)

    def edit(self, name, new_name, new_code, new_restriction):
        self.db.execute('''UPDATE codes SET (client_name=?, client_code=?, client_restrictions=?)
            WHERE client_name=?''', (new_name, new_code, new_restriction, name))

    def change_code(self, name, new_code):
        self.db.execute('''UPDATE codes SET (client_code=?) WHERE client_name=?''', (new_code, name))

    def list(self):
        cursor = self.db.execute('''SELECT client_name, client_code, client_restrictions FROM codes''')
        return cursor.fetchall()


# instantiate the class ClientDatabase, create an object of ClientDatabase, the object is called "client"
# client = ClientDatabase()
# client.add("Alex", 1234, "Staff")
# client.delete("Alex")
# client.edit("Alex", "Alex2", 4321, "Nobody")
# user_list = client.list()
# for row in user_list:
#     print("name: " + row[0])
#     print("code: " + row[1])
#     print("restriction: " + row[2] + "\n")

class KeypadI2C:
    r1 = 3
    r2 = 2
    r3 = 1
    r4 = 0
    c1 = 0
    c2 = 1
    c3 = 2
    
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
        if output[15] == 240:
            print("Release")
        else:
            num = self.parse(output[13])
            print(num)
            self.buffer += str(num)
            self.lcd.display_message(self.buffer, duration=0, clear=False)
            if len(self.buffer) == 4:
                db = ClientDatabase()
                print("send code")
                name = db.check_code(self.buffer)
                self.buffer = ""
                if name:
                    self.lcd.valid_code_lcd(name)
                else:
                    self.lcd.invalid_code()
                db.db.close()
                del db
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
