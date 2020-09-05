class String:
    def __init__(self):
        self.str=""
    def get_String(self):
        print("In get_String Function")
        self.str=input("Enter String")
    def print_String(self):
        print("In print_String Function")
        print(self.str.upper()) 
st=String()
st.get_String()
st.print_String()    

    
