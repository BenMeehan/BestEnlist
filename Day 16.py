# Day 15 - MYSQL

# 1.
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bestenlist"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT VERSION()")

data = mycursor.fetchone()
print(data)

# 2.
mycursor.execute("CREATE TABLE multiple (a INT, b INT, result INT)")
sql = "INSERT INTO multiple (a,b,result) VALUES (%s, %s,%s)"
for i in range(10):
    for j in range(10):
        val = (i, j, i*j)
        mycursor.execute(sql, val)
mydb.commit()

# 3.
mycursor.execute("CREATE TABLE employee (name VARCHAR(255), id INT)")
mycursor.execute("SELECT name FROM employee")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)
