"""
User: give my important notes for viva questions about dictionaries

GitHub Copilot: **What Is a Dictionary?**
- **Definition:** `dict` is an unordered (insertion-ordered since Python 3.7), mutable mapping of keys → values.
- **Key rules:** Keys must be immutable and hashable (e.g., `str`, `int`, `tuple`), values can be any object(mutable).

**Creation & Access**
- **Literal:** `d = {'a': 1, 'b': 2}`.
- **Constructor:** `d = dict(a=1, b=2)` or `dict([('a',1), ('b',2)])`.
- **Access:** `d['a']` (raises `KeyError` if missing) vs `d.get('a')` (returns `None` or default).
- **Add/Update:** `d['c'] = 3` updates or inserts.
- **Delete:** `del d['a']` or `d.pop('a')` (returns value).

**Important Methods**
- **`keys()` :** Returns view of keys (`dict_keys`).
- **`values()` :** Returns view of values (`dict_values`).
- **`items()` :** Returns view of `(key, value)` pairs (`dict_items`).
- **`get(key, default)` :** Safe lookup without exception.
- **`setdefault(key, default)` :** Return value; insert default if key missing.
- **`update(other)` :** Merge another mapping/iterable into dict.
- **`popitem()` :** Remove and return last (LIFO) `(key, value)` pair.
- **`clear()` :** Remove all items.
- **`copy()` :** Shallow copy of the dict.

**Iteration & Comprehension**
- **Iterate keys:** `for k in d:`
- **Iterate pairs:** `for k, v in d.items():`
- **Comprehension:** `{k: v*2 for k, v in d.items()}`

**Shallow vs Deep Copy**
- **Shallow copy:** `d.copy()` duplicates mapping but not mutable nested objects (references preserved).
- **Deep copy:** `import copy; copy.deepcopy(d)` to duplicate nested structures.

**Common Patterns & Tricks**
- **Counting/frequency:** `from collections import Counter` or use `d.setdefault(x,0); d[x]+=1`.
- **Default dict:** `from collections import defaultdict` to avoid `setdefault` idioms.
- **Merge dicts (3.9+):** `d3 = d1 | d2` or `d1 |= d2` to update in-place.
- **Safe pop with default:** `d.pop('k', default_value)`.

**Complexity & Performance**
- **Average time:** O(1) average for lookup, insert, delete (hash-based).
- **Worst-case:** Hash collisions can degrade performance; very rare in practice.

**Common Pitfalls**
- **Mutable keys:** Do not use lists or other mutable objects as keys — they are unhashable.
- **Aliasing values:** Mutable values are shared across copies unless deep-copied.
- **Modifying while iterating:** Avoid changing dict size while iterating over it; iterate over `list(d.items())` if you must modify.

**Viva-Focus Questions**
- **Difference between `get()` and `[]`?**
- **When to use `defaultdict` vs `dict.setdefault()`?**
- **What is a dict view (`keys()`, `items()`)? Are they dynamic?**
- **How to merge two dicts and what happens on key conflicts?**
- **Explain shallow vs deep copy with example.**

Would you like concise one-page notes or example snippets for any of these topics?"""
a={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five'}
l=len(a)
print(l)
for i in a:
    print(i,a[i])#end=" "
print(a.keys())#list
print(a.values())#list
print(a.items())#list
print(a.get(1))
print(a.get(6,"six"))
print("deleted value:",a.pop(5))
print("deleted value:",a.pop(6,"six not exist"))
b={}
print(a.popitem())#deleted pair in tuple
'''print(b.popitem())'''#deleted pair in tuple,'popitem(): dictionary is empty'
b=dict.fromkeys([6,7],"SS")#give given key value pait with same value
print(b)
b=a.copy()
print(b)
a.update({6:"six",1:"sev"})
print(a)
print(1 in a)
print(1 not in a)
print(a)
a[4]="four"#adds key value pair at the end of the dict
print(a)
a[0]="toy"#can change value of existing pair
print(a)
print("--"*50)
# a.popitem()
# a[2]="value2"
# a.update({a:"value",b:"at"})
# a.clear
a[8]="Qwer"
a["7"]="7"
#print key whose charater =4
print(a)
for i in a:
    if len(a[i])==4:
        print(a[i])
print(a)
#print pair whose key starts with capital letter
for i in a:
    if a[i][0].isupper():
        print(i,a[i])
print(a)
#count pair whose key equal to its value
e=0
for i in a:
    if i==a[i]:
        e=e+1
        print(i,a[i])
print(f"total key equal to value: {e}") 
#print value of all pairs whose keys starts with the same harater as the value 
c={"one":"ok",'six':"seven","tit":"tat"}
print("following are value whose keys start with same char",)
for i in c:
    if i[0]==c[i][0]:
        print(c[i])  
print("--"*20)        
#print keys of pairs whose value ends with digit
c={"one":"99",'six':"7","tit":"66"}
for i in c:
    if c[i][-1].isdigit():
        print(i,c[i])
#print length of dict without len()
c={"one":"99",'six':"7","tit":"66"}
cu=0
for i in c:
    cu=cu+1    
print(f"lenght of dict c is: {cu}")  
#take dict and put all its values in dit     
c={"one":"99",'six':"7","tit":"66"}
l=[]
for i in c:
    l.append(c[i])
print(l)   
#to input in a dictionary
d={}
n=int(input("enter the total no of pairs: "))
for i in range(n):
    key=input("enter a key: ")
    value=input("enter a value: ")
    d[key]=value
print(d)    