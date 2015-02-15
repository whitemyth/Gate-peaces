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

        return 0

    def display_message_method(self, message):
        print(message)
        # LCD command