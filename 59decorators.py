# Python decorators are a powerful and versatile tool that allow you to modify the behavior of functions and methods. 
# They are a way to extend the functionality of a function or method without modifying its source code.

# A decorator is a function that takes another function as an argument and returns a new function that modifies the behavior of the original function. 
# The new function is often referred to as a "decorated" function
# The @decorator_function notation is just a shorthand for the following code
# Decorators are often used to add functionality to functions and methods, such as logging, memoization, and access control.
# @decorator_function
# def my_function():
#     pass
import time
# def greet(fx):
#   def mfx(*args, **kwargs):
#     print("Good Morning")
#     fx(*args, **kwargs)
#     print("Thanks for using this function")
#   return mfx
##time bases gm,ge,gn
def greet(fx):
   def gtfx(*args,**kwargs):
    timestamp=time.strftime("%I:%M:%S %p")
    print(timestamp)
# here time.strftime("%I:%M:%S") is used to get the current time in hours, minutes and seconds
    timeh=int(time.strftime("%I")) # here time.strftime("%I") is used to get the current hour in 12 hour format
    zone=time.strftime("%p") # here time.strftime("%p") is used to get AM AND PM
    if(timeh>1 and  timeh<12 and zone=="AM"):
        print("GOOD MORNING SIR")
    elif(timeh==12  and zone=="PM") or(timeh<5 and zone =="PM"):
        print("GOOD AFTERNOON SIR")
    elif(timeh>=5 and timeh<12 and zone=="PM"):
        print("GOOD EVENING SIR")
    else:
        print("GOOD NIGHT SIR")
    fx(*args,**kwargs)
    pass
   return gtfx  
 
@greet
def hello():
    print("hello")
hello()
# Practical use case
# One common use of decorators is to add logging to a function. For example, you could use a decorator to log the 
# arguments and return value of a function each time it is called:
#####################################################################################
import logging                                                                      #   
def log_function_call(func):                                                        # any function
    def decorated(*args, **kwargs):                                                 #
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")  #
        result = func(*args, **kwargs)                                              #
        logging.info(f"{func.__name__} returned {result}")                          #
        return result                                                               #
    return decorated                                                                #
#####################################################################################
# @log_function_call
def my_function(a, b):
    print(a+b)
my_function(4,7)