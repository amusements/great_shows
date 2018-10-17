import json
import urllib.request, urllib.parse, urllib.error
import sqlite3 as lite
import sys

def getDramaAPIData():
    url = "https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=2"
    request = urllib.request.urlopen(url)
    decodeRequest = request.read().decode()
    jsonData = json.loads(decodeRequest)
    return jsonData

con = lite.connect('rika.db')
with con:
    cur = con.cursor()
    # cur.execute("DROP TABLE Dramas")
    cur.execute("CREATE TABLE Dramas(UID TEXT, Title TEXT, Category TEXT)")
    dramaAPIData = getDramaAPIData()
    for objDict in dramaAPIData:
        uid = objDict["UID"]
        title = objDict["title"]
        category = objDict["category"]
        cur.execute("INSERT INTO Dramas VALUES('"+uid+"', '"+title+"', '"+category+"')")
    cur.execute("SELECT * FROM Dramas")
    rows = cur.fetchall()
    print("{0} rows in Dramas table".format(len(rows)))
