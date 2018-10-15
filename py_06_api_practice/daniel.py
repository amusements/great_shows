import re
import json
import urllib.request, urllib.parse, urllib.error
from datetime import datetime



while True:
	a = "a. 戲劇開始日期與結束日期"
	b = "b. 表演地點"
	search = "請選擇使用何種方式搜尋 (a,b): "
	print(a + "\n" + b)
	searchtype = input(search)
	autotime = "00:00:00"
	get_loc = ""
	dt_start_time = ""
	dt_end_time = ""
	tw_city =("臺北市","台北市","新北市","桃園市","臺中市","臺南市","高雄市","基隆市","新竹市",
	"嘉義市","新竹縣","苗栗縣","彰化縣","南投縣","雲林縣","嘉義縣","屏東縣","宜蘭縣","花蓮縣","臺東縣","澎湖縣")
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
	if searchtype == "b":
		while True:
			get_loc = input("請輸入欲查詢之表演地點（xx 縣 / 市）: ")
			if get_loc not in tw_city:
				print ("沒這種縣市，當什麼假外國人？")
			else:
				break
		break
	else:
		print("你選了什麼鳥？ 重新輸入不然不讓你離開")

url = 'https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=2'
data = urllib.request.urlopen(url).read().decode()
count = 0
try:
  js = json.loads(data)
except:
  js = None

for item in js:
	for value in item['showInfo']:
		if dt_start_time <= value['time'] <= dt_end_time or get_loc in value['location']:
			title = item['title']
			time = value['time']
			location = value['location']
			print('戲劇名稱:' ,title, '表演地點:',location, '表演時間', time)
			count +=1

else:
	print("搜尋完畢，您的結果有",count,"筆")

