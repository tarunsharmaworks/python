class employee:
    company_name="google"
    noemp=0
    def __init__(self,name,raise_amo):
        self.name=name
        self.raise_amo=raise_amo
        employee.noemp+=1
    def showinfo(self):
        print(f"{self.noemp}) {(self.name)} {self.raise_amo} {self.company_name}")
ep1=employee("john",45)  
ep1.raise_amo=100
ep1.company_name="apple"
ep1.showinfo()

ep2=employee("brony",477)            
ep2.raise_amo=150
ep2.showinfo()