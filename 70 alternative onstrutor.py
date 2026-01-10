# Class Methods as Alternative Constructors in Python 
# In object-oriented programming, the term "constructor" refers to a special 
# type of method that is automatically executed when an object is created from a class. 
# The purpose of a constructor is to initialize the object's attributes, allowing the object to be fully functional and ready to use.

# However, there are times when you may want to create an object in a different way, 
# or with different initial values, than what is provided by the default constructor. 
# This is where class methods can be used as alternative constructors.

# A class method belongs to the class rather than to an instance of the class. 
# One common use case for class methods as alternative constructors is when you 
# want to create an object from data that is stored in a different format, such as 
# a string or a dictionary. For example, consider a class named "Person" that has 
# two attributes: "name" and "age". The default constructor for the class might look like this
class employee:
    def __init__(self,name,salary):
     self.name=name
     self.salary=salary

    @classmethod
    def frmstr(cls,string):
       return  cls(string.split("*")[0],int(string.split("*")[1]))
    
data = [
    "Alice*50000",
    "Bob*60000",
    "Charlie*55000",
    "Diana*70000",]
employees = []
for i in data:
    emp = employee.frmstr(i)
    employees.append(emp)

# To check the result:
for emp in employees:
    print(emp.name, emp.salary)

