import re
import datetime
import urllib.request
import json

StartDate = input('輸入開始時間：')
EndDate = input('輸入結束時間：')
Location = input('輸入地點：')

TimeRegular = re.compile(('[0-1][0-9]|2[0-3])\/[0-5][0-9]\/[0-5][0-9]')
TimeMatch = TimeRegular.search(StartDate,EndDate)
if TimeMatch:
	return True
else:
	print ("error!")

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
