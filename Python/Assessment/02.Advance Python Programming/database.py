import pymysql

mydb = pymysql.connect(host="localhost", user="root", password="")
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS Python_Assessment")
mydb.commit()

mydb = pymysql.connect(host="localhost", user="root", password="", database="Python_Assessment")
mycursor = mydb.cursor()

mycursor.execute("""
CREATE TABLE IF NOT EXISTS BILL(
    Customer_ID INT PRIMARY KEY AUTO_INCREMENT, 
    Customer_Name VARCHAR(30), 
    Phone_No BIGINT UNIQUE, 
    Bill_No INT UNIQUE, 
    Items INT NOT NULL, 
    Sub_Total DECIMAL(10,2) NOT NULL, 
    Tax DECIMAL(10,2) NOT NULL, 
    Total DECIMAL(10,2) NOT NULL
)
""")

mydb.commit()



def insert_Data():
    
    sql = "INSERT INTO(Customer_ID, Customer_Name, Phone_No, Bill_No, Items, Sub_Total, Tax, Total) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s')" 
    args = ()

    mycursor.execute(sql % args)
    mydb.commit()

    
mycursor.close()
mydb.close()