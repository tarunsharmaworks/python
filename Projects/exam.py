def NO():
    a=input("choose the input you want:\n1.str\n2.Number\n-->: ")
    if a in "1":
        n=input("Enter a string: ")
        return n
    elif a in "2":
        n=float(input("Enter a Number: "))
        return n
    else:
        pass
# rat=float(input("enter rate: "))
# qty=int(input("enter quantity: "))
# subtotal=rat*qty
# dct_amnt=subtotal*(25/100)
# total_bill=subtotal-dct_amnt
# print(subtotal)
# print(dct_amnt)
# print(total_bill)
# -------------------------------
# sal=int(input("entr salry; "))
# #bon(40%)(40*sal)/100
# #anul=12*sal+bon
# bon=(40*sal)/100
# asal=12*sal+bon
# print("bonus",bon)
# print("annual salary",asal)
# # ------------------------
# n=float(input("enter a no"))
# if n>0:
#     print(n,"is +ve")
# else:
#     print(n,"is -ve")  
# # --------------------------------------
# a1=int(input("enter age 1"))
# a2=int(input("enetr age 2"))
# if a1>a2:
#     print("age 1 is elder")
# elif a2>a1:
#     print("age 2 is elder") 
# else:
#     print("bother have same age")
# -------------------------------------
#odd or even
# n=NO()
# if n % 2==0:
#     print("e")
# else:
#     print("o")  
#_------------------------------------
# #check if it vowel or consonat
# n=NO()
# if n in"AEIOUaeiou":
#     print("vowel")
# else:
#     print("consonant")    
#_---------------------------
# input day and get their n0
# n=NO()
# if n==1:
#     print("Mon")
# elif n==2:
#     print("Tue")
# elif n==3:
#     print("Wed")
# elif n==4:
#     print("Thu")
# elif n==5:
#     print("Fri")
# elif n==6:
#     print("Sat")
# elif n==7:
#     print("sun")
#-----------------------
# n=NO()
# if n==1:
#     print("one")
# if n==2:
#     print("two")
# if n==3:
#     print("three")
# if n==4:
#     print("four")
# if n==5:
#     print("five")
# if n==6:
#     print("six")
# if n==7:
#     print("seven")
# if n==8:
#     print("eight")
# if n==9:
#     print("nine")
# if n==0:
#     print("zero")
#------------------------------------
# m1=int(input("enetr a no"))
# m2=int(input("enetr a no"))
# m3=int(input("enetr a no"))
# avg=(m1+m2+m3)/3
# if avg>=90:
#     print("a+")
# elif avg>=75:
#     print("a")
# elif avg>=50:
#     print("b")
# elif avg>=33:
#     print("c")
# else:
#     print("fa")
#_-------------------------------
# n=NO()
# if n>=10000:
#     bon=(n*45)/100
# if n>=50000:
#     bon=(n*25)/100
# if n>=25000:
#     bon=(n*10)/100
# else:
#     bon=0
# an_sal=12*n+bon
# print("bonus",bon)
# print("annual salry",an_sal)    
#---------------------------------------
# n=NO()
# if n>="A" and n<="Z":
#     print("capital")
# elif n>="a" and n <="z":
#     print("small")
# elif n ==" ":
#     print("space")
# elif n>="0"and n<="9":
#     print("digit")
# else:
#     print("special syb")        
# -----------------------------
# n=NO()
# asc=ord(n)
# if asc>=65 and asc<=90:
#     print("capital")
# elif asc>=97 and asc <=122:
#     print("small")
# elif asc ==32:
#     print("space")
# elif asc>=48 and asc<=57:
#     print("digit")
# else:
    # print("special syb") 
