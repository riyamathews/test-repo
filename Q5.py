class Employee:
    def __init__(self):
        self.name=input("Enter Name")
        self.des=input("Enter Designation")
        self.sal=input("Enter Salary")
    def disp(self):
        print(self.name,"\t|",self.des,"\t|",self.sal,"|")
list=[]
n=1
cnt=0;
while n!=3:
    
    print("Employee Database Operations\n1. Add\n2. Show List\n3. Exit")
    
    n=int(input("Enter Your Choice"))
    cnt=cnt+1;
    if n==1:
        
        if(cnt>2):
            print("Max 2 Emp")
            break
        else:
            list.append(Employee())
            
    elif n==2:
        print("=================================")
        print("Name\t|Designation\t|Salary\t|")
        print("=================================")
        for i in list:
            i.disp()
        print("=================================")
    elif n==3:
        break
    else:
        print("Invalid Option")
        
