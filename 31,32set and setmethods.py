# day 11 video 31 date 13/5/25
#sets
#they are unordered
# s={}#will give class dict
# print(type(s))
#to get class set use->s=set()
s={1,"tar",55,78}
for i in s:
    print(i)
# print("------------------------------------------------------------------------")
# day 12 video 32 date 14/5/25
setmethods=()#set methods
s1={1,2,2,4,5}
s2={3,4,2,2,6}
#set.union() merges two sets without repetition
s3=s1.union(s2) #here cmn elmnt not repeted
#set.update() adds new element in  existing set ["set" here is any set]
s1.update(s2) # adds elmnts of s2 to s1
print(s1)
print(s3)

s1={1,2,2,4,5}
s2={3,4,2,2,6}
#set.intersection() returns the common element in both sets
s4=s1.intersection(s2) # will give cmn elmnts in both sets
#set.intersection_update() updates the set with the intersection of two sets
s2.intersection_update(s1) # updates s2 with the cmn elmnts of s1
print(s4)
print(s2)

s1={1,2,2,4,5}
s2={3,4,2,2,6}
#set.symmetric_difference() # returns the elmnts that are not cmn in both sets
s5=s1.symmetric_difference(s2)
#set.symmnetric_difference_update() # update the set by removing the cmn elmnts in both set
s2.symmetric_difference_update(s1) # updates s2 with the cmn elmnts of s1
print(s2)
print(s5)

s1={"tar","har","pen"}
s2={"har","bem","ten"}
#set.difference() # returns the elnts that are not cmn in both sets
s6=s1.difference(s2)# returns non cmn elmnts of s1
#set.difference_update() # updates the set by removing the cmn elmnts in both sets
s2.difference_update(s1)  # return non cmn elmnts if s1
print(s6)
print(s2)

s1={"tar","har","pen"}
s2={"har","bem","ten"}
s3={"har","bem"}
#set.isdisjoint() # returns True if two elements have no elmnt in cmn
s7=s1.isdisjoint(s2) # return TRUE is no cmn elmnt
#set.issuperset() # returns True if all the elements of a particular set are present in the og set
s8=s2.issuperset(s3) # T bec. s2 has all elmnts of s3
#set.issubset() # returns true if 1 set contains all elmnts of og set
s9=s3.issubset(s2) #t bec.s3 has elmnts if s2
print(s7)
print(s8)
print(s9)

#set.add() adds elmnt to the set [preferably for one item]
#set.update() add many elmnts to the set[ for many items]
#ONLY set.remove() gives error if elmnt not present
#set.remove() removes an elmnt from the set E.G
#set.discord()removes an elmnt from the set[set/discard.(item)]
#set.pop() removes the last elmnt of the set but do not know which item is removed
set1 = {1, 2, 3, 4, 5}
print(set1)
r = set1.pop()
print(set1)
print(r)
if 5 in set1:
    print("y")
set1.clear()  #empties the set
print(set1)
del set1  # deletes the entire set