d ={}

class A:
    def ragister(self):
        name = input("Enter your Name : ")
        roll_no = int(input("Enter Your Roll No : "))
        
        d['name'] = name
        d['roll_no'] = roll_no
        
        print("Ragistration Successfully..!!!!")
        
        
        
class B(A):
    maths = 90
    science = 95
    english = 80
    
    def aunthicate(self):
        name = input("Enter a Name : ")
        roll = int(input("Enter a Roll No : "))
        
        self.name = name
        self.roll_no = roll
        
        if d['name'] == self.name and d['roll_no'] == self.roll_no:
            
            print("**************** Marks *************")
            print(f"Maths : {self.maths}")
            print(f"Science : {self.science}")
            print(f"English : {self.english}")
            
        else:
            print("XXXXX Invalid Credintials..!!!!!")
            
            
class C(B):
    def show(self):
        if d['name'] == self.name and d['roll_no'] == self.roll_no:
            total = self.maths + self.english + self.science
            print(f"Total Marks : {total}")
            print(f"Percentage : {total/3}")
            
            
student = C()

menu = """
    press 1 for Ragister
    press 2 Exit 
    """
    
print(menu)
choice = int(input("Enter Your Choice : "))

if choice == 1:
    student.ragister()
    menu1 = """
        press 1 for Aunthicate
        press 2 for Exit
        """
    print(menu1)
    
    ch = int(input("Enter Your Choice : "))
    
    if ch == 1:
        student.aunthicate()
        student.show()
    elif ch == 2:
        print("Thank You Very much........")
    else:
        print("XXXX InValid Choice")     
    
elif choice == 2:
    print("Thank You Very much........")
else:
    print("XXXX InValid Choice")