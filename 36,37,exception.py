#--------------------------------------------------------------------------
#Exception handeling 25/5/25 36
# try:
#      #statements which could generate 
#      #exception
# except: exception as e  (to print error without crashing)
#       #Soloution of generated exception
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")
#####################################################
def fun1(): #37 finally cause
  try:
    num= int(input("Enter an integer:"))
  except ValueError:# retuns error if num  is not integer
    print("INVALID INPUT"
    " PLEASE ENTER AN INTEGER")
    print(fun1())
  finally:#always executed
      print("TASK COMPLETE")
fun1()
###################################################