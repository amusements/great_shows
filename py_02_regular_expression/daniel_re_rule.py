#!/usr/local/bin/python3

import re
Keyword = input("Please tpye the keyword: ")
Email = re.match("[^@]+@[^@]+\.[^@]+",Keyword)
Phone = re.match("^09\d{8}",Keyword)
TWID = re.match("^[A-Z][12][0-9]{8}$",Keyword)
def letter(x):
	return{
	"A":10,
	"B":11,
	"C":12,
	"D":13,
	"E":14,
	"F":15,
	"G":16,
	"H":17,
	"I":34,
	"J":18,
	"K":19,
	"L":20,
	"M":21,
	"N":22,
	"O":35,
	"P":23,
	"Q":24,
	"R":25,
	"S":26,
	"T":27,
	"U":28,
	"V":29,
	"W":32,
	"X":30,
	"Y":31,
	"Z":33,
	}[x]

def TWID(x):
	letter_str = int(str(letter(Keyword[0]))+(Keyword[1:]))  #Change letter to number and merge w/ rest ID number
	letter_list = list(map(int,str(letter_str))) #Convert letter_str to list for calculation
	num = [1,9,8,7,6,5,4,3,2,1,1] #ID check rule
	verify = list(map(lambda x,y:x*y,letter_list,num)) #multiply ID w/ checkrule
	if sum(verify)%10 == 0:
		print (Keyword, "is a valid TWID")
	else:
		print(Keyword, "is not a valid TWID")
if Email:
	print(Keyword, "is an email address")
elif Phone:
	print(Keyword, "is an mobile phone number")
elif TWID:	
	TWID(Keyword)
elif ValueError:
	print("Can't verify the Keyword")

'''
#--------list multiply test------


a = [1,2,3]
b = [4,5,6]
c = list(map(lambda x,y:x*y,a,b))

print(reduce(lambda x,y:x*y,c))
'''


