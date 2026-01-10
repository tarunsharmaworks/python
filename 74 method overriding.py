# # class for  forsimpliity sake i will take two numbers a and b class name=
class shapes:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def ar(self):
        return(self.a * self.b)
class circle(shapes):
    def __init__(self,radius):
        self.radius=radius
        super().__init__(radius,radius)
    def ar(self):
        return 3.14 * super().ar()     
s=shapes(3,3)     
print(s.ar())
c=circle(3)
print(c.ar())

# class Shape:

#   def __init__(self, x, y):
#     self.x = x
#     self.y = y

#   def area(self):
#     return self.x * self.y


# class Circle(Shape):

#   def __init__(self, radius):
#     self.radius = radius
#     super().__init__(radius, radius)

#   def area(self):
#     return 3.14 * super().area()


# rec = Shape(3, 5)
# print(rec.area())

# c = Circle(5)
# print(c.area())
