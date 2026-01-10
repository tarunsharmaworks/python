print("------------------------------------------------------------------------")   
# day 5 video 20 date 22/4/25
#function
#built in functions
# max() RETURNS THE MAXIMUM VALUE FROM THE GIVEN ARGUMENTS
# min() RETURNS THE MINIMUM VALUE FROM THE GIVEN ARGUMENTS
# len() RETURNS THE LENGTH OF THE GIVEN ARGUMENTS 
# sum() RETURNS THE SUM OF THE GIVEN ARGUMENTS 
# type() RETURNS THE TYPE OF THE GIVEN ARGUMENTS
# range() RETURNS THE RANGE OF THE GIVEN ARGUMENTS
# dict() RETURNS THE DICTIONARY OF THE GIVEN ARGUMENTS
# list() RETURNS THE LIST OF THE GIVEN ARGUMENTS
# tuple() RETURNS THE TUPLE OF THE GIVEN ARGUMENTS
# set() RETURNS THE SET OF THE GIVEN ARGUMENTS

#USER DEFINED FUNCTIONS
#they are used to define a block of code which can be reused multiple times in the program
#def function_name(parameters):
#   pass
  # Code and Statements
#pass is used to define a function without any code or statements
def isgreater(a,b):#here isgreater is the function name and a,b are the parameters
    if(a>b):
       print(a,"is greater than",b)
    elif(a<b):
       print(a,"is lesser than",b)
    else:
        print("both numbers are equal", a,"=",b) 
        
a=2
b=7
c=2
isgreater(a,c)#here output will be a is equal to c           
isgreater(a,b)#here output will be a is lesser than b           
isgreater(b,c)#here output will be b is greater than c

def number(a):
    if(a>=3):
        print(a,"is greater than equal to 3")
    else:
        print(a)
a=4
number(a)    
print("------------------------------------------------------------------------")
# day 5 video 21  date 22/4/25
# FUNCTION ARGUMENTS and return argument

#default arguments 
# We can provide a default value while creating a function, and that default value would be used if no value is given.
#if one value is given then the default value will be replaced by the given value.
def average(a=4,b=6):#this is a default argument
    print("the average is()",(a+b)/2)
average(1) #here only a will be changed to 1 and b will be 6 or-
average(b=5)#here only b will be changed to 5 and a will be 4

#keyword arguments
#here we can pass the arguments in any order by using the keyword of the argument for example[average(a=1,b=2)]
def average(a=1,b=7):#this is a keyword argument
    print("the average is(key)",(a+b)/2)
average()

#required arguments
#here we have to pass the arguments in the same order as they are defined in the function
#the number of arguments passed should match with actual function definition.
def average(a,b):#this is a required argument
    print("the average is(req)",(a+b)/2)#here it is required to give values to both a and b
average(2,4)

#variable length arguments
#to pass more arguments than those defined in the actual function. This can be done using variable-length arguments.

#arbitrary arguments
#here we can pass any number of arguments to the function and they will be stored in a tuple
def name(*name):
    print("hello",name[0],name[1],name[2])
name("john","doe","jane")#here the arguments are passed in the form of a tuple


#keyword arbitrary arguments
def name(**name):
    print("hello",name["first"],name["last"])#here the arguments are passed in the form of a dictionary
name(first="John", last="Doe")


def table(number):
    for i in range(1,11):
     print(number,"X",i,"=",number*(i))
     print("----------")
table(5)   
table(2)    #simple table efficiencised