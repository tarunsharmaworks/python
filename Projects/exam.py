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

#program ro inpur str and count no of vowels
# without indexed-------------------
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
# if a[1::]==a[5::-1]:
#     print(a,"is palindrome")
# else:
#     print(a,"is not palindrome")    
# ------------------------------------
# print str in reverse
# a=input("entr str: ")
# print(a[len(a)::-1])
# ------------------------------
# a=input("entr str: ")
