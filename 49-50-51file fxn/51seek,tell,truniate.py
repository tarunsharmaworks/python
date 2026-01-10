f=open("mytext3.txt","r")
#The seek() function allows you to move the current position within a file to a specific point. 
# The position is specified in bytes, and you can move either forward or backward from the current position
f.seek(2) #starts from 2nd byte
print(f.read(5))
######################
# The tell() function returns the current position within the file, in bytes. 
# This can be useful for keeping track of your location within the file or for seeking to 
# a specific position relative to the current position. including bytes read and bytes written.
z=f.tell()
print(z)
############################
#the truncate(*size*) function is used to resize the file to a specified size.
# If the size is not specified, it will truncate the file to the current position.
with open("mytext4.txt","a") as f:
    f.write("hellomynameistarunsharma")
    f.truncate(10)  # restricts the file to 10 bytes