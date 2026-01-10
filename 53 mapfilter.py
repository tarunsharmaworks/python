# In Python, the map, filter, and reduce functions are built-in functions that allow you 
# to apply a function to a sequence of elements and return a new sequence.
# These functions are known as higher-order functions, as they take other functions as arguments.
import random
number=[1,2,3,4,5,6,7,8,9,0]
cube=lambda x:x**3
square=lambda x:x**2
################################

#____________MAP__________
# The map function applies a function to each element in a sequence and 
# returns a new sequence containing the transformed elements.

newl=list(map(cube,number))
newl2=list(map(square,number))
print(newl)
print(newl2)
###############################

#____________FILTER___________
#the filter function filters a sequence of elements based on a given predicate 
# (a function that returns a boolean value) and returns a new 
# sequence containing only the elements that meet the predicate.

def iseven_filter(x):
    return x%2==0
filtereven=list(filter(iseven_filter,number))
print(f"EVEN NUMBERS-->{filtereven}")
###############################

#_________REDUCE______________
# The reduce function is a higher-order function that 
# applies a function to a sequence and returns a single value. 

from functools import reduce#  compulsory for reduce fxn
n=[1,4,2,5]
mult= lambda x,y: x*y 
x=reduce(mult, n)
print(x)
####################################