#_-------------------------------------
##fFACTORSSSSSS
# n=NO()
# n=int(n)
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)
# ------------------------------
# e=o=0
# for i in range(1,101):
#     if i%2==0:
#         e=e+1
#     else:
#         o=o+1
# print("odd",o)            
# print("even",e) 
# if e > o :
#     print("even more")
# elif o>e :
#     print("odd more")
# else:
#     print("both equal")                 #----------------------
# # c=0
# for i in range(256,32,-1):
#     if i%7==0 and i%9==0:
#         c=c+1
# print("counts",c)    
# x x2 x3 x4-------------------
# x=int(input("enter a no"))
# l=int(input("enetr a limit"))
# s=0        
# for i in range(1,l+1):
#     s=s+(x**i)
# print(s)  
#--------------------------
# x=int(input("enter a no"))
# l=int(input("enetr a limit"))  
# s=0
# for i in range(1,l+1):
#     s=s+(i/x**i)
#--------------------------
# x=int(input("enter a no"))
# l=int(input("enetr a limit"))  
# s=0
# for i in range(1,l+1):
#     s=s+(i*x**(i+1)/i+1)
#factorial
# n=int(NO())
# s=1
# for i in range(1,n+1):
#     s=s*i
# print(s)    
#--------------------------
#series
# n=int(NO())
# for i in range(1,n+1):
#     print(i*i,end=",")
#--------------------------
#series
# n=int(NO())
# for i in range(1,n+1):
#     print(i**3-i,end=",")
#--------------------------
#all even no from 1 to 100
# for i in range(1,101):
#     if i%2==1:
#         continue
#     print(i,end=",")
#--------------------------
#print last no divisible by 17bw s56 and 989
# for i in range (989,257,-1):
#     if i%17==0:
#         print(i)
#         break
#--------------------------
# n=int(NO())
# f=0
# for i in range(2,n):
#     if n%i==0:
#         print("np")
#         f=1
#         break
# if f==0:
#     print("p")
#--------------------------
# # # without indexed-------------------
#program ro inpur str and count no of vowels
# str=input('enter a string: ')
# v=0
# for i in str:
#     if i in"AEIOUaeiou":
#         v=v+1
# print("no of vowels:",v) 
# indexed------------------ 
# str=input('enter a string: ')
# v=0   
# for i in range(0,len(str)):
#     if str[i] in"AEIOUaeiou":
#          v=v+1
# print(v)  
#while loop---------------------
# str=input('enter a string: ')
# v=0
# i=0
# while i < len(str):
#     if str[i] in "AEIOUaeiou":
#         v=v+1
#     i=i+1
# print("vowel",v)        
#---------------------
#chech if str is palindrome
# hello
# a=input("entr str: ")
# if a==a[::-1]:
#     print(a,"is palindrome")
# else:
#     print(a,"is not palindrome")    
# # ------------------------------------
# print str in reverse
# a=input("entr str: ")
# print(a[len(a)::-1])
# ------------------------------

# n="hellossoapwe223"
# print(n+"hi")
# print(n*2)
# print("so"in n)
#--
# print("so"not in n)
# print(n.isalpha())
# print(n.isdigit())
# print(" ".isspace())
# print(n.isalnum())# no space,spec symbol
#######------
# print("abc".islower())
#####--------
# print("ABC".isupper())
##############---------
# print("Abc Cdf".istitle())
##########---------
# print("efefe2323%#(@&AVIWV )".upper())
# #---------
# print("efefe2323%#(@&AVIWV )".lower())
# #---------
# print("efef e2323%#(@&A VIWV )".title())
# #---------
# print("efefe2323%#(@&AVIWV )".capitalize())
#--------------------
# a="hello my name is tarun sharma"
# print(a.lstrip("hello my name is"))
# a="hello my name is tarun sharma"
# print(a.rstrip("sharma"))
# a="xxxxxtarun sharmaxxxxxx"
# print(a.strip("x "))
#-------------
# a="zeooo"
# print("-blue-boy-".join(a))
# print(a.count("o"))
#--------------
# print(a.find("qw"),"not found")
#----------------------
# #print(a.index("qw"))#type:ignore
# print(a.index("e"))#value error

