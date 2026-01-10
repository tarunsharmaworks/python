def add(a,b):
    return a+b 

def subt(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    if b==0:
        return "NULL, ERROR: DIVISION BY ZERO"
    else:
        return a/b

a= float(input("CALCULATOR\n ENTER A NUMBER"))
b= float(input("CALCULATOR\n ENTER A NUMBER"))
print("PLEASE SELECT AN OPERATOR\n " \
"1")
