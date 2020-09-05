class Bank_ac:
    def __init__(self):
        self.name=input("enter name")
        self.acno=int(input("enter account bal"))
        self.ac_type=input("enter a/c type")
        self.bal=int(input("enter balance"))

    def deposit(self):
        amt=int(input("Enter deposit amt"));
        self.bal=self.bal+amt;

    def withdraw(self):
        print("amt in a/c",self.bal)
        amt=int(input("Enter withdraw amt"))
        self.bal=self.bal-amt

    def display(self):
        print("user name",self.name)
        print("amt in a/c",self.bal)
n=1
while n!=5:
    print("1.deposit \n 2.withdraw \n 3.display \n 4.exit")
    n=int(input("neer your choice"))
    if(n==5):
        break
    bc=Bank_ac()
    if n==1:
        bc.deposit()
    if n==2:
        bc.withdra()
    if n==3:
        bc.display()

    
        
