"""give my important notes for viva questions about lists

GitHub Copilot: Here are **important Python Lists notes for viva questions:**

## **What is a List?**
- Ordered collection of items (mutable - can be changed)
- Indexed starting from 0
- Can contain mixed data types
- Created using square brackets `[]`

## **List Methods (Important for Viva)**

| Method | Purpose |
|--------|---------|
| `append()` | Add single element at end |
| `extend()` | Add multiple elements from iterable |
| `insert(index, item)` | Add element at specific position |
| `remove(item)` | Remove first occurrence of item |
| `pop(index)` | Remove and return element at index (last if no index) |
| `clear()` | Remove all elements |
| `index(item)` | Return index of first occurrence |
| `count(item)` | Count occurrences of item |
| `sort()` | Sort list in-place |
| `reverse()` | Reverse list in-place |
| `copy()` | Create shallow copy |

## **Key Differences (Common Viva Q's)**

**List vs Tuple:**
- List is mutable, Tuple is immutable
- List uses `[]`, Tuple uses `()`
- Tuple is faster and uses less memory

**List vs Dictionary:**
- List: indexed by position (0, 1, 2...)
- Dictionary: indexed by keys

## **List Operations**

```python
# Slicing
lst[1:4]      # Elements from index 1 to 3
lst[::2]      # Every 2nd element
lst[::-1]     # Reverse

# Concatenation
list1 + list2

# Repetition
lst * 3       # Repeat 3 times

# Membership
item in lst   # Check if exists
```

## **Important Concepts**

1. **Aliasing vs Copying:**
   --> b = a` → Alias (both point to same list)
   --> b = a.copy()` → Copy (separate lists)

2. **List Comprehension:**
   ```python
   [x*2 for x in range(5)]  # [0, 2, 4, 6, 8]
   [x for x in lst if x > 5]  # Conditional
   ```

3. **Nested Lists:**
   - List inside list
   - Access: `lst[0][1]` → row 0, column 1

4. **Immutability Question:**
   - Strings, Tuples are immutable
   - Lists are mutable (can modify in-place)

5. **Pass by Reference:**
   - Lists are passed by reference to functions
   - Changes inside function affect original list

## **Common Viva Questions**

1. **What's the difference between `remove()` and `pop()`?**
   --> remove()` removes by value, `pop()` removes by index
   
2. **How to check if list is empty?**
   -> `if not lst:` or `if len(lst) == 0:`

3. **How to find maximum/minimum?**
   --> max(lst)`, `min(lst)`

4. **Can you add different data types in a list?**
   - Yes! `[1, 'string', 3.14, True]` is valid

5. **What is list slicing?**
   --> lst[start:end:step]` → Returns new list

6. **What happens with negative indexing?**
   --> lst[-1]` → Last element
   --> lst[-2]` → Second last element

These are the most commonly asked topics in viva exams!
"""
# n=int(input("enter a limit: "))
# e=o=0
# for i in range(1,n+1):
#     if n%i==0 and i%2==0:
#         print("even")
#         e=e+1
#     elif n%i==0 and i%2==1:
#         print("odd")   
#         o=o+1 
# print(e)  
# print(o) 

# c=z=0
# for i in range(256,30,-1):
#     if i%7==0 and i%9==0:
#         c=c+1
#     else:
#         z=z+1
# print(c) 
# print(z)
# wihtout negative in account
# while True:
#    a=eval(input("enter a list"))
#    o=t=0
#    for i in a:
#     if i >=0 and i<=9:
#         o=o+1
#     elif i>=10 and i<=99:
#         t=t+1
#    if t >o:
#     print("two digits more") 
#    elif o>t:
#     print("one digtis more")
#    else:
#     print("both equal")    
# while True:
#     a=eval(input("enter a list"))
#     c=0
#     l=len(a)
#     for i in range(0,l):
#        if i==a[i]:
#         c=c+1
# #     print(c)        
# a=eval(input("enter a list"))
# l=len(a)
# g=a[0]
# for i in range(1,l):
#     if a[i]>g:
#         g=a[i]
# print(g)        
# a=eval(input("enter a list"))
# l=len(a)
# for i in range(l-1,-1,-1):
#     if a[i]%2==0:
#         print(a[i])
#         break
# a=eval(input("enter a list"))
# l=len(a)
# for i in range(0,l):
#     if a[i]%7==0:
#         a[i]=a[i]+5
#     else:
#         a[i]=a[i]-4
# print(a)            
# liost funtions
a=[1,22,33,44,4,00,3,3,12,33,-21]
print(a)
a.append(32) #at the end of list
print(a)
a.extend([[1,2]])
print(a)
a.insert(2,69)
print(a)
a.remove(33)
print(a)
a.pop(3)#44
print(a)
a.pop()#44
# a.clear clears the lst
print(a)
a.reverse()
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
b=a.count(3)
print(b)
b=a.index(22)
print(b)
print(a)
print("shallow opy")
b=a.copy()
print(b,"copy")
b[2]=100
print(b,"copy")
print(a,"og")
print("deep copy")
b=a
a[1]=100
print(a)
print(b)
a=[1,22,33,44]
b=[1,20,33,11,111]
c=a+b
print(c)
print(a*2)
a=[1,22,33,44]
print(1 in a)
print(1 not in a)
a=[1,22,33,44,54,55,6,34,9,90,3,32,23]
print(a[1:5:2])
print(a[::2])#start to end with gap=2
print(a[::-1])