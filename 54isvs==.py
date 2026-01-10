# In Python, is and == are both comparison operators that can be used to check if two values are equal. 
# However, there are some important differences between the two that you should be aware of
##########IS OPERATOR#############
# The is operator compares the identity of two objects
#  This means that is will only return True if the objects being compared are the exact same object in memory
# you should use == when you want to compare the values of two objects, 
####################==OPERATOR###############
#  while the == operator compares the values of the objects
# while == will return True if the objects have the same value
# use is when you want to check if two objects are the same object in memory.
# FOR EXAMPLE
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True
print(a is b)  # False
# In this case, a and b are two separate lists that have the same values, so == returns True. 
# However, a and b are not the same object in memory, so is returns False.

# One important thing to note is that, in Python, strings and integers are immutable, which means that 
# once they are created, their value cannot be changed. This means that, for strings and integers, is and == will 
# always return the same result:
a = "hello"
b = "hello"
print(a == b)  # True
print(a is b)  # True
a = 5
b = 5
print(a == b)  # True
print(a is b)  # True
# In these cases, a and b are both pointing to the same object in memory, so is and == both return True.