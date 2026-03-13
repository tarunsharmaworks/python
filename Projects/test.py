def count_of_a(txt):
    count=txt.lower().count("a")
    return count
def shift_1st_to_last_elmnt(txt):
    if len(txt)==0:
        return txt
    shifted_list=txt[1:]+[txt[0]]
    return shifted_list

def display():
    print(f"\n"+"="*50)
    print("MENU DRIVEN PROJECT")
    print(f""+"="*50)
    print("1. Count occurrences of 'a'")
    print("2. Shift first element to last in a list")
    print("3. Exit")
    print("="*50)
    
def main():
    while True:
        display()
        choice=input("Enter your choice [1/2/3]:")
        if choice == "1":
            txt= input("enter a string: ")
            count= count_of_a(txt)
            print(f"\nNO Of Occurance Of 'a' in ' {txt} '' is:")
        elif choice == "2":
            try:
                list_input=input("enter elements of list seperated by spaces: ").split()
                shifted=shift_1st_to_last_elmnt(list_input)
                print(f"original input{list_input}")
                print(f" shifted input{shifted}")
            except Exception as e:
                print(f"Error{e}")

        elif choice== "3":
            print("THANK YOU FOR USING THIS PROGRAM. HAVE A GOOD DAY")
            break    
if __name__=="__main__":
    main()            