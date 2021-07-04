# Day 19

import pandas as pd
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="studentmanagement"
)
mycursor = mydb.cursor()


df = pd.read_excel("C:\\Users\\Ben\\Desktop\\BestEnlist\\Day 19\\student.xlsx")
cols = list(df)
names = df[cols[0]]
reg = df[cols[1]]
mails = df[cols[2]]
mycursor.execute(
    f"CREATE TABLE students ({cols[0]} VARCHAR(255), {cols[1]} VARCHAR(255),{cols[2]} VARCHAR(255))")

sql = f"INSERT INTO students ({cols[0]},{cols[1]},{cols[2]})" + \
    "VALUES (%s, %s,%s)"
for i in range(len(names)):
    val = (names[i], str(reg[i]), mails[i])
    mycursor.execute(sql, val)
mydb.commit()
