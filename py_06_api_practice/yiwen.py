#!/usr/local/bin/python3

import datetime
import json
import urllib.request, urllib.parse, urllib.error
import sys

inputStart = input("Please enter start date for search: ")
inputEnd = input("Please enter end date for search: ")
inputLocate = input("Please enter location for search: ")
inputTheater = input("Please enter theater name: ")


url = "https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=2"
data_str = urllib.request.urlopen(url).read().decode()
data = json.loads(data_str)

#count = 0
#for obj in data:
#    if inputEnd >= obj["startDate"] and inputStart <= obj["endDate"]:
#        for info in obj["showInfo"]:
#            if inputLocate in info["location"]:
#                count +=1
#                print(info["time"], ', ', obj["title"], ', ', info["location"])
#print("Total count:", count)


# Function(s)
def filtering(in_data, in_put, in_field):
    outcome = []
    for obj in in_data:
        to_add = 0
        for info in obj["showInfo"]:
            if in_put in info[in_field]:
                to_add = 1
        if to_add == 1:
            outcome.append(obj)
    return outcome

# Filters with 'AND'
if len(inputLocate) > 0:
    data = filtering(data, inputLocate, "location")

if len(inputTheater) > 0:
    data = filtering(data, inputTheater, "locationName")

for res in data:
    print("{} ~ {} \t{}".format(res["startDate"], res["endDate"], res["title"]))
