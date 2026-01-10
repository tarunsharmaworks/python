listmethods=()#here
#list methods
#list.append() had the given value at the end of the list
#list.sort() sorts the list in ascending order
#list.sort(reverse=true) sorts the list in discending order
#list.reverse() reverses the list
#list.index() returns the index of the first occurance of the list item
#list.count() returns the count of occurances of the list item
#list.insert() inserts an item at the given index for sxample list.insert(1,boy)
#list.copy() returns a copy of the list
#list.extend() This method adds an entire list or(set, tuple, dic.) to the existing list.
#list.pop this removes an item from the list
#list[no.]=[what you want] this changes the item form the given index
#LIKE-- list[1:5] = [100] # this will change the values of the list from 1 to 5 to 100

print("------------------------------------------------------------------------")
# day 6 video 25 date 24/4/25
#tuples
# Tuples are ordered collection of data items.
# They store multiple items in a single variable.
# Tuple items are separated by commas and enclosed within round brackets ().
# Tuples are unchangeable meaning we can not alter them after creation.

tup=(1,2,3,4,5,6,7,8,9,10,"england","france","germany","spain","italy")
#tuples cannot be chnaged or modified
# tup[1]=100 this would give an error

#+ve indexing
print(tup[0]) #here 1 will be printed as is the first element of the tuple
print(tup[1]) #here 2 will be printed
print(tup[2]) #here 3 will be printed

#-ve indexing (or use len(tup) if confused)
print(tup[-1])#here italy will be printed as it is the last element
print(tup[-2])#here spain will be printed as it is the second last element or   
print(tup[(len(tup))-3])#here germany will be printed as it is the third last element

#checking for item

if "france" in tup:
    print("TRUE") #here ans. will be true

#range of the index
#for example (tup[first:last:gap])
print(tup[0:10:2])# here tup will end at 10th index and print in intervals of 2
print(tup[-1:-10:-2])# here tup will start from the end  and print in the intervals of 2
#(stops at-10 that is 6) 
print(tup[::2])
print(tup[::-2]) # here prints in reverse order with gaps of 2
print(tup[-5:]) # starts form 5 form the end
print(tup[5:])

print("------------------------------------------------------------------------")
# day 6 video 26 date 24/4/25
#tuple methods
# if you want to add,remove or change tuple items,
# then first you must convert the tuple to a list.
# perform operation on that list and convert it back to tuple.
#we can add two tuples
listmethods#uses same fxnof list (use ctrl+click)
num=(0,1,2,7,4,5,6,7,4,7,7,8,8,9,9,2,2,10)
#tuple methods
#tuple.count() 
#tuple.index(element,start,end)
print(num.index(7,2,10)) # (3) here start form 0 to 10 and print the first occurance
print(num.count(8)) # here count will be 2(of 8)

#to change tuple we temporary change it into list
#never use class names as variables
temp = list(num)
temp.append("india")
num = tuple(temp)
print(num)