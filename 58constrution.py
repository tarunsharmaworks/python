#construA constructor is a special method in a class used to create and initialize an object of a class. 
# There are different types of constructors. Constructor is invoked automatically when an object of a class is created.

# A constructor is a unique function that gets called automatically when an object is created of a class. 
# The main purpose of a constructor is to initialize or assign values to the data members of that class. 
# It cannot return any value other than None.

# def __init__(self): syntax
#     print("Hello")

# Parameterized Constructor in Python

# When the constructor accepts arguments along with self, it is known as parameterized constructor.
# These arguments can be used inside the class to assign the values to the data members.

class person:
   def __init__(self,fname,lname,age,occ,place):
    print("WORKING!!")
    self.fname="john"
    self.lname="bentos"
    self.age="46"
    self.occ="cook"
    self.place="dallas"
   def info(self):
     print(f"{self.fname} {self.lname} *({self.age})*is the best {self.occ} in the whole{self.place}")
a=person("John","Bentos","46","COOK","Dallas")     
a.info()

#####Default Constructor in Python
# When the constructor doesn't accept any arguments from the object and has only one argument, self, 
# in the constructor, it is known as a Default constructor.
class details:
  def __init__(self):
   print("HEllo worlds")
a=details()   