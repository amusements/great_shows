import urllib.request
import json
import sqlite3 as lite
import sys

response = urllib.request.urlopen('https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=2')
response = response.read().decode('utf-8')
responseJason = json.loads(response)

con = lite.connect('linda.db')

with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Dramas (UID INT, Title TEXT, Category TEXT)")

for UID in responseJason:
    cur.execute("INSERT into Dramas values(?,?,?)", [UID["UID"], UID["title"], UID["category"]])
    con.commit()

with con:
    cur.execute("SELECT COUNT(*) FROM Dramas")
    row_cont = cur.fetchall()
    print(row_cont)

