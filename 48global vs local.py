# A local variable is a variable that is defined within a function and is only accessible within that function. 
# It is created when the function is called and is destroyed when the function returns.

# a global variable is a variable that is defined outside of a function and is accessible from within any function in your code.
x = 10  # global variable


def my_function():
  global x
  x = 5  # this will change the value of the global variable x
  y = 5  # local variable
# global keyword to declare 
# that we want to modify the global variable x from within the function

my_function()
print(x)  # prints 5
try: 
 print(y)  # type: ignore this will cause an error because y is a local variable and is not accessible outside of the function
except NameError:
  raise NameError("y=VALUE not defined")