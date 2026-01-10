class employee:
    def __init__(self):
        self.name="john"

a=employee()
print(a.name)    #all variables and methods are default public
# Access Specifiers/Modifiers

# Access specifiers or access modifiers in python programming are used to limit the 
# access of class variables and class methods outside of class while implementing the concepts 
# of inheritance.

# Let us see the each one of access specifiers in detail:

# Types of access specifiers

# Public access modifier------------------------------------------------------------

# All the variables and methods (member functions) in python are BY DEFAULT PUBLIC
# Any instance variable in a class followed by the ‘self’ keyword 
# ie. self.var_name are public accessed.
class Student:
    # constructor is defined
    def __init__(self, age, name):
        self.age = age               # public variable
        self.name = name             # public variable

obj = Student(21,"Harry")
print(obj.age)
print(obj.name)
# OUTPUT
 # 21
# Harry
print("---------------------------------------------")
# Private access modifier-----------------------------------------------------

# By definition, Private members of a class (variables or methods) are those members -
# which are only accessible inside the class. We cannot use private members outside of class.
# In Py, there is no strict concept of "private" access modifiers like in some other programming lang.
# to indicate that a variable or method should be considered private by prefixing its -
# name with a double underscore (__). This is known as a "weak internal use indicator" -
# and it is a convention only, not a strict rule.
class Student1: 
    def __init__(self, age, name): 
        self.__age = age      # An indication of private variable
        
        def __funName(self):  # An indication of private function
            self.y = 34
            print(self.y)

class Subject(Student1):
    pass

obj = Student1(21,"Harry")
obj1 = Subject

# calling by object of class Student
# print(obj.__age) -- gives error
# print(obj.__funName())-- gives error

# calling by object  of class Subject
# print(obj1.__age)
# print(obj1.__funName())
print("---------------------------------------------")
# Private members of a class cannot be accessed or inherited outside of class. 
# If we try to access or to inherit the properties of private members to child class (derived class). 
# Then it will show the error.

# Name mangling----------------------------------------

# Name mangling in Python is a technique used to protect class-private and superclass-private 
# attributes from being accidentally overwritten by subclasses. Names of class-private and superclass-
# private attributes are transformed by the addition of a single leading underscore and a double leading
#  underscore respectively.

class MyClass:
    def __init__(self):
        self._nonmangled_attribute = "I am a nonmangled attribute"
        self.__mangled_attribute = "I am a mangled attribute"
my_object = MyClass()
print(my_object._nonmangled_attribute) # Output: I am a nonmangled attribute
# print(my_object.__mangled_attribute) # Throws an AttributeError
print(my_object._MyClass__mangled_attribute) # Output: I am a mangled attribute
print("---------------------------------------------")

# Protected access modifier-------------------------------

# In object-oriented programming (OOP), the term "protected" is used to describe a member 
# (i.e., a method or attribute) of a class that is intended to be accessed only by the class itself 
# and its subclasses. In Python, the convention for indicating that a member is protected is to prefix its 
# name with a single underscore (_). For example, if a class has a method called _my_method, it is indicating 
# that the method should only be accessed by the class itself and its subclasses.

# It's important to note that the single underscore is just a naming convention, and does not actually provide 
# any protection or restrict access to the member. The syntax we follow to make any variable protected is to write 
# variable name followed by a single underscore (_) ie. _varName.


class Student:
    def __init__(self):
        self._name = "Harry"
    def _funName(self):      # protected method
        return "CodeWithHarry"
class Subject(Student):       #inherited class
    pass
obj = Student()
obj1 = Subject()
# calling by object of Student class
print(obj._name)      
print(obj._funName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName())
print("---------------------------------------------")
 