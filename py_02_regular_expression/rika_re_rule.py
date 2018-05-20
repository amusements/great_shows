import re
inputText = input("Please enter keyword: ")
mailRegular = '^[0-9a-z._+-]*@[a-z0-9]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$'
phoneRegular = '^09[0-9]{8}$'
twIdRegular = '^[A-Z]{1}[0-9]{9}$'
idVerifyDictionary = {"A": 10, "B": 11, "C": 12,
                      "D": 13, "E": 14, "F": 15,
                      "G": 16, "H": 17, "I": 34,
                      "J": 18, "K": 19, "L": 20,
                      "M": 21, "N": 22, "O": 35,
                      "P": 23, "Q": 24, "R": 25,
                      "S": 26, "T": 27, "U": 28,
                      "V": 29, "W": 32, "X": 30,
                      "Y": 31, "Z": 33}

if re.match(mailRegular, inputText) != None:
    print("Keyword {} is a email".format(inputText))
elif re.match(phoneRegular, inputText) != None:
    print("Keyword {} is a mobile phone number".format(inputText))
elif re.match(twIdRegular, inputText) != None:
    strStrip = inputText.strip()
    strStripMaxIndex = len(strStrip)-1
    strStripFirstWord = strStrip[0]
    verifyKey = idVerifyDictionary[strStripFirstWord] 
    verifyInt = int(strStrip[strStripMaxIndex])
    verifyInt += verifyKey / 10 + (verifyKey % 10) * 9
    i = 8;
    for x in range(1, strStripMaxIndex):
        verifyInt += x * i
        i -= 1
    if verifyInt % 10 == 0:
        print("Keyword {} is a TW id".format(inputText))
    else :
        print("Keyword {} is not TW id".format(inputText))
else :
    print("Keyword {} is not matched".format(inputText))
