# Day 19

import pandas as pd
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bestenlist"
)
mycursor = mydb.cursor()
mycursor.execute(
    "CREATE TABLE employee (name VARCHAR(255), id INT,salary INT)")

# a.
mycursor.execute("SELECT max(salary),min(salary) FROM employee")
myresult = mycursor.fetchall()
for x in myresult:
    print(f"Max Salary : {x[0]}, Min Salary : {x[1]}")

# b.
mycursor.execute("SELECT count(id) FROM employee")
myresult = mycursor.fetchall()
for x in myresult:
    print("Number of employees : ", x[0])


# c.
mycursor.execute("SELECT substring(e.name,1,3) FROM employee e")
myresult = mycursor.fetchall()
for x in range(len(myresult)):
    print(myresult[x][0])
