# day 3 video 14 date 20/4/25
 #if else
# CONDITIONAL OPERATORS
# == is equal to
# < is less than
# > is greater than
# <= is less than or equal to
# >= is greater than or equal to
# != is not equal to
Q=15 # Q=int(input("Is the sum of two rational numbers rational? i.e,for two rational number like \n10+5 the answers is:"))
if(Q==15):
    print("YOU WIN 100 MILLION DOLLA DOLLA")
else:
    print("self destruct mechanism will be active in 5 seconds, please leave the area")
# here if the condition is true then the first statement is executed and if the condition is false then the second statement is executed

n= 17  # n=int(input("enter your number(n):"))#n is a number
if(n<0):
    print("n is a negative number")
elif(n==17):
    print("n is equal to 17")
elif(n<=20):
    print("n is less than equal to 20")
else:
    print("n is a positive number")
# here if the first condition is true then the first statement is executed and 
# if the first condition is false then the second condition is checked and so on
# in nested you can use if else inside an if else
num=14#num is a number
if(num<0):
    print("num is a negative number")
elif(num>0):
    if(num>=15):
        print("num is a positive number and greater than or equal to 15")
    elif(num==15):
        print("num is equal to 15")
    else:
        print("num is a positive number and less than 15")
else:
    print("num is zero")
print("-----------------------------------------------------------------------")
# day 4 video 16   
#match case statement
# match case statement is used to match a value with a case and execute the code block of that case
#The main idea is to keep on comparing the variable with all the present patterns until it fits into one.
#it matches with the first case that is true and executes the code block of that case.
x= int(input("enter the value of x:"))
match(x):
    case 1 if x is 1:
        print("x is 1")
    case 2 if x is 2:
        print("x is 2")
    case _ if x!=42 and x==52:#default case if x is not 1 or 2 # always lecave space before " _ " e.g{ case _:
        print(x,"is not equal to 42 and is equal to 52")
    case _ if x%2==0:#if x is even
        print(x," is even")
    case _ if x==77:#if x is 77
        print(x," is a number")
    case _ if x%2!=0:#if x is odd
        print(x," is odd")
# default case(will only be matched if the above cases were not matched)
print("------------------------------------------------------------------------")