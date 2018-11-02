import datetime
import json
import urllib.request, urllib.parse, urllib.error
import sys
import re

'''
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
'''

StartDate = input('輸入開始時間：')
EndDate = input('輸入結束時間：')
Location = input('輸入地點：')


TimeRegular = re.compile('[0-1][0-9]|2[0-3]\/[0-5][0-9]\/[0-5][0-9]')
TimeMatch = TimeRegular.search(StartDate)

if not TimeMatch:
	#print ("error!")
	exit("No way")

response = urllib.request.urlopen('https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=2')
response = response.read().decode('utf-8')
responseJason = json.loads(response)
for dataDict in responseJason:
	if EndDate >= obj["startDate"] and StartDate <= obj["endDate"] :
		for infoDict in dataDict["showInfo"]:
			if Location in info["location"]:
			print("Drama Title: "+title)
			print("Location: {0} ({1})".format(locationName, location))
			print("Performance time: "+time)
else:
	print("找不到資料")