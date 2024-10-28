import pymysql

mydb = pymysql.connect(host="localhost", user="root", password="")
mycusrsor = mydb.cursor()

mycusrsor.execute("Create Database if not exists hello")
mydb.commit()

mydb = pymysql.connect(host="localhost", user="root", password="", database="hello")
mycusrsor = mydb.cursor()

mycusrsor.execute("create table if not exists hell(id int primary key, name varchar(10))")
mydb.commit()
