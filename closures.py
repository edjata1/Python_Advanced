# Empress Djata
# closures

# nested functions

def outerFunction(text):
    text = text

    def innerFunction():
        print(text)

    innerFunction()

outerFunction('Hello Empress')

def outerFunction2(text):
    text = text

    def innerFunction():
        print(text)

    return innerFunction

myFunction = outerFunction2('Hello Dj')

myFunction()

# end nested test ----

import logging

logging.basicConfig(filename='example.log', level=logging.INFO)
def logger(func):

    # this is the enclosing function
    def log_func(*args):
        logging.info('Running "{}" with arguments {}'.format(func.__name__,args))
        print(func(*args))

    # Necessary for closure to
    # work (returning WITHOUT parenthesis)
    # closure
    return  log_func

# two functions add(x,y) sub(x,y)
def add(x,y):
    return x + y

def sub(x,y):
    return x - y

# initial scope
add_logger = logger(add)
sub_logger = logger(sub)

# accessing outside initial scope. still has access to variables x,y
add_logger(27, 13)
add_logger(42, 16)

sub_logger(110, 65)
sub_logger(63, 26)