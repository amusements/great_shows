import json
import requests
import sqlite3

#Get JSON Data from api
drama_api_res = requests.get("https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=2")
drama_json = drama_api_res.json()

#Create DB and insert data
conn = sqlite3.connect("sharon.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS Dramas (UID INT, Title TEXT, Category TEXT)")

for UID in drama_json:
    c.execute("insert into Dramas values (?,?,?)", [UID["UID"], UID["title"], UID["category"]])
    conn.commit()

#Count rows of Dramas table
with conn:
    c.execute("SELECT COUNT(*) FROM Dramas")
    row_count = c.fetchall()
    print(row_count)
