#!/Users/yaliyang/anaconda3/bin/python3

import re

test_dialog = input ("Keyword : ")

emailReg = '^\w+@[A-Za-z0-9]*.[A-Za-z]{3}$'

cellphoneReg = '^09[0-9]{8}$'

IDReg = r'^[A-Z]{1}[12]{1}\d{8}$'

dic_alphabet = {'A': '10', 'B': '11', 'C': '12', 'D': '13', 
                'E': '14', 'F': '15', 'G': '16', 'H': '17', 
                'I': '34', 'J': '18', 'K': '19', 'L': '20', 
                'M': '21', 'N': '22', 'O': '35', 'P': '23', 
                'Q': '24', 'R': '25', 'S': '26', 'T': '27', 
                'U': '28', 'V': '29', 'W': '32', 'X': '30', 
                'Y': '31', 'Z': '33'}  
weight = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]


def is_id(inStr):
    cha_first = dic_alphabet[inStr[0]]
    body = inStr[1:10]
    all = cha_first + body
    
    total = 0

    for index, val in enumerate(weight):
        total += (int(val) * int(all[index]))

    if total % 10 == 0:
        print ("This is a Taiwanese Id.")   
    
    else :
        print ("incorrect")


if re.match(emailReg, test_dialog) != None:

    print ('Keyword', test_dialog, 'is an email')

elif re.match(cellphoneReg, test_dialog) != None:

    print ('Keyword', test_dialog, 'is a cellphone number')

elif re.match(IDReg, test_dialog) != None:

     is_id(test_dialog)

else:
    print('Invalid')
    




    








