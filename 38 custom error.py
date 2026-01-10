#CUSTOM ERRORS 38
#like memory error
#value error

a=((input("enter a number->")))
if a=="hello":
    print(a)
else:
    try:
        int(a)
        print(f"{a} is a valid elmnt")
    except ValueError:
        raise ValueError(f"Please enter a valid number[M.B.H]")    
    ###############################################