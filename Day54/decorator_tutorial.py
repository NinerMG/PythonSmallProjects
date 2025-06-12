import time



def decorator_function(function):
    def wrapper_function():
        function()
    return wrapper_function()

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        #do something before
        function()
        print("test")
        # do something after
    return wrapper_function


# def say_hello():
#     time.sleep(2)
#     print("Hello")

@delay_decorator
def say_hello():
     print("Hello")

@delay_decorator
def say_bye():
    print("Bye")

@delay_decorator
def say_greeting():
    print("How are you?")

say_hello()