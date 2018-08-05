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
		print("Drama Title: "+title)
		print("Location: {0} ({1})".format(locationName, location))
		print("Performance time: "+time)
