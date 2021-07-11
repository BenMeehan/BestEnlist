# Day 22

# 1.
from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.request
import requests
import sqlite3
from PyPDF2 import PdfFileMerger
from PIL import Image

im = Image.open(r"C:\Users\Ben\Desktop\BestEnlist\Day 22\jpeg-home.jpg")
im.show()


# 2.

pdfs = [r'C:\Users\Ben\Desktop\BestEnlist\Day 22\file1.pdf',
        r'C:\Users\Ben\Desktop\BestEnlist\Day 22\file2.pdf']

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write(r"C:\Users\Ben\Desktop\BestEnlist\Day 22\result.pdf")
merger.close()

# 3.

db = sqlite3.connect('scrape.db')
cursor = db.cursor()

html = urlopen(
    "https://en.wikipedia.org/wiki/List_of_best-selling_video_games")
soup = BeautifulSoup(html, "html.parser")

db.execute(
    '''CREATE TABLE videogames (ID INT PRIMARY KEY NOT NULL,NAME VARCHAR(255) NOT NULL);''')
i = 1
for ana in soup.findAll('a'):
    if ana.parent.name == 'i':
        db.execute(
            "INSERT INTO videogames (ID,NAME) VALUES (?,?)", (i, ana['title']))
        i += 1

db.commit()
db.close()


# 4 .

cursor.execute("SELECT * From videogames WHERE NAME='Minecraft'")
res = cursor.fetchone()
print(res)
