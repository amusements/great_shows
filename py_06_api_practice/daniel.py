import json
import urllib.request, urllib.parse, urllib.error
from datetime import datetime

url = 'https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=2'
data = urllib.request.urlopen(url).read().decode()
count = 0
#print(data)
try:
  js = json.loads(data)
except:
  js = None


while True:
	a = "a. 戲劇開始日期與結束日期"
	b = "b. 表演地點"
	search = "請選擇使用何種方式搜尋 (a,b): "
	print(a + "\n" + b)
	searchtype = input(search)
	autotime = "00:00:00"
	if searchtype == "a":	
		while True:
			try:
				get_st_dt = str(input("請輸入欲查詢之開始時間 (YYYY/MM/DD): "))
				dt_start = datetime.strptime(get_st_dt, '%Y/%m/%d')
				dt_start_time = "{} {}" .format(get_st_dt, autotime) 
				break
			except ValueError: 
				print ("開始時間錯誤，請重新輸入一次")

		while True: 		
			try:
				get_end_dt = str(input("請輸入欲查詢之結束時間 (YYYY/MM/DD): "))
				dt_end =  str(datetime.strptime(get_end_dt, '%Y/%m/%d'))
				dt_end_time = "{} {}" .format(get_end_dt, autotime)
				break
			except ValueError:
				print ("結束時間錯誤，請重新輸入一次")
		break
	elif searchtype == "b":
		print ("我還沒寫完啦！")
		'''
		while True:
			try:
				locat = input_location = input("請輸入欲查詢之表演地點(選填): ")
				break
			except ValueError:
				print ("地點輸入錯誤，請重新輸入一次")
		break
		'''
	else:
		print("你選了什麼鳥？ 重新輸入不然不讓你離開")





#print(dt_start_time)
#print(dt_end_time)

#print(json.dumps(js, indent=4))
for item in js:
	for value in item['showInfo']:
		if dt_start_time <= value['time'] <= dt_end_time:
			title = item['title']
			time = value['time']
			#showunit = item['showUnit']
			#time = item['showInfo'][0]['time']
			location = value['location']
			print('戲劇名稱:' ,title, '表演地點:',location, '表演時間', time)
			count +=1
else:
	print("搜尋完畢，您的結果有",count,"筆")			
