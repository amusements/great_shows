#!/Users/yaliyang/anaconda3/bin/python3
import re
import json
import urllib.request, urllib.parse, urllib.error
drama= urllib.request.urlopen('https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=2 ')
drama_list= drama.read().decode()
total_list=json.loads(drama_list) 

city = input("City/County:")
start= input("Start date(0000/00/00 00:00:00):")
end= input("End date(0000/00/00 00:00:00):")
theater = input("Theater:")

if len(city) ==0:
    print("You have to fill all the information needed!")
elif len(start) ==0:
    print("You have to fill all the information needed")
elif len(end) ==0:
    print("You have to fill all the information needed")
elif len(theater) ==0:
    print("You have to fill all the information needed")

for dramadict in total_list:
    for infodict in dramadict["showInfo"]:
        title = dramadict["title"]
        time = infodict["time"]
        location = infodict["location"] 
        locationName = infodict["locationName"]
        price = infodict["price"]   
#        recity = re.sub("台", "臺", str(infodict["location"]))
        if (city in infodict["location"]) and (start <= infodict["time"] <= end) and (theater in infodict["locationName"]):
                print ("Drama Title:", title)
                print ("Performance time:", time)
                print ("Theater: {0} ({1})".format(locationName, location))
                print ("Price:", price)           
        


