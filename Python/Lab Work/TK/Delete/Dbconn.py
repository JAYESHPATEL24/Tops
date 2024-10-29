import pymysql

mydb = pymysql.connect(host="localhost",user="root",password="")
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS BillingSys_Customer")
mydb.commit()

mydb = pymysql.connect(host="localhost",user="root",password="",database="BillingSys_Customer")
mycursor = mydb.cursor()

#----------------------------------->   CUSTOMER DETAILS TABLE
mycursor.execute("""
                  CREATE TABLE IF NOT EXISTS Customer_Details(
                  Custom_id INT PRIMARY KEY AUTO_INCREMENT,
                  Name VARCHAR(50) NOT NULL,
                  Phone_no BIGINT UNIQUE NOT NULL,
                  Bill_No INT NOT NULL UNIQUE,
                  Total_bill DECIMAL(10,2) NOT NULL                                             )
                """)

mydb.commit()