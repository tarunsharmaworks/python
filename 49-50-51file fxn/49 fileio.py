# READING A FILE

f = open('myfile.txt', 'r')
print(f)
text = f.read()
print(text)
f.close()

# WRITING A FILE

# f = open('myfile.txt', 'a')
# f.write(' Hello, world!')
# f.close()
#####################IMPORTANT###########

# Modes in file------------------------------------#

# There are various modes in which we can open files.

# read (r): This mode opens the file for reading only and gives an error if the file does not exist.
#  This is the default mode if no mode is passed as a parameter.

# write (w): This mode opens the file for writing only and creates a new file if the file does not exist.

# append (a): This mode opens the file for appending only and creates a new file if the file does not exist.

# create (x): This mode creates a file and gives an error if the file already exists.

# text (t): Apart from these modes we also need to specify how the file must be handled. 
# t mode is used to handle text files. t refers to the text mode.
#  There is no difference between r and rt or w and wt since text mode is the default. 
# The default mode is 'r' (open for reading text, synonym of 'rt' ).

# binary (b): used to handle binary files (images, pdfs, etc).
##############
# file fxn
# f=open(filename,mode)
#f.close() to close file
# f.write() to write

# --------------------------------------------------------
# The 'with' statement
# Alternatively, you can use the with statement to automatically close the file after you are done with it.

# with open('myfile.txt', 'a') as f:
#   f.write("Hey I am inside with")
# -------------------------------------------------
###################################################################################
# read lines file methods
#-The readline() method reads a single line from the file. If we want to read multiple lines, we can use a loop.

f=open("mytext.txt","r")
i=0
while True:
  i=i+1
  line=f.readline()
  if not line:
    break

  s1=int(line.split(",")[0])
  s2=int(line.split(",")[1])
  s3=int(line.split(",")[2])
  s4=int(line.split(",")[3])
  print(f"{(s1/100)*100} %")
  print(f"{(s2/100)*100} %")
  print(f"{(s3/100)*100} %")
  print(f"{(s4/100)*100} %")
  print(line)
  ########################################

  #write line method
# The writelines() method writes a list of strings to the file.
# f=open("mytext2.txt","w")
# i=0
# lines=[f"line1","line2","line3"]
# for line in lines:
#   f.write(line+"\n")
# f.close
################################################
