# DAY 2 VIDEO 11 date 20/4/25
name= 'tarun sharma'

print(name[0]) # here name[0] is the first character of the string
print(name[1]) # here name[1] is the second character of the string
print(name[2]) # here name[2] is the third character of the string
print(name[3]) # here name[3] is the fourth character of the string
print(name[4]) # here name[4] is the fifth character of the string
print('<--USING A FOR LOOP-->')
for character in name:
    print(character) 
# here character is the variable which takes the value of each character in the string name one by one
print("-----------------------------------------------------------------------")
# DAY 2 VIDEO 12 date 20/4/25
# Strings Slicing and Operations on Strings 
# for slicing string we use [] brackets
# len() function is used to find the length of the string
#      1234567890123
name= 'tarun_sharma'
namelen=len(name)
print(namelen)

print(name[0:7])#slicing the string from 0 that is the start
print(name[:5])  # python auto puts zero if the space is left empty
print(name[0:-8]) # here -8 means the 8th character from the end of the string
print(name[2:6]) #slicing the string from 2 to 6 
print(name[7:0]) #slicking till the end of the string
#loop through the string
place="DANNY'S MAJESTICAL PIZZA"
for character in place:
    print(character) #here character is a varibale which prints each character of the string one by one
# Quick Quiz:
nm = "Harry"#5
print(nm[-4:-2])
print(nm[1:3])
# DAY 2 VIDEO 13 date 20/4/25
# String Methods
strings_methods=()
# STRINGS ARE IMMUTABLE IN PYTHON MEANING THEY CANNOT BE CHANGED OR MODIFIED
# STRINGS ARE INDEXED IN PYTHON MEANING THEY HAVE A FIXED POSITION
a= "Tarun"
print(len(a))
print(a.upper()) #here upper() is astring method which converts the string to upper case
print(a.lower()) #here lower() is astring method which converts the string to lower case

a= "!!!!!!!!!!!!!!-TARUN-!!!!!!!!!!!!!!"
print(a.rstrip("!")) #here rstrip() is a string method which removes the trailing characters from the RIGHT side of the string
print(a.lstrip("!")) #here lstrip() is a string method which removes the trailing characters from the LEFT side of the string
print(a.strip("!")) #here strip() is a string method which removes the trailing characters from BOTH THE SIDES of the string
print(a.replace(a ,"ARTHUR")) #here replace() is a string method which replaces the string with the given string
print(a.split("-")) #here split() is a string method which splits the string into a list using the given seperator[LIKE - IN THIS CASE]
print(a.capitalize()) #here capitalize() is a string method which capitalizes the ONLY first character of the 
#string and the rest are turns into lower case if they are capatilised.
print(len(a))
print(len(a.center(50)))
print(a.center(50)) # here centre() is a string method which centres the string as per the given length
print("Number of \"!\" present in \"a\" is",a.count("!"))
#here count() is a string method which counts the number of times the given character is present in the string
print(a.endswith("!"))
#here endswith() is a string method which checks if the string ends with the given character 
#and returns True or False[IN BOOLEAN DATA TYPE]
print(a.endswith("-",4,15))# here i can slice strings by giving numercial pos. to see if it ends with any char.

print(a.find("TARUN"))#The find() method searches for ONLY the first occurrence of the given value and returns the index where it is present
print(a.find("JOHN"))# IF THE FIND METHOD DOES NOT FIND THE VALUE[LIKE JOHN*NOT IN THE STRING] IT RETURNS -1
print(a.index("TARUN")) #The index() method searches for the first occurrence of the given value and returns the index where it is present.
print(a.isalnum())# here isalnum() is a string method which checks if the string is alphanumeric or not and returns True or False
#[IN BOOLEAN DATA TYPE] { for example= ABC123} AND NOT [ABC 123] ranging from [0 to 9,A to Z, a to z] 
Z="AB123"
print(Z.isalnum()) #here the output will be true
print(Z.isalpha()) #here isalpha() is a string method which checks if the string is alphabetic or not and returns True or False
#[IN BOOLEAN DATA TYPE] { for example= ABC} AND NOT [ABC 123] ranging from [A to Z, a to z]
print(Z.islower()) #here islower() is a string method which checks if the string is lower case or not and returns True or False
print(Z.isprintable()) #here isprintable() is a string method which checks if the string is printable or not and returns True or False
q="             "
print(q.isspace()) #here isspace() is a string method which checks if the WHOLE string is space or not and returns True or False
Y="Tello World"
print(Y.istitle())#The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False
print(Z.isupper()) #The isupper() method returns True if all the characters in the string are upper case, else it returns False.
d="This is a sentence and five plus five is ten."
print(d.startswith("This")) #The startswith() method returns True if the string starts with the specified value, else it returns False.
print(d.swapcase()) #The swapcase() method returns a new string with all the upper case letters converted to lower case and vice versa.
print(d.title()) #The title() method returns a new string with the first letter of each word capitalized.
print("-----------------------------------------------------------------------")