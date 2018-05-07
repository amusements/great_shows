#!/usr/local/bin/python3

import re
Keyword = input("Please tpye the keyword: ")
Email = re.match("[^@]+@[^@]+\.[^@]+",Keyword)
Phone = re.match("^09\d{8}",Keyword)
TWID = re.match("^[A-Z][12][0-9]{8}$",Keyword)

if Email:
	print(Keyword, "is an email address")
elif Phone:
	print(Keyword, "is an mobile phone number")
elif TWID:
	print(Keyword, "is not a TWID")
else:
	print("Can't verify the Keyword")


''' Verify the vaild TWID, but dont know how to put into previous if statment

a = []; a.extend("10987654932210898765431320")
c = int(a[ord(Keyword[0])-65]) + int(Keyword[9])
for x in range(1, 9):
	c += int(Keyword[x]) * (9 - x)
	if c % 10 == 0: 
		print (TWID, "is a vaild TWID")
'''