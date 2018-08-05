#!/usr/local/bin/python3

import datetime
import json
import urllib.request, urllib.parse, urllib.error

url = "https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=2"
data_str = urllib.request.urlopen(url).read().decode()
data = json.loads(data_str)

count = 0
for obj in data:
    for info in obj["showInfo"]:
        if info["time"] >= "2018/01/01 00:00:00":
            count +=1
            print(info["time"], ', ', obj["title"], ', ', info["location"])
print("Total count:", count)
