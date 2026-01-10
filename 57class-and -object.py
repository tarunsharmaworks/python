# A class is a blueprint or a template for creating objects, providing initial values for state (member variables or attributes), and 
# implementations of behavior (member functions or methods). The user-defined objects are created using the class keyword
# Creating a Class:
class person:
    name="John"
    age="45"
    occupation="construction manager"
    def info(self):
        print(f"\n{self.name} is a {self.occupation} and is {self.age} years old")
# creating an object
# Object is the instance of the class used to access the properties of the class Now lets create an object of the class.
a=person()
a.info() 

b=person()
b.name="sam"
b.occupation="job1"
b.info()
#######################
# self parameter

# # The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
# It must be provided as the extra parameter inside the method definition.
class Details:
    name = "Rohan"
    age = 20

    def description(self):
        print("\nMy name is", self.name, "and I'm", self.age, "years old.")

obj1 = Details()
obj1.description()