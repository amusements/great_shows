#!/Users/yaliyang/anaconda3/bin/python3
# -*- coding: utf-8 -*-
import sqlite3 as lite
import sys
import re
import json
import urllib.request, urllib.parse, urllib.error


drama= urllib.request.urlopen('https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=2 ')
drama_list= drama.read().decode()
total_list=json.loads(drama_list)

con = lite.connect('lily.db')
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS DRAMA (UID INT, title TEXT, category TEXT)")

for info in total_list:
    UID=info["UID"]
    title=info["title"]
    category=info["category"] 
    cur.execute("INSERT INTO DRAMA VALUES(?, ?, ?)", [info["UID"], info["title"], info["category"]]) 
    con.commit()

with con: 
    cur.execute("SELECT COUNT(*) FROM DRAMA")
    rows = cur.fetchall()
    print(rows)




