from tabulate import tabulate
from Database import *

menu = """
        press 1 for Insert Data
        press 2 for Update Data
        press 3 for Delete Data
        press 4 for View Data
        press 5 for Exit

    """
    
mydb = pymysql.connect(host = "localhost", user = "root", password="", database="Python")
mycursor = mydb.cursor()
    

mycursor.execute("select * FROM flipkart") 
data = mycursor.fetchall()
    
# Define column names
column_names = ["ID", "Name", "Email", "Password"]
    
# Print data in table format
print(tabulate(data, headers=column_names, tablefmt="fancy_grid"))
