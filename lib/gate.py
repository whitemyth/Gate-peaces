import time
from lib.Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
import RPi.GPIO as GPIO
#from MCP23017_I2C import *
from lib.MCP23017_I2C import MCP23017_I2C
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
        bot = JabberBot()
        control = GateControl()
        listen = GateMonitor()
        #keypad = Keypad()
        keypad = KeypadI2C()
        keypad.set_lcd(lcd)
        db = Database()

        lcd.awake()
        # lcd.standby()
        # lcd.valid_code_lcd()
        # lcd.invalid_code()

        keypad.listen()

        print('press enter to exit program')
        input()

        keypad.cleanup()

        return 0

        bot.listen()
        bot.notify()

        control.close()
        control.hold_open()
        control.open()

        listen.gate_is_closed()
        listen.gate_is_moving()
        listen.gate_is_open()

        keypad.press_key('1')
        keypad.press_key('2')
        keypad.press_key('3')
        keypad.press_key('4')
        keypad.press_key('5')
        keypad.press_key('6')
        keypad.press_key('7')
        keypad.press_key('8')
        keypad.press_key('9')
        keypad.press_key('0')
        keypad.press_key('*')
        keypad.press_key('#')

        db.access_code()
        db.add_code()
        db.remove_code()
        db.list_code()

        # class
        # method
        # calls

        # variable = Class
        # control.open()  calling a method

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
    def __init__(self):
        self.lcd = lcd = Adafruit_CharLCDPlate()
        lcd.begin(16, 2)

    def standby(self):
        self.lcd.backlight(self.lcd.BLUE)
        self.lcd.message('Enter Code.')
        time.sleep(1)

    def awake(self):
        self.lcd.backlight(self.lcd.YELLOW)
        self.lcd.message('Waking up.')
        time.sleep(1)

    def valid_code_lcd(self):
        self.lcd.backlight(self.lcd.GREEN)
        self.lcd.message('Welcome sir.')
        time.sleep(1)
        self.lcd.clear()

    def invalid_code(self):
        self.lcd.backlight(self.lcd.RED)
        self.lcd.message('Invalid code.')
        time.sleep(1)
        self.lcd.clear()

    def display(self, message):
        self.lcd.clear()
        self.lcd.message('Code: ' + message)


class JabberBot:
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


class Database:
    # commands to interface with database
    def access_code(self):
        # defines access code, 4 digits stored in database with name, last access, and access restrictions
        pass

    def add_code(self):
        # adds a code to the database
        pass

    def remove_code(self):
        # removes a code form the database
        pass

    def list_code(self):
        # lists all codes and users from database
        pass

class KeypadI2C:
    r1 = 3
    r2 = 2
    r3 = 1
    r4 = 0
    c1 = 0
    c2 = 1
    c3 = 2
    lcd = None
    buffer = ''

    def __init__(self):
        GPIO_CHIP_1 = GPIO_Chip(0x20, 1) #define and assign chip MCP23017_I2c (0= model, b rev2, or B+ 1= model b rev1)
        GPIO_CHIP_1.setup(self.r1, 'IN', 'A')
        GPIO_CHIP_1.setup(self.r2, 'IN', 'A')
        GPIO_CHIP_1.setup(self.r3, 'IN', 'A')
        GPIO_CHIP_1.setup(self.r4, 'IN', 'A')
        GPIO_CHIP_1.setup(self.c1, 'IN', 'B')
        GPIO_CHIP_1.setup(self.c2, 'IN', 'B')
        GPIO_CHIP_1.setup(self.c3, 'IN', 'B')

    @staticmethod
    def set_lcd(new_lcd: Lcd):
        KeypadI2C.lcd = new_lcd

    @staticmethod
    def key_pressed(channel):
        the_key = ''

        if GPIO_Chip1.input(KeypadI2C.r1) and GPIO_Chip1.input(KeypadI2C.c1):
            the_key = '1'
        elif GPIO_Chip1.input(KeypadI2C.r1) and GPIO_Chip1.input(KeypadI2C.c2):
            the_key = '2'
        elif GPIO_Chip1.input(KeypadI2C.r1) and GPIO_Chip1.input(KeypadI2C.c3):
            the_key = '3'
        elif GPIO_Chip1.input(KeypadI2C.r2) and GPIO_Chip1.input(KeypadI2C.c1):
            the_key = '4'
        elif GPIO_Chip1.input(KeypadI2C.r2) and GPIO_Chip1.input(KeypadI2C.c2):
            the_key = '5'
        elif GPIO_Chip1.input(KeypadI2C.r2) and GPIO_Chip1.input(KeypadI2C.c3):
            the_key = '6'
        elif GPIO_Chip1.input(KeypadI2C.r3) and GPIO_Chip1.input(KeypadI2C.c1):
            the_key = '7'
        elif GPIO_Chip1.input(KeypadI2C.r3) and GPIO_Chip1.input(KeypadI2C.c2):
            the_key = '8'
        elif GPIO_Chip1.input(KeypadI2C.r3) and GPIO_Chip1.input(KeypadI2C.c3):
            the_key = '9'
        elif GPIO_Chip1.input(KeypadI2C.r4) and GPIO_Chip1.input(KeypadI2C.c1):
            the_key = '*'
        elif GPIO_Chip1.input(KeypadI2C.r4) and GPIO_Chip1.input(KeypadI2C.c2):
            the_key = '0'
        elif GPIO_Chip1.input(KeypadI2C.r4) and GPIO_Chip1.input(KeypadI2C.c3):
            the_key = '#'

        print(the_key)
        if len(KeypadI2C.buffer) < 4:
            KeypadI2C.buffer += the_key

        if KeypadI2C.lcd is not None:
            KeypadI2C.lcd.display(KeypadI2C.buffer)

        if len(KeypadI2C.buffer) == 4:
            print('Key entered: ' + KeypadI2C.buffer)
            KeypadI2C.buffer = ''

        def cleanup(self):
            GPIO.cleanup()


