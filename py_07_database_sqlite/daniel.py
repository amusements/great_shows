#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
import sqlite3 as lite
import sys
import re
import json
import urllib.request, urllib.parse, urllib.error

conn = lite.connect('daniel.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE Dramas(UID TEXT, Title TEXT, Category TEXT)''')

url = 'https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=2'
data = urllib.request.urlopen(url).read().decode()
try:
  js = json.loads(data)
except:
  js = None

for item in js:
	UID = item['UID']
	Title = item['title']
	Category = item['category']
	print(UID,Title,Category)
	cur.execute('''INSERT INTO Dramas VALUES (?,?,?)''', (UID,Title,Category))
	conn.commit()

count = cur.execute('SELECT COUNT() FROM Dramas')
Dramas = cur.fetchone()[0]
print(Dramas)