# a="zoology"
# print(a.split("l"))#list
# print(a.partition("l"))#tuple
# a="zaology"
# print(a[1:len(a)-1:2]) 
#count digts,cpital,small etc
# n=NO()
# c=0
# for i in n:
#     if i in "AEIOUaeiou":
#         c=c+1
# print(c)      
# c=s=d=sp=sy=0
# n=NO()
# for i in n:
#     if i.isupper():
#         c=c+1
#     elif i.islower():
#         s=s+1
#     elif i.isdigit():
#         d=d+1
#     elif i.isspace():
#         sp=sp+1
#     else:
#         sy=sy+1
# print(c,s,d,sp,sy)   
# count total words in str  
# n=NO()
# c=0
# for i in n:
#     if i.isspace():
#         c=c+1
# print(c+1)        
# print(n[::-1])
#if only special sym
# n=NO()
# c=0
# for i in n:
#     if not(i.isalnum() or i.isspace()):
#         c=c+1
# print(c) 
# remvoe all space       
# n=NO()
# b=""
# for i in n:
#     if i!=" ":
#         b=b+i
# print(b)   
#case change
# n=NO()
# v=""
# for i in n:
#     if i.isupper():
#         v=v+i.lower()
#     elif i.islower():
#         v=v+i.upper()
#     else:
#         v=v+i
# print(v)     
# doube up digits      
# n=NO()
# b=""
# for i in n:
#     if i.isdigit():
#         b=b+i+i 
#     else:
#         b=b+i
# print(b) 
#----------------------
#list
#enter a list and print all even
# a=eval(input("enter a lst"))
# for i in a:
#     if i%2==0:
#         print(i,end=",")
#enter a list print reverse if list
# a=eval(input("enter a lst"))
# l=len(a)
# for i in range(l-1,-1,-1):
#     print(a[i])
# print(a[::-1])      choice  
#enter a list and print all its element
# a=eval(input("enter a lst"))
# s=0
# for i in a:
#     s=s+i
# print(s)    
# a=eval(input("enter a lst"))
# s=0
# i=0
# for i in range(0,len(a)):
#     s=s+a[i]
# print(s)    
# a=eval(input("enter a lst"))
# a=[1,2,3,4,5]
# print(len(a))
# c=0
# for i in range(0,len(a)):
#     if a[i]==i:
#         c=c+1
# print(c)
# count if one digit no or two        
# a=[1,2,11,22,33,44,55]
# o=t=0
# for i in a:
#     if i >=10 and i<=99:
#         t=t+1
#     elif i>=0 and i<=9:
#         o=o+1
# if t>o:
#     print("two")
# elif o>t:
#     print("one")
# else:
#     print("equal")      
# a=[1,2,11,22,33,44,55,43,54,4,3,43,234,434,23,4343,134545454]
# g=a[0]
# for i in range(1,len(a)):#1 bec 0 already there
#     if a[i]>g:
#         g=a[i]
# print(g)   
# print last even no     
# a=[1,4,2,7,3,7,3,8,72,8]
# for i in range(len(a)-1,-1,-1):
#     if a[i]%2==0:
#         break
# print(a[i])    
#if div by 7 then add 5 or munius 4
# a=[1,4,2,7,3,7,3,8,72,8]
# for i in range(0,len(a)):
#     if a[i]%7==0:
#         a[i]+=5
#     else:
#         a[i]-=4  
# print(a)          
# a=[1,4,2,7,3,7,3,8,72,8]
# for i in range(0,len(a)):
#     if a[i]%2==0:
#         a[i]=a[i]+i
#     else:
#         a[i]=a[i]-i    
# print(a)        
########################
a=[1,2,3]
# a.append(4)
# print(a)
#--------------
# a.extend([4,5])
# a.extend([0])
# print(a)
#---------------
# a.insert(2,7)# add item at index and shifts back the item before
# print(a)
#-----------------
# a.remove(3)#only first occur
# print(a)
#---------------
# a.pop(1)#2
# print(a)
# a.pop()#3
# print(a)
#----------------
# a.clear()
# print(a)
#-------------
# a.reverse()
# print(a)
#---------------
# a.sort(reverse=False)
# print(a)
# a.sort(reverse=True)
# print(a)
#-----------------
# print(a.count(3))
#---------------
# print(a.index(3))
#----------------
# b=a.copy()
# b[2]=4
# print(a)
# print(b)
#---------------
# b=a
# b[1]=100
# print(a)
# print(b)
#-------------
# b=[4,5,6]
# c=a+b
# print(c)
# d=a+[4,5,6]
# print(d)
#----------
# print(a*2)
# #--------------
#List slice
# a=[1,2,3,4,5,6,7,8,9]
# print(a[0::2])
# print(a[::-1])
#----------------
# tuple slicing
# a=(1,2,3,4,5,6,7,8,9)
# a= a + (10,11,12)
# print(a[0::2])
#----------------
#dict
a={"a":"ewew","b":"!BC"}
# print(a.keys())
# #----------------
# print(a.values())
#-----------
# print(a.items())# list
#---------
# print(a.get("a","hell"))
# print(a.get("2","hell"))
#_--------------
# print(a.pop("a"))
# print(a.pop("c","hell"))
#_--------------
# print(a.popitem())
#---------------
# a=dict.fromkeys(["1","2","3"],"RED")
# print(a)
#_----------------
# a={"a":"ewew","b":"!BC"}
# # a.update({"c":"123"})
# # print(a)
# # print( "a" in a)#t
# # print("ewew" in a )#false
# #---------------
# # to change value a----------
# a["a"]="yoyo"
# print(a)
# #add new value---------------
# a["d"]="too"
# print(a)
#------------
# to clear the dict
#a.clear()
#_----------------
#print all values whose key is 4 char long
a={"A":"red","beee":"Blue","ceee":"car"}
# for i in a:
#     if len(i)==4:
#         print(a[i],end=",")
#------------------
#program print pair whose key starts with capital
# for i in a:
#     if i.isupper():
#         print(i,a[i])
#---------------------
#count pair whose key=value
a={"bad":"bad","car":"car"}
# c=0
# for i in a:
#     if i==a[i]:
#         c=c+1
# print(c)        
#-----------------
#print value of all pairs whose key starts with same char sa value
# a={"bad":"boy","car":"cat"}
# for i in a:
#     if i[0]==a[i][0]:
#         print(i,a[i])
#--------------        
a={"bad":"boy23","car":"cat2"}
# for i in a:
#     if a[i][-1].isdigit():
#         print(i)
#--------------
#print length of dict withour using len
a={"bad":"boy23","car":"cat2"}
# l=0
# for i in a:
#     l=l+1
# print(l)    
#_-------------------
#put all valuein lst
a={"bad":"boy23","car":"cat2"}
# b=[]    
# for i in a:
#     b.append(a[i])
# print(b)    
#--------------------
# to input a dict
a={}
# n=int(input("enter total no of pairs"))
# for i in range(n):
#     key=input("enter key")
#     value=input("enter value")
#     a[key]=value
# print(a)    
###################


# a="Hello my name is &*^76"
# print(a.iscapitalize())
#Traceback (most recent call last):
#   File "c:\Users\Yuvraj\Desktop\New folder\Projects\exam.py", line 608, in <module>
#     print(a.iscapitalize())
#           ^^^^^^^^^^^^^^
# AttributeError: 'str' object has no attribute 'iscapitalize'. Did you mean: 'capitalize'?
a={1:"mon",2:"tue",3:"wed",4:"thu",5:"thu",6:"fri",7:"sat",8:"sun"}
for i in range(0,len(a)):
    if i:
        print(a[i])