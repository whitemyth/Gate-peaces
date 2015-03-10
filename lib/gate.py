def display_message_function(message):
    print(message)


class Gate:
    def run(self):
        print('hello world')

        # This is where the main program flow will be.
        # Ideally, every part that we could isolate into a single working piece should be wrapped into classes
        # and methods that are easy to test.
        # Easy to test means it should be a function/method that receives arguments and returns values that we can
        # confirm true or false.

        display_message_function("hello from the function")
        self.display_message_method("hello from the method")

        # some objects
        lcd = Lcd()
        # lcd object
        talk = JabberBot()
        control = GateControl()
        listen = GateMonitor()
        keypad = Keypad()
        db = Database()

        lcd.awake()
        lcd.standby()
        lcd.valid_code_lcd()
        lcd.invalid_code()

        talk.listen()
        talk.notify()

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

        # send notice through jabberbot of attempt, or correct entry of code


class Lcd:
    # class for LCD modes
    # idle mode when no keys are being pressed after x amount (probably 30 seconds)
    def standby(self):
        LCD.set_color(0.0, 0.0, 0.5)
        LCD.message("time /n Enter Code")

        # what happens as soon as any key is pressed

    def awake(self):
        LCD.set_color(0.0, 0.0, 1.0)
        LCD.message([keypad_imput])

        # what happens if a valid code is entered

    def valid_code_lcd(self):
        LCD.set_color(0.0, 1.0, 0.0)
        LCD.message("Welcome 'client_name'")
        time.sleep(5.0)
        LCD.clear()

    # what happens if an invalid code is entered
    def invalid_code(self):
        LCD.set_color(1.0, 0.0, 0.0)
        LCD.message("Invalid Code")
        time.sleep(3)
        LCD.clear()


# class for jabber bot communication
class JabberBot:
    def listen(self):
        # listens for commands from admin
        pass

    def notify(self):
        # provides feedback of gate status to admin
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
        self.gate = self.GATE_IS_CLOSED

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


class Keypad:
    def press_key(self, key):
        pass
