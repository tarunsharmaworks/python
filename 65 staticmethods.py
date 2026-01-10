class math:
    def __init__(self,num):
        self.num=num
    def addtonum(self,n):
        self.num=self.num+n

    @staticmethod
    def add(a,b):
        return a+b
result=math.add(5,5)        
print(result,"from math.add")
a=math(5)
print(a.num)
a.addtonum(5)
print(a.num)