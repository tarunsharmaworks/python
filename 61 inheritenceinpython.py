# When a class derives from another class. The child class will inherit all the public and 
# protected properties and methods from the parent class. In addition, it can have its own 
# properties and methods,this is called as inheritance.     
#it has many types of lvls[ lvl = inheritane]
print("--------------------------------------------")
# 1) single lvl
class employee:
    def __init__(self,name,id,rank,salary):
        self.name=name
        self.id=id
        self.rank=rank
        self.salary=salary
    def Epinfo(self):
        print(f"The name of Employee: {self.id} is {self.name}.\nHe has pos. of {self.rank} and earns {self.salary}")
a = employee("John Smith",478,"Technician",50000)
a.Epinfo() 
print("--------------------------------------------")
# 2)MULTI LVL
# WHEN CLASS DERIVED FROM MORE THAN ONE CLASS 
class Mother:
    mothername = "d"
    def mother(self):
        print(self.mothername)
class Father:
    fathername = "2"
 
    def father(self):
        print(self.fathername) 
class Son(Mother, Father):
    def parents(self):
        print("Father name is :", self.fathername)
        print("Mother :", self.mothername)
s1 = Son()
s1.fathername = "Daddy"
s1.mothername = "Mommy"
s1.parents() 
print("--------------------------------------------")
# 3)MULTILVL when feature if base class and derived class are inheritted in the new derived class
class Grandfather:
 
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername

class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
        Grandfather.__init__(self, grandfathername)

class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname
        Father.__init__(self, fathername, grandfathername)
 
    def print_name(self):
        print('Grandfather name :', self.grandfathername)
        print("Father name :", self.fathername)
        print("Son name :", self.sonname)
s1 = Son('Prince', 'Rampal', 'Lal mani')
s1.print_name()
print("--------------------------------------------")
# 4)HIERARCHAL LVL WHEN MULTIPLE DERIVED CLASS ARE FORMED FORM A SINGLE BASE CLASS
class Parent:
    def func1(self):
        print("This function is in parent class.")

class Child1(Parent):
    def func2(self):
        print("This function is in child 1.")
      
class Child2(Parent):
    def func3(self):
        print("This function is in child 2.")
 
object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()
print("--------------------------------------------")
# 5)HYBRD LVL WHEN A CLASS CONSISTS OF MULTIPLE CLASSES
class School:
    def func1(self):
        print("This function is in school.")
 
 
class Student1(School):#learnt from SCHOOL
    def func2(self):
        print("This function is in student 1. ")
 
 
class Student2(School):#learnt from SCHOOL
    def func3(self):
        print("This function is in student 2.")
 
 
class Student3(Student1, School):#learnt from SCHOOL AND STUDENT1
    def func4(self):
        print("This function is in student 3.")
 
object = Student3()
object.func1()
object.func2()
print("--------------------------------------------")