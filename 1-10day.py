# day 1 video 1 to 4 completed date 19/4/25
# day1 video 5
# USE CTRL + / FOR MULTI COMMENTING
# TRIPLE QUOTE """ FOR MULTI LINE COMMENTING
print("tarun sharma")  # here tarun sharma is a string

print(17 * 82)  # 17 * 82 is an expression

print("i am a good boy \nand tarun is a good boy")
# here \n is an escape sequence WHICH MAKES THE FOLLOWING TEXT TO THE NEXT LINE

print("tarun sharma is a \"good boy and a chill guy\"")
# here \" is an escape sequence which makes the  text to be in double quotes"

print("tarun sharma", 88, 77, 88, sep="*HAFF* *HAAF*")
# HERE SEP=" ANY CHARACTER YOUN WANT" IS USED TO SEPERATE VALUES

print("TARUN", "SHARMA", "TAKUMI", sep="--69420--", end="42069XX")
# HERE end="ANY CHARACTER YOUN WANT" IS used to add a character at the end of the print statement
print("\n-----------------------------------------------------------------------")

# DAY 2 VIDEO 6 date 20/4/25
# VARIABLES
a = 27                # here a is a integer
b = "TARUN SHAARMA"   # here b is a string
c = 33                # here c is an integer
d = None              # here d is of type NoneType
e = True              # here e is a boolean
f = 3.14              # here f is a float
g = complex(55, 6)    # here g is a complex number
print(a+c)
print(" a is of class", type(a))
print(" b is of class", type(b))
print(" c is of class", type(c))
print(" d is of class", type(d))
print(" e is of class", type(e))
print(" f is of class", type(f))
print(" g is of class", type(g))

list1 = (44, 55, (6.5, 4.5), ("apple", "tree"))
print(list1)  # here list is a SEQUENCED DATA TYPE

tuple1 = (("apple,tree,lion"), ("grass,insect,frog,snake,eagle,tiger"))
print(tuple1)  # here tuple is a SEQUENCED DATA TYPE

dict = {"NAME:TARUN SHARMA", "AGE:20", "PERCENTAGE:99.420", "CAN_VOTE=TRUE"}
print(dict)  # here IS A dict
print("\n---------------------------BASIC-CALCULATOR-------------------------")
# DAY 2 VIDEO 9 date 20/4/25
# TYPE CASTING

# explicit type casting(manual conversion)
a=15 # here a is an integer
b="45" # here b is a string

print(int(b)+a) # here b is converted to integer and added to a
# or 
c=2
e="5"
d=int(e)
print(c+d) # here e is converted to integer(d) and added to c

#  implicit type casting(automatic conversion)

a=5 # here a is an integer
z=8.99 # here z is a float

print(a+z) # here a is converted to float by python and added to z
print("-----------------------------------------------------------------------")
# DAY 2 VIDEO 10 date 20/4/25
# taking user input
#  COMMENTED TO AVOID FUTURE INCONVENIENCE
a=input("please enter your FIRST NUMBER:")# the input function takes input as string by default
b=input("please enter your SECOND NUMBER:")
print(a+b) # here a and b are joined together
print(int(a)+int(b))# here a and b are converted to integer and added