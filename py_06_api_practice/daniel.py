import json
import urllib.request, urllib.parse, urllib.error

url = 'https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=2'
data = urllib.request.urlopen(url).read().decode()
count = 0
#print(data)
try:
  js = json.loads(data)
except:
  js = None

#print(json.dumps(js, indent=4))
for item in js:
	for value in item['showInfo']:
		if value['time'] >= '2018/01/01 00:00:00':
			title = item['title']
			time = value['time']
			#showunit = item['showUnit']
			#time = item['showInfo'][0]['time']
			#print(time)			
			location = value['location']
			print('戲劇名稱:' ,title, '表演地點:',location, '表演時間', time)
			count +=1
print(count)
		