class Keypad:
    r1 = 14
    r2 = 15
    r3 = 18
    r4 = 23
    c1 = 17
    c2 = 27
    c3 = 22
    lcd = None
    buffer = ''

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        # Set as input and pulled down - connected to 3V3 on button press.
        GPIO.setup(self.r1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Row 1
        GPIO.setup(self.r2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Row 2
        GPIO.setup(self.r3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Row 3
        GPIO.setup(self.r4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Row 4
        GPIO.setup(self.c1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Column A
        GPIO.setup(self.c2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Column B
        GPIO.setup(self.c3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Column C

    @staticmethod
    def set_lcd(new_lcd: Lcd):
        Keypad.lcd = new_lcd

    @staticmethod
    def key_pressed(channel):
        the_key = ''

        if GPIO.input(Keypad.r1) and GPIO.input(Keypad.c1):
            the_key = '1'
        elif GPIO.input(Keypad.r1) and GPIO.input(Keypad.c2):
            the_key = '2'
        elif GPIO.input(Keypad.r1) and GPIO.input(Keypad.c3):
            the_key = '3'
        elif GPIO.input(Keypad.r2) and GPIO.input(Keypad.c1):
            the_key = '4'
        elif GPIO.input(Keypad.r2) and GPIO.input(Keypad.c2):
            the_key = '5'
        elif GPIO.input(Keypad.r2) and GPIO.input(Keypad.c3):
            the_key = '6'
        elif GPIO.input(Keypad.r3) and GPIO.input(Keypad.c1):
            the_key = '7'
        elif GPIO.input(Keypad.r3) and GPIO.input(Keypad.c2):
            the_key = '8'
        elif GPIO.input(Keypad.r3) and GPIO.input(Keypad.c3):
            the_key = '9'
        elif GPIO.input(Keypad.r4) and GPIO.input(Keypad.c1):
            the_key = '*'
        elif GPIO.input(Keypad.r4) and GPIO.input(Keypad.c2):
            the_key = '0'
        elif GPIO.input(Keypad.r4) and GPIO.input(Keypad.c3):
            the_key = '#'

        print(the_key)

        if len(Keypad.buffer) < 4:
            Keypad.buffer += the_key

        if Keypad.lcd is not None:
            Keypad.lcd.display(Keypad.buffer)

        if len(Keypad.buffer) == 4:
            print('Key entered: ' + Keypad.buffer)
            Keypad.buffer = ''

    def listen(self):
        GPIO.add_event_detect(self.c1, GPIO.RISING, callback=self.key_pressed, bouncetime=300)
        GPIO.add_event_detect(self.c2, GPIO.RISING, callback=self.key_pressed, bouncetime=300)
        GPIO.add_event_detect(self.c3, GPIO.RISING, callback=self.key_pressed, bouncetime=300)

    def cleanup(self):
        GPIO.cleanup()
