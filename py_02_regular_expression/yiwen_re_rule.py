import re

# DEFINE
inputText = input("Please enter keyword: ")
mailRegular = '^[0-9a-z._+-]*@[a-z0-9]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$'
phoneRegular = '^09[0-9]{8}$'
twIdRegular = '^[A-Z]{1}[0-9]{9}$'
idVerifyDictionary = {"A": "10", "B": "11", "C": "12",
                      "D": "13", "E": "14", "F": "15",
                      "G": "16", "H": "17", "I": "34",
                      "J": "18", "K": "19", "L": "20",
                      "M": "21", "N": "22", "O": "35",
                      "P": "23", "Q": "24", "R": "25",
                      "S": "26", "T": "27", "U": "28",
                      "V": "29", "W": "32", "X": "30",
                      "Y": "31", "Z": "33"}
weight = [1,9,8,7,6,5,4,3,2,1,1]

# FUNCTION(s)
def is_tw_id(inStr):
    head = idVerifyDictionary[inStr[0]]
    body = inStr[1:10]
    e = head + body

    total = 0
    for index, val in enumerate(weight):
        total += (int(val) * int(e[index]))

    if total % 10 == 0:
        print("Keyword {} is a TW id".format(inStr))
    else :
        print("Keyword {} is not TW id".format(inStr))


# MAIN
if re.match(mailRegular, inputText) != None:
    print("Keyword {} is a email".format(inputText))
elif re.match(phoneRegular, inputText) != None:
    print("Keyword {} is a mobile phone number".format(inputText))
elif re.match(twIdRegular, inputText) != None:
    is_tw_id(inputText)
else :
    print("Keyword {} is not matched".format(inputText))
