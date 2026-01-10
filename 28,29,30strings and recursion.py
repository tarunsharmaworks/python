# day 8 video 28 date 24/4/25
#f strings 

name="john"
age=20
letter=f"hello my name is {name} and i am {age} years old"
print(letter)
#USE f to add variables between strings
#inside  -->  {}
price = 49.09999
txt = f"For only {price:.2f} dollars!"#here the value wil be till 2 decimal points price:.1-9f

print("------------------------------------------------------------------------")
# day 9 video 29 date 2/5/25
#doc strings

def adddiv(n):
    """ no. n is checked if even or odd then if even no. then
10 is added to n and divided 5.

if n is an odd no then 50 is added to n  and it is divided by 3

"""
    if n%2==0:
        return(f"{n} is an even no.\n{(n+10)/5:.3f}")
    return(print(f"{n} is an odd no.\n{(n+50)/3:.3f}"))    

print( adddiv(4))#even
print( adddiv(3))#odd
print(adddiv.__doc__)
# import this
# print(this) #ZEN OF PYTHON

# print("------------------------------------------------------------------------")
# day 10 video 30 date 13/5/25
#RECURSIONS
# i can put fxn in anothet fxn

#like factirial
#5!=5*4**2*1
#0!=1
def factorial(x):
    if(x>=1):
        return x * factorial(x-1)
    else:
        return 1
print(factorial(0))    

#fibonachi series

#f(0) = 0
# f(1) = 1
# f(2) = f(1) + f(0)

def fibser(n):
    if(n==1 or n==2):
        return 1
    else:
        return fibser(n-1) + fibser(n-2)
print(fibser(4))    
# print("------------------------------------------------------------------------")