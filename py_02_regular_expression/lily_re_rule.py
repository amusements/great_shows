#!/Users/yaliyang/anaconda3/bin/python3

import re

test_dialog = input ("Keyword : ")

matches_1 = re.findall('^\w+@[A-Za-z0-9]*.[A-Za-z]{3}$', test_dialog)

matches_2 = re.findall('^09[0-9]{8}$', test_dialog)

matches_3 = re.findall(r'^[A-Z]{1}[12]{1}\d{8}$', test_dialog)

if matches_1:
    print ('Keyword', matches_1, 'is an email')

elif matches_2:
    print ('Keyword', matches_2, 'is a cellphone number')

elif matches_3:
    print ('Keyword', matches_3, 'is an ID number')

else:
    print('Not found')


