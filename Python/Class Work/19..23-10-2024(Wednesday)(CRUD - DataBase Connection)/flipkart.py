from Database import *
import pymysql

menu = """
        press 1 for Insert Data
        press 2 for Update Data
        press 3 for Delete Data
        press 4 for View Data
        press 5 for Exit

    """
    
mydb = pymysql.connect(host = "localhost", user = "root", password="", database="Python")
mycursor = mydb.cursor()
    
while True:
    
    print(menu)
    
    choice = int(input("Enter Your Choice : "))
    
    if choice == 1:
        name = input("Enter your Name : ")
        email = input("Enter your email : ")
        password = int(input("Enter your Password : "))
        
        sql = "insert into flipkart (name, email, password) values ('%s','%s', '%s')"
        args = (name, email, password)
        
        mycursor.execute(sql%args)
        mydb.commit()
        
        print("Data Inserted Successfully !!!!!")
        
    elif choice == 2:
        id = int(input("Enter Id : "))
        name = input("Enter a Name for Update : ")
        email = input("Enter a email for update : ")
        password = int(input("Enter a  Password for update : "))
        
        sql = "update flipkart set name = '%s', email = '%s', password = '%s' where id  = '%s'"
        args = (name, email, password, id)
        
        mycursor.execute(sql%args)
        mydb.commit()
        
        print("Data Updated Successfully !!!!!")
    
    elif choice == 3:
        id = int(input("Enter Id : "))

        sql = "delete from flipkart where id = '%s'"
        args = (id)
        
        mycursor.execute(sql%args)
        mydb.commit()
        
        print("Data Deleted Successfully !!!!!")
          
    elif choice == 4:
        sql = "select * from flipkart"
        mycursor.execute(sql)
        data = mycursor.fetchall()
        print(data)
                
    elif choice == 5:
        print("Thank You... !!!")
        break
        
    else:
        print("XXXX INVALID CHOICE!!!!!")
     