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

class TelegramGateBot:


    def __init__(self, secret, new_db):
        self.fields = "id name code expiry".split()
        self.db = new_db
        self.bot = telebot.TeleBot(secret)
        
        self.bot.register_message_handler(self.list_codes, commands=["list"])
        self.bot.register_message_handler(self.create_code, commands=["add"])
        self.bot.register_message_handler(self.expire_code, commands=["remove"])
        #open
        #hold open
        #cycle
        
    def start(self):
        self.bot.infinity_polling()

    def help(self, message):
        self.bot.reply_to(message, HELP_MESSAGE)

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
