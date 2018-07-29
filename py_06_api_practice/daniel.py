import json
import urllib.request, urllib.parse, urllib.error


url = 'https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=2'
uh = urllib.request.urlopen(url)
data = uh.read().decode()
added = 0

#print(data)

try:
  js = json.loads(data)
except:
  js = None

#print(json.dumps(js, indent=4))

for item in js:
	title = item['title']
	#showunit = item['showUnit']
	showInfo = item['showInfo']
	#time = item['showInfo'][0]['time']
	#print(time)
	for value in showInfo:
		time = value['time']
		location = value['location']
		if time >= '2018/01/01 00:00:00':
			print('戲劇名稱:' ,title, '表演地點:',location, '表演時間', time)
			added +=1
print(added)
		
