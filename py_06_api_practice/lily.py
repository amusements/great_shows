#!/Users/yaliyang/anaconda3/bin/python3
import json
import urllib.request, urllib.parse, urllib.error
drama= urllib.request.urlopen('https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=2 ')
drama_list= drama.read().decode()
total_list=json.loads(drama_list) 

start= input("Start date(0000/00/00 00:00:00):")
end= input("End date(0000/00/00 00:00:00):")
theater = input("Location:")

count=0    
for dramadict in total_list:
    for infodict in dramadict["showInfo"]:
        title = dramadict["title"]
        time = infodict["time"]
        location = infodict["location"] 
        locationName = infodict["locationName"]
        price = infodict["price"]   
#        if infodict["time"] >= "2018/01/01 00:00:00":
#            count +=1

#        print ("Drama Title:" ,title)
#        print ("Location: {0} ({1})".format(locationName, location))
#        print ("Preformance time:" ,time)
#print ("total count:" ,count)


        if (start <= infodict["time"] <= end) and (theater in infodict["locationName"]):
            print ("Drama Title:", title)
            print ("Performance time:", time)
            print ("Location: {0} ({1})".format(locationName, location))
            print ("Price:", price)        
        else:
            print ("no results")
    
    

