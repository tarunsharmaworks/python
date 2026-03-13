# enter salry
# calculate bonus as 40% AND calculate annual salry

try:
    print("="*50)
    sal=int(input("Enter Monthly salary: "))
    bonux= 40/100*sal
    bonus=round(bonux,2)
    annual_sal=12*sal
    print(f"Monthly Bonus= {bonus} *(Bonus= 40 % of salary)\n"+"-"*10+"rounded up to 2 decimals")
    print(f"Annual Salary= {annual_sal}")
    print(""+"="*50)
except Exception as e:
    print("="*50 +f"\nError: {e} ")  

rate=float(input("Enter rate of item: "))
quantity=int(input("Enter quantity of items: "))
subtotal=rate*quantity
discount=25/100
discounted_amnt=subtotal*discount
total_bill=subtotal-discounted_amnt
print(f"Amount before discount: {subtotal}")
print(f"Amount after discount: {total_bill}")
print(f"Discounted Amount: {discounted_amnt}")
print("="*50)