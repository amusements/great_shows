#!/usr/local/bin/python3

import datetime
import json
import urllib.request, urllib.parse, urllib.error
import sys

inputStart = input("Please enter start date for search: ")
inputEnd = input("Please enter end date for search: ")
inputLocate = input("Please enter location for search: ")
#sys.exit(inputText)

url = "https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=2"
data_str = urllib.request.urlopen(url).read().decode()
data = json.loads(data_str)

count = 0
for obj in data:
    if inputEnd >= obj["startDate"] and inputStart <= obj["endDate"]:
        for info in obj["showInfo"]:
            if inputLocate in info["location"]:
                count +=1
                print(info["time"], ', ', obj["title"], ', ', info["location"])
print("Total count:", count)
