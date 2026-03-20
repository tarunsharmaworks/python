while True:
    print("------------------------------------------------------\n CALCULATOR")
    a= float(input(" ENTER A NUMBER: "))
    b= float(input(" ENTER A NUMBER: "))
    opt_list=["add","subt","mult","div"]
    opt=input("please select an operation\n1[add]\n2[subt]\n3[mult]\n4[div]\n:>> ")
    if opt in("add1"):
        print(f"{a}+{b}={a+b}")
    elif opt in("subt2"):
        print(f"{a}-{b}={a-b}")    
    elif opt in("mult3"):
        print(f"{a}x{b}={a*b}")     
    elif opt in("div4"):
        if b== 0:
            print(f"{int(a)}/{int(b)} NOT DIVISIBLE BY ZERO")
        else:    
            print(f"{a}/{b}={a/b}")
    else:
        pass
        