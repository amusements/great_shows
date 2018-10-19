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

for info in total_list:
    UID = info ["UID"]
    title = info["title"]
    category = info["category"] 

con = lite.connect('lily.db')
 
with con:
 
    cur = con.cursor()    
   # cur.execute("CREATE TABLE DRAMA (UID INT, title TEXT, category TEXT)")   

    cur.execute("INSERT INTO DRAMA VALUES ('"+UID+"', '"+title+"', '"+category+"')")

    cur.execute("SELECT COUNT(*) FROM DRAMA")
 
    rows_count = cur.fetchall()

    print (rows_count)
