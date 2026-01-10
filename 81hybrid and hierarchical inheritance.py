# hirarchical
class animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("animal speak")  
class cat(animal):
    def speak(self):
        print(f"{self.name} says : MEOW~~")          
class dog(animal):
    def speak(self):
        print(f"{self.name} says : WOOF!!")          

a=dog("tommy")   
a.speak()            
b=cat("MInsk")               
b.speak()            