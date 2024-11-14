import pymysql

class Database:
    def __init__(self):
            # Connect to MySQL
        self.db = pymysql.connect(host="localhost", user="root", password="")
        self.cursor = self.db.cursor()

            # Create database if it does not exist
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS CUSTOMER_BILL")
        self.db.commit()

            # Connect to the newly created database
        self.db = pymysql.connect(host="localhost", user="root", password="", database="CUSTOMER_BILL")
        self.cursor = self.db.cursor()

            # Create BILL table
        self.create_bill_table()

            # Create ITEMS table
        self.create_items_table()

    def create_bill_table(self):
            # SQL query to create the BILL table with required fields
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS BILL (
                CUSTOMER_ID INT AUTO_INCREMENT PRIMARY KEY,
                Customer_name VARCHAR(255),
                Phone_No BIGINT,
                Bill_No INT UNIQUE,
                TOTAL_AMOUNT INT
            )
        """)
        self.db.commit()

    def create_items_table(self):
            # SQL query to create the Iteams table with required fields
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS ITEMS (
                Item_ID INT AUTO_INCREMENT PRIMARY KEY,
                Bill_No INT,
                Bath_Soap INT,
                Face_Cream INT,
                Face_Wash INT,
                Hair_Spray INT,
                Body_Lotion INT,
                Rice INT,
                Food_Oil INT,
                Daal INT,
                Wheat INT,
                Sugar INT,
                Maza INT,
                Coke INT,
                Frooti INT,
                Nimkos INT,
                Biscuits INT,
                Total_Iteams INT,
                FOREIGN KEY (Bill_No) REFERENCES BILL(Bill_No)
            )
        """)
        self.db.commit()

        # method for save all the details in database
    def database_dataentry(self, customerdata, totalamount, iteamsqty, totaliteams):
        sql = "INSERT INTO BILL(Customer_name, Phone_No, Bill_No, TOTAL_AMOUNT) VALUES('%s','%s','%s','%s')"
        args = (customerdata[0], customerdata[1], customerdata[2], totalamount)

        iteams = []
        for qty in iteamsqty.values():
            iteams.append(qty)

        self.cursor.execute(sql%args)
        self.db.commit()

        sql = "INSERT INTO ITEMS(Bill_No, Bath_Soap, Face_Cream, Face_Wash, Hair_Spray, Body_Lotion, Rice, Food_Oil, Daal, Wheat, Sugar, Maza, Coke, Frooti, Nimkos, Biscuits, Total_Iteams) VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"
        args = (customerdata[2], iteams[0], iteams[1], iteams[2], iteams[3], iteams[4], iteams[5], iteams[6], iteams[7], iteams[8], iteams[9], iteams[10], iteams[11], iteams[12], iteams[13], iteams[14], totaliteams)
        self.cursor.execute(sql%args)
        self.db.commit()


        # method if customer_data is available in database or not.
    def checkdata(self,billno):

        sql = "SELECT * FROM BILL WHERE Bill_No = '%s'"
        args = (billno)
        self.cursor.execute(sql%args)
        
        check = self.cursor.fetchone()

        return check