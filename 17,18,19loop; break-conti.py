# day 4 video 17 date 21/4/25
#for loops

#IN STRING
name="john"
for i in name:
    print(i) #here i is a variable which takes the value of each character in the string one by one
#IN LIST
list2=["john","doe","jane\n"]
for t in list2:
    print(t,end=(""))
#RANGE
for l in range(5,10,2):#here range(5,10,2) means the numbers from 5 to 9 with a gap of 2
    print(l+1,"-")#here l is a variable which takes the value of each number in the range one by one
#here range(5) means the numbers from 0 to 4 
for l in range(1,6):##here range(1,6) means the numbers from 1 to 5
    print(l)
#IMPORTANT!! to note that the range function does not include the last number in the range
print("------------------------------------------------------------------------")
# day 4 video 18 date 21/4/25
#while loops

#[ LESS EFFICIENT EMULATED DO WHILE LOOP]

# l= int(input("enter the value of l:"))#l is a number
# while(l>0): #l is a +ve number
#     l= int(input("enter the value of l:"))#l is a number
#     print(l)
# print("loop completed")

#decrementing loop
number=5 #-ve no will lead to false condition and the loop will not run
while(number>0):
    print(number)
    number=number-1 #here number is decremented by 1
else:#here else is used to execute the code block if the while loop is false
    print("loop completed")
print("------------------------------------------------------------------------")
#emulate a do while loop
#here we will use a while loop to emulate a do while loop
#the do while loop will run at least once even if the condition is false
n=1
while True:
    print(n)
    n=n+1
    if(n%10==0):# here n%50 is used to check if n is divisible by 50 or not
        break
print("------------------------------------------------------------------------")   
# day 4 video 19 date 21/4/25
#break and continue statements
# break #break statement is used to break out of the loop
# continue #continue statement is used to skip the current iteration of the loop and-
#  continue with the next iteration
i=0
for i in range(10):
    if(i==10):
     break
    print("5 X",i+1,"=",5*(i+1))

i=0
for i in range(12):
    if(i==8):
     print("SKIPPING THE 8th ITERATION")
     continue
    print("5 X",i,"=",5*(i))
# can also use else in the for/while loop
for i in range(1,11,2):
        print(i,end="-\n",sep="*")