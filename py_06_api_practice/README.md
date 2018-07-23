##[Reference Website] 
https://docs.python.org/3/tutorial/datastructures.html 5.5 dictionaries, 5.6 looping
https://docs.python.org/3/library/json.html import json
https://docs.python.org/3/library/urllib.html import urllib

##Hand-in instruction 

1. Pull master branch and find the new folder, `py_06_api_practice`.
2. Create your own branch named it as `[your name]_api_drama` based on master
3. Read through 'README.md' file
4. Name your homework file as `[your name].py`
5. Commit your homwork file to local branch
6. Push your branch to remote
7. Create PR and add reviewer on Github

In this Assignment, you will need to use python to extract data from JSON, one of the most popular format of API.

##Deliverable: 
Use python to call API and display the following details:
1. Drama Title
2. Location
3. Performance time (greater than 2018/01/01 00:00:00)
4. Total count of dramas with different time (same drama but different time are different counts)

##Materials:
API: https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=2 (Highly recommend to install Chrome extension JSONView to have a better look at data structure)

##Time estimation: 0.5 to 1.5 hours

##Limitation:
None, do whatever you like as long as you can extract and display the deliverable. 
##!!CAUTION!! Hard-code may serious affect the performance and get BOOs from other people!

##Assignment instruction 
You may found helpful `Sample code below but suggest follow the step and try it first`

1. Import libraries json urllib mentioned at reference
2. Open,read and decode the API url, you may use print to test and found something like

```
0:00"}],"showUnit":"","discountInfo":"","descriptionFilterHtml":"","imageUrl":"","masterUnit":[],"subUnit":[],"supportUnit":[],"otherUnit":[],"webSales":"https://www.accupass.com/event/1806181412251090157280","sourceWebPromote":"","comment":"","editModifyDate":"","sourceWebName":"花蓮縣文化局","startDate":"2018/08/22","endDate":"2018/08/22","hitRate":0},{"version":"1.4","UID":"5b55bd96d083a3989c55aa14","title":"107年花蓮漫畫夏令營","category":"2","showInfo":[{"time":"2018/08/02 00:00:00","location":"花蓮市中山路71號","locationName":"花蓮鐵道文化園區一館中山堂","onSales":"N","price":"","latitude":null,"longitude":null,"endTime":"2018/08/21 00:00:00"}],"showUnit":"","discountInfo":"","descriptionFilterHtml":"","imageUrl":"","masterUnit":[],"subUnit":[],"supportUnit":[],"otherUnit":[],"webSales":"https://www.facebook.com/fishanima/","sourceWebPromote":"","comment":"","editModifyDate":"","sourceWebName":"花蓮縣文化局","startDate":"2018/08/02","endDate":"2018/08/21","hitRate":0}]
```

3. Extract JSON object by using json.loads function 
4. Write loop to get the target details and counts `Hint: Review the 5.5 and 5.6`








```Sample Code, please replace 'something'```

import json
import urllib.request, urllib.parse, urllib.error
urllib.request.urlopen('something')
'something'.read().decode()
json.loads('something')


