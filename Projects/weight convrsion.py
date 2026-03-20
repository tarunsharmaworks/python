#weight conversion
weight=float(input("Enter weight: "))
print("---"*20)
unit=(input("1]kgs or k or 1\n2]lbs or L or 2\nSelect your unit : ")).lower()
print("---"*20)
if unit in "kgsk1":
    weight=weight*2.205
    print(f"Your weight is {round(weight,2)} Kgs")
elif unit in "lbsl2":
    weight=weight/2.205
    print(f"Your weight is {round(weight,2)} Lbs")    
else:
    print("Invalid Unit Input")    
print("---"*20)