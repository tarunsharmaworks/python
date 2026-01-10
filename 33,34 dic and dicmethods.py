# day 13 video 33 date 15/5/25
#dict are ordered set
#dic1["name"] returns elmnt in dict
#dic1.get("Name") returns elmnt in dict
#"Name" is a Key and "Tarun Sharma" is a value
dic1 = {"Name": "Tarun Sharma", "Age": 25, "city": "Delhi"}
print(dic1["Name"])  #returns the value of the key and gives error if value not present
dic1.get("Name")  #returns the value of the key and gives None error
#dic1.values() returns all the values in the dict
print(dic1.values())
# dic1.keys()returns all the keys in the dict
print(dic1.keys())
#dic1.items() returns all the key-value pairs in the dict
c=1
for key,value in dic1.items():
    print(f"{c}){key}-->{value}")
    c+=1#as counter
# print("------------------------------------------------------------------------")
# day 13 video 34 date 15/5/25    
dicmethods=()#dict metods
#dic.update() updates the dict with the key-value pairs from another dict
#if key not present then creates new key
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
info.update({'age':20})
info.update({'DOB':2001})
print(info)
#dic.clear removes all the items from the dict
#dic.pop() #removes key-value pair form given key
#dic.popitem() #removes the last key-value pair from the dict
#del dic #deletes the entire dict
#del dic["key"] #deletes the given key-value pair from the dict
#enumerate() #returns the index and value of the dict
#zip(dic1,dic2) #returns the key-value pairs of the dict
#dic.copy() #returns a shallow copy of the dict
#sorted(dic1) #returns the sorted dict
# reversed(dic1) #returns the reversed dict

# print("------------------------------------------------------------------------")