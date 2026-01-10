# day 5 video date 22 23/4/25
#lists
#Lists are ordered collection of data items.
# They store multiple items in a single variable.
# List items are separated by commas and enclosed within square brackets [].
# Lists are changeable meaning we can alter them after creation.
list3=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] #here list is a list of numbers
list3[0]=2 #here list3[0] is the first element of the list and it is changed to 2 
print(list3[0])
print(list3[1])
print(list3[2])
print(list3[3])
print(list3[len(list3)-3])#negative indexing
print(list3[15-3])#negative indexing

#in short
print(list3[-3])#negative indexing
print(list3[-10])# just count from back if list is short

def inlist3(number):
 if (number in list3):
    print("true",number,"is in list3")
 else:
    print("false",number,"is not in list3")
inlist3(78)    

namelist=["john","rohan","harry","harry","tarun"]

# note function and list name cannot be same
def nlist(name):
 if (name in namelist):
    print("true",name,"is in list")
 else:
    print("false",name,"is not in list")
nlist("harry")

list4=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] #here list is a list of numbers
#    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]

#list always starts form 0
print(list4[5:10])#here  numbers form 5 to 10 will be printed
print(list4[-10:-5])#here  numbers from 5 to 10 will be printed

# printing all element from a given index till the end
print(list4[5:])#+ve here 5 to end
print(list4[-5:])#-ve 11 to end

# printing all elements from start to a given index
print(list4[:7])#+ve here 0 to 7
print(list4[:-7])#-ve here 0 to 8

#Printing alternate values
print(list4[::5]) #here prints to the end with gaps of 10
print(list4[1:10:2])# here 1:10:2 means the numbers from 0 to 10 with a gap of 2

#accepting items(i) that are even no. in new list
even = [i for i in list4 if i % 2 == 0]
print("here are even numbers", even)

#or

no = [i for i in list4 if (i + 5 / 2 != i % 2 != 0)]
print(no)

print("------------------------------------------------------------------------")
# day 6 video 23 date 24/4/25
#lists methods
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
list5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list5.append(12)  # here 12 will be added at the end of the list
print("1",list5)
list5.sort()  # sorts the list in ascending order
print("2",list5)
list5.sort(reverse=True)  # sorts the list in discending order
print("3",list5)
list5.reverse()  # reverses the list
print("4",list5)
list5.index(5)
print("5",list5)
list5.count(5)
print("6",list5)
list5.insert(2,"hi")
print("7",list5)
list5.copy()
print("8",list5)
#concatenating two lists
list6 = [12345]
list7 = [67890]
list6.extend(list7) #
print("8",list6)
#or
print(list6+list7)#