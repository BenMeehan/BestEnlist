# Day 18

# 1.
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="doctordb"
)
mycursor = mydb.cursor()
mycursor.execute(
    "CREATE TABLE doctors (name VARCHAR(255), id INT,patients INT)")


# 2.
print("More than 5 patients : ")
mycursor.execute("SELECT name FROM doctors WHERE patients>5")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)

# 3.
print("No Patients : ")
mycursor.execute("SELECT name FROM doctors WHERE patients=0")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)
