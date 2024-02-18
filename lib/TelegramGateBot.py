import telebot
import configparser

HELP_MESSAGE = "TODO -- HELP MESSAGE"
CREATE_CODE_BAD_FORMAT = "Wrong format -- user code optional_expiry"
CREATE_CODE_SUCCESS_TEMPLATE = "Registering code {} for user {} with expiration date {}"
EXPIRE_CODE_PARSE_FAILURE = "Failed to expire code -- enter the user name associated with the code to expire"
EXPIRE_CODE_GENERAL_FAILURE_TEMPLATE = "Failed to expire code -- user {} may not exist"
EXPIRE_CODE_SUCCESS_TEMPLATE = "Successfully expired code for user {}"
LIST_CODE_TEMPLATE = "{}:{} ({})"
NO_CODES_FOUND_MESSAGE = "No codes found in database"
GATE_OPENING_MESSAGE = "Gate is now opening..."

class TelegramGateBot:


    def __init__(self, secret, new_db, gate_control):
        self.fields = "id name code expiry".split()
        self.db = new_db
        self.gate_control = gate_control
        self.bot = telebot.TeleBot(secret)
        
        self.bot.register_message_handler(self.list_codes, commands=["list"])
        self.bot.register_message_handler(self.create_code, commands=["add"])
        self.bot.register_message_handler(self.expire_code, commands=["remove"])
        self.bot.register_message_handler(self.open_gate, commands=["open"])
        #open
        #hold open
        #cycle
        
        command_list = telebot.types.BotCommand(command='list', description='List entries')
        command_add = telebot.types.BotCommand(command='add', description='Add new code')
        command_expire = telebot.types.BotCommand(command='remove', description='Remove user')
        command_open = telebot.types.BotCommand(command="open", description="Open gate")
        command_hold = telebot.types.BotCommand(command="hold", description="Hold gate open")
        command_cycle = telebot.types.BotCommand(command="cycle", description="Cycle gate")
        
        self.bot.set_my_commands([command_list, command_add, command_expire])
        self.bot.set_chat_menu_button(None, telebot.types.MenuButtonCommands('commands'))
        
    def start(self):
        self.bot.infinity_polling()

    def help(self, message):
        self.bot.reply_to(message, HELP_MESSAGE)
        
    def open_gate(self, message):
        print("running open_gate...")
        self.gate_control.open()
        self.bot.reply_to(message, GATE_OPENING_MESSAGE)
        
    def hold_open(self, message):
        pass
        
    def cycle_gate(self, message):
        pass

    def create_code(self, message):
        try:
            parts = message.text.split()
            command = parts[0] #discard
            user = parts[1]
            code = parts[2]
            #check that code is an integer of length 4
            _ = int(code)
            assert len(code) == 4
            #TODO -- handle expiration dates
            if len(parts) == 4:
                expiration_date = parts[3]
            else:
                expiration_date = None
        except:
            self.bot.reply_to(message, CREATE_CODE_BAD_FORMAT)
            return
        self.db.add(user, code, expiration_date)
            
        self.bot.reply_to(message, CREATE_CODE_SUCCESS_TEMPLATE.format(code, user, expiration_date))

    def expire_code(self, message):
        try:
            parts = message.text.split()
            command = parts[0]
            user = parts[1]
        except:
            self.bot.reply_to(message, EXPIRE_CODE_PARSE_FAILURE)
            return
        try:
            self.db.delete(user)
        except:
            self.bot.reply_to(message, EXPIRE_CODE_GENERAL_FAILURE_TEMPLATE.format(user))
            return
        self.bot.reply_to(message, EXPIRE_CODE_SUCCESS_TEMPLATE.format(user))

    def list_codes(self, message):
        codes = self.db.list()
        if len(codes) == 0:
            output = NO_CODES_FOUND_MESSAGE
        else:
            output = "\n".join([LIST_CODE_TEMPLATE.format(datum[0], datum[1], datum[2]) for datum in codes])
        self.bot.reply_to(message, output)
