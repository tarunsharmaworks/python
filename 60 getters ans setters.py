# # Getters_________________________________--
# # Getters in Python are methods that are used to access the values of an object's properties. 
# # They are used to return the value of a specific property, and are typically defined using the @property decorator. 
# # Here is an example of a simple class with a getter method:

class MyClass:
    def __init__(self, value):
        self._value = value
    @property
    def value(self):
        return self._value
# # In this example, the MyClass class has a single property, _value, which is initialized in the init method.
# # The value method is defined as a getter using the @property decorator, and is used to return the value of the _value property.

# # To use the getter, we can create an instance of the MyClass class, and then access the value property as if it were an attribute:

obj = MyClass(10)
z=obj.value
print(z)

# # Setters___________________________________
# # It is important to note that the getters do not take any parameters and we cannot set the value through getter method.
# # For that we need setter method which can be added by decorating method with @property_name.setter

# # Here is an example of a class with both getter and setter:--------------------------------------------#########

class MyClass:
    def __init__(self, value):
        self._value = value
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, new_value):
        self._value = new_value
# # We can use setter method like this:

obj = MyClass(10)
obj.value = 20
s=obj.value
print(s)
# In conclusion, getters are a convenient way to access the values of an object's properties, 
# # while keeping the internal representation of the property hidden. This can be useful for encapsulation and data validation.

class myclass1:
  def __init__(self,value):
        self.value = value

  def show(self):  
        print(f"the value is:{self.value}")   
        
  @property #getter
  def ten_value(self):
        return self.value
  @ten_value.setter #setter
  def ten_value(self,new_value):
        self.value=new_value/10
     
a=myclass1(10)
a.ten_value=50    #DO NOT HAVE SAME NAME AS IN __INIT__ FOR LOWER FXN WILL NOT WORK
print(a.ten_value)
a.show()

####################################################################
class zlass:
     def __init__(self,value):
          self.value=value
#      def show(self):
#           print(f"current value of self.value->{self.value}")    
     @property    #getter
     def multby20(self):
          return self.value
     @multby20.setter    
     def multby20(self,new_value):
          self.value= new_value*20

# Object Creation
c=zlass(5)
# Calls __init__, so self.value = 5.
# 2. Setter Call
c.multby20=5
# Calls the setter: self.value = new_value * 20
# new_value is 5, so self.value = 5 * 20 = 100
# 3. Getter Call
print(c.multby20)
# Calls the getter: return self.value
# self.value is now 100
# Output: 100

     