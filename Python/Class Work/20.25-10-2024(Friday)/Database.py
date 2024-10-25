import pymysql

db = pymysql.connect(host="localhost", user="root", password="")
cursor = db.cursor()

cursor.execute("CREATE DATABASE if not exists Python")
db.commit()

db = pymysql.connect(host="localhost", user="root", password="", database="Python")
cursor = db.cursor()

cursor.execute("CREATE TABLE if not exists Person(ID INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(30), Email VARCHAR(30) UNIQUE KEY, Moblie_No BIGINT UNIQUE KEY, Password VARCHAR(30))")
db.commit()
