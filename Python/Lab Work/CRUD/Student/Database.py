import pymysql
from tabulate import tabulate

db = pymysql.connect(host="localhost", user="root", password="")
cursor = db.cursor()

cursor.execute("CREATE DATABASE if not exists LAB")
db.commit()

db = pymysql.connect(host="localhost", user="root", password="", database="LAB")
cursor = db.cursor()

cursor.execute("CREATE TABLE if not exists STUDENT(Roll_No INT PRIMARY KEY NOT NULL, Name VARCHAR(30), Class INT, City VARCHAR(30), Mobile_No BIGINT UNIQUE KEY, Email VARCHAR(30) UNIQUE KEY)")
db.commit()

def Viewmenu():
    print(f"{'*'*20} Menu {'*'*20}")
    menu = """
        Press 1 for Insert Data
        Press 2 for Update Data
        Press 3 for Delete Data
        Press 4 for View Data
        press 5 for Exit
    """
    print(menu)
    

def Insert():
    print(f"{'-'*12} Enter Student's Data {'-'*12}")
    roll = int(input("Roll No   : "))
    
    sql = "SELECT * FROM STUDENT WHERE Roll_No = '%s'"
    args = (roll)
    
    cursor.execute(sql%args)
    check = cursor.fetchone()
    
    if check:
        print()
        print(" \u274C"*15)
        print()
        print(f"  Roll No {roll} already exist in the database.")
        print()
        print(" \u274C"*15)
        print()
        
    else:
        name = input("Name      : ")
        std = int(input("Class     : "))
        city = input("City      : ")
        mobile = int(input("Mobile No : ")) 
        email = input("Email     : ")
        
        sql = "INSERT INTO STUDENT(Roll_No, Name, Class, City, Mobile_No, Email) VALUES('%s','%s','%s','%s','%s','%s')"
        args = (roll,name,std,city,mobile,email)
        
        cursor.execute(sql%args)
        db.commit()
        
        
        print()
        print(" \U0001F607"*15)
        print()
        print("  DATA INSERTED SUCCESSFULLY.....!!!!!!")
        print()
        print(" \U0001F607"*15)
        print()
        print()
        
def Update():
    roll = int(input("Enter the Roll No of the student you want to update : "))
    
    sql = "SELECT * FROM STUDENT WHERE ROLL_NO = '%s'"
    args = (roll)
    
    cursor.execute(sql%args)
    
    check = cursor.fetchone()

    if check:
        print()
        print(" \u274C"*15)
        print()
        print(f"  Roll No {roll} does not exist in the database.")
        print()
        print(" \u274C"*15)
        print()
    
    else:
    
        menu = """
            Which field do you want to update?
            1. Roll No
            2. Name
            3. Class
            4. City
            5. Mobile No
            6. Email
            7. Return to Menu
        """
        
        while True:
            print(menu)
        
            choice = int(input("Enter Your Field Choice : "))
            
            match choice:
                case 1:
                    field = "Roll_No"
                    new = int(input("Enter New Roll No : "))
                    
                case 2:
                    field = "Name"
                    new = input("Enter New Name : ")
                    
                case 3:
                    field = "Class"
                    new = int(input("Enter New Class : "))
                
                case 4:
                    field = "City"
                    new = input("Enter New City : ")
                
                case 5:
                    field = "Mobile_No"
                    new = int(input("Enter New Mobile No : "))
                
                case 6:
                    field = "Email"
                    new = input("Enter New Email : ")
                
                case 7:
                    print("Thank You...!!!!")
                    print()
                    break
                    
                case _:
                    print("XXXX Invalid Field Choice...!!!!")
                    print()
                    continue
            
            sql = f"UPDATE STUDENT SET {field} = '%s' WHERE ROLL_No = '%s'"
            args = (new,roll)
            
            cursor.execute(sql%args)
            db.commit()
        
        print()
        print(" 👍"*15)
        print()
        print("  DATA UPDATED SUCCESSFULLY.....!!!!!!")
        print()
        print(" 👍"*15)
        print()
    
def Delete():
    roll = int(input("Enter Student's Roll No : "))
    
    sql = "SELECT * FROM STUDENT WHERE ROLL_NO = '%s'"
    args = (roll)
    
    cursor.execute(sql%args)
    
    check = cursor.fetchone()

    if not check:
        print()
        print(" \u274C"*15)
        print()
        print(f"  Roll No {roll} does not exist in the database.")
        print()
        print(" \u274C"*15)
        print()
    
    else:
    
        sql = "DELETE FROM STUDENT WHERE Roll_No = '%s'"
        args = (roll)
        
        cursor.execute(sql % args)
        db.commit()
        
        print()
        print(" 🚮"*15)
        print()
        print("  DATA DELETED SUCCESSFULLY.....!!!!!!")
        print()
        print(" 🚮"*15)
        print()

def View_Data():
    sql = "SELECT * FROM STUDENT"
    cursor.execute(sql)
    data = cursor.fetchall()
    column = ["Roll No ","Name","Class","city","Mobile No ","Email "]
    centered_txt = [head.center(10) for head in column]
    print()
    print(f"{'-'*60} Student's Data {'-'*60}")
    print(tabulate(data, headers=centered_txt, tablefmt="fancy_grid"))
    print()