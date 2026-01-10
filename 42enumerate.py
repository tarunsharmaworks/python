#The enumerate function is a built-in function in Python that allows you to loop over a 
# sequence (such as a list, tuple, or string) and
#  get the index and value of each element in the sequence at the same time. 
#enumnerate() 
words= ["apple", "banana", "cat", "dog", "elephant", "fish", "grape", "hat", "ice", "jungle", "kite", "lion"]
for index,words in enumerate(words):
    print(f"{index+1}){words}")