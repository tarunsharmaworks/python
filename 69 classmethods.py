class employee:
    company="apple"
    def show(self):
        print(f"the company is {self.company} and name is {self.name}")
    # if want to change class variable
    @classmethod
    def changecomp(cls,newcompany):
        cls.company=newcompany

ep1=employee()
ep1.name="humpy"      
ep1.show()       
ep1.changecomp("relist")
ep1.show()       
# What are Python Class Methods?
# A class method is a type of method that is bound to the class and not the
#  instance of the class. In other words, it operates on the class as a whole,
#  rather than on a specific instance of the class. Class methods are defined
#  using the "@classmethod" decorator, followed by a function definition. 
# The first argument of the function is always "cls," which represents the 
# class itself.