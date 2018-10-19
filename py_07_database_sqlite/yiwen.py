#!/Users/yaliyang/anaconda3/bin/python3
# -*- coding: utf-8 -*-

import sqlite3 as lite
import json
import urllib.request, urllib.parse, urllib.error

drama= urllib.request.urlopen('https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=2')
drama_list= drama.read().decode()
total_list=json.loads(drama_list)

data_rows = []
for info in total_list:
    data_rows.append((info["UID"], info["title"], info["category"]))

print("data size: ", len(data_rows))
con = lite.connect('yiwen.db')

with con:

    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS DRAMA (UID INT, title TEXT, category TEXT)")

    cur.execute("SELECT * FROM DRAMA")
    rows = cur.fetchall()

    if len(rows) != len(data_rows):
        cur.execute("DELETE FROM DRAMA")
        cur.executemany("INSERT INTO DRAMA ('UID','title', 'category') VALUES (?, ? ,?)", data_rows)
    else:
        for row in rows:
            print (row)
