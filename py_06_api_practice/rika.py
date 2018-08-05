import json
import urllib.request, urllib.parse, urllib.error
sourceURL = "https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=2"
source = urllib.request.urlopen(sourceURL)
decodeSource = source.read().decode()
sourceJson = json.loads(decodeSource)
dramaArr = []
for objDict in sourceJson:
    for infoDict in objDict["showInfo"]:
        time = infoDict["time"]
        if (time >= "2018/01/01 00:00:00"):
            title = objDict["title"]
            location = infoDict["location"]
            locationName = infoDict["locationName"]
            dramaDic = {"title": title, "time": time, "location": location, "locationName": locationName}
            dramaArr.append(dramaDic)
            print("Drama Title: "+title)
            print("Location: {0} ({1})".format(locationName, location))
            print("Performance time: "+time)
print("Total count: {0}".format(len(dramaArr)))
