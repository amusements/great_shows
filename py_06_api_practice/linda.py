StartDate = input('輸入開始時間：')
EndDate = input('輸入結束時間：')
Location = input('輸入地點：')
import re
timeRegular = re.compile(('[0-1][0-9]|2[0-3])\/[0-5][0-9]\/[0-5][0-9]')
timeMatch = timeRegular.match(StartDate,EndDate)
if timeMatch:

else:
	print ("error!")
import datetime
import urllib.request
import json
response = urllib.request.urlopen('https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=2')
response = response.read().decode('utf-8')
responseJason = json.loads(response)
for dataDict in responseJason:
	for infoDict in dataDict["showInfo"]:
		title = dataDict["title"]
		time = infoDict["time"]
		location = infoDict["location"]
		locationName = infoDict["locationName"]
		dramaDic = {"title": title, "time": time, "location": location, "locationName": locationName}
	if (time >= StartDate and time <= EndDate) or (location == Location) :
		print("Drama Title: "+title)
		print("Location: {0} ({1})".format(locationName, location))
		print("Performance time: "+time)
	else:
		print("找不到資料")
