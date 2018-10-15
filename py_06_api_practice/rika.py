import re
dateRegular = '^[0-9]{4}/[0-9]{2}/[0-9]{2}$'
def check_date_format(dateStr):
    if len(dateStr) == 0:
        return True
    if re.match(dateRegular, dateStr) == None:
        print('dateRegular')
        return False
    dateArr = dateStr.split('/')
    if dateArr[1] < '01' or dateArr[1] > '12' or dateArr[2] < '01' or dateArr[2] > '31':
        print('dateArr')
        return False
    return True

import json
import urllib.request, urllib.parse, urllib.error
def get_josn_data(startDateStr, endDateStr, locationStr):
    sourceURL = "https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=2"
    source = urllib.request.urlopen(sourceURL)
    decodeSource = source.read().decode()
    sourceJson = json.loads(decodeSource)
    dramaArr = []
    for objDict in sourceJson:
        for infoDict in objDict["showInfo"]:
            location = infoDict["location"]
            if len(locationStr) > 0 and not locationStr in location:
                continue;
            time = infoDict["time"]
            if (len(startDate) > 0 and len(startDate) == len(endDate) and (time < startDate or time > endDate)):
                continue;
            elif (len(startDate) > 0 and time < startDate):
                continue;
            elif (len(endDate) > 0 and time > endDate):
                continue;
            title = objDict["title"]
            locationName = infoDict["locationName"]
            print("Drama Title: ",title)
            print("Time: ",time)
            print("Location: {0} ({1})".format(location, locationName))
            dramaDic = {"title": title, "time": time, "location": location, "locationName": locationName}
            dramaArr.append(dramaDic)
    return dramaArr

startDate = input("Please enter start date for search(EX: 2018/01/01): ")
endDate = input("Please enter end date for search(EX: 2018/01/01): ")
location = input("Please enter location for search(EX: 國家戲劇院): ")
print('Searching..............')
errorMsg = ''
if not check_date_format(startDate) or not check_date_format(endDate):
    errorMsg = "Start date or end date has wrong format!\nDate format should be like 2018/01/01"
elif len(startDate) > 0 and len(endDate) > 0 and startDate > endDate:
    errorMsg = "Start date must be earlier than end date."

if len(errorMsg) > 0:
    print('Error: ',errorMsg)
else:
    resultArr = get_josn_data(startDate, endDate, location)
    print("Total result count: {0}".format(len(resultArr)))
