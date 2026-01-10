import os
import random
alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n",
          "o","p","q","r","s","t","u","v","w","x","y","z",]
if(not os.path.exists("68 exercise")):
    os.mkdir("68 exercise")
# to make random txt files
# for i in range(0,30):
#     folder_name="".join(random.sample(alphabet,3))+".txt"
#     filepath=(f"68 exercise/{folder_name}")
#     with open(filepath,"w")as f:
#         pass

folder = "68 exercise"
files = os.listdir(folder)
# |
# V
# i=1
# for file in files:
#     if file.endswith(".txt"):
#         print(file)
#         os.rename(f"68 exercise/{file}",f"68 exercise/{i}.png")
#         i=i+1
for i, filename in enumerate(files, start=1):
    old_path = os.path.join(folder, filename)
    new_path = os.path.join(folder, f"{i}.txt")
    os.rename(old_path, new_path)