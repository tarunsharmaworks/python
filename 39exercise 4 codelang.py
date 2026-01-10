####################################################################################################################################################################
import random
# 1. random.random() - Returns a random float between 0.0 and 1.0
# print(random.random()) #

# 2. random.randint(a, b) - Returns a random integer N such that a <= N <= b
# print(random.randint(1, 10))

# 3. random.randrange(start, stop[, step]) - Returns a randomly selected element from range(start, stop, step)#
# print(random.randrange(1, 10, 2))

# 4. random.choice(seq) - Returns a random element from a non-empty sequence
# print(random.choice(['apple', 'banana', 'cherry']))

# 5. random.choices(seq, k=3) - Returns a list of k random elements (with replacement)
# print(random.choices(['a', 'b', 'c', 'd'], k=3))

# 6. random.sample(seq, k) - Returns a list of k unique random elements (without replacement)
# print(random.sample(['a', 'b', 'c', 'd'], 3))

# 7. random.shuffle(seq) - Shuffles the sequence in place (works only for mutable sequences like lists)
# lst = [1, 2, 3, 4]
# random.shuffle(lst)
# print(lst)

# 8. random.uniform(a, b) - Returns a random float N such that a <= N <= b
# print(random.uniform(1.5, 5.5))
#####################################################################################################################################################################

x=input("ENTER A MESSAGE:")
# for i in enumerate(word):
#     print(i)
# print(word[0]) #h
# print(word[1:0]) #e,empty
# print(word[2]) #l
# print(word[3]) #L
# print(word[4]) #0
#35 secret code language
########____ENCODING______############
alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n",
          "o","p","q","r","s","t","u","v","w","x","y","z"]

words = x.split(" ")
def encode_word(word):
    nword=[]
    for word in words:
       x= word[::-1] # reverses the words
       if len(word) < 1:
           nword.append(word)#  return word
       else:
            s1="".join(random.sample(alphabet,3))
            s2="".join(random.sample(alphabet,3))
            ret=s1+word[1:]+word[0]+s2
            nword.append(ret)
    print(" ".join(nword))        
 
# word=input("Enter a word to encode:")
# print(encode_word(word))

###########_______DECODING______##########
def decode_word(word):
    nwords = []
    for word in words:
       if (len(word) >= 3):
        x = word[3:-3]
        x = x[-1] + x[:-1]
        nwords.append(x)
       else:
        nwords.append(word[::-1])
    print(" ".join(nwords))
#     word= word[::-1]
#     if len(word)<=6:
#         return ''
#     else:
#         core= word[3:-3]
#         return core 
#####################starting########################################################
code=int(input("Enter 1 for coding and 2 for decoding:"))
if code==1:
    print(encode_word(x))
else:
    print(decode_word(x))
# 
###############################################################################################################################################
