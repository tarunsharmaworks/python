#lamda fxn
#lets you write anoymous functions
#Lambda functions are often used in situations where a small function is required for a short period of time. 
# They are commonly used as arguments to higher-order functions, such as map, filter, and reduce.

#lambda arguments: expression
#for example-  square = lambda x: x * x
isoe=lambda x:"Even" if x%2==0 else "Odd"
print(isoe(78))
# Lambda function to calculate the product of two numbers,
# with additional print statement
z=lambda x, y: print(f'{x} * {y} = {x * y}')
print(z(2,2))
#################
#can pass fxn as argument
#and also pass fxn as fxn in another fxn
#for e.g
#making a quick fxn for calculator
add = lambda x, y: x + y
sub = lambda x, y: x - y
mul = lambda x, y: x * y
div = lambda x, y: x / y if y != 0 else "Cannot divide by zero"
while True:
   fn= input("Enter operation (add, sub, mul, div) or 'quit', 'stop', '0' to exit: ")
   if fn in("quit","exit","stop","0"):
    print("calc exited")
    break
   try:
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    if fn == "add":
        print("Result:", add(x, y))
    elif fn == "sub":
        print("Result:", sub(x, y))
    elif fn == "mul":
        print("Result:", mul(x, y))
    elif fn == "div":
        print("Result:", div(x, y))
    else:
        print("Unknown operation.")
   except Exception as e:
    print("Error:", e)
