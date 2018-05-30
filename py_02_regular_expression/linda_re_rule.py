word = input('Input your word:').strip()
import re
phoneRegular = re.compile('^09\d{8}$')
phoneMatch = phoneRegular.match(word)
idRegular = re.compile('^[A-Z]\d{9}$')
idMatch = idRegular.match(word)
emailRegular = re.compile('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
emailMatch = emailRegular.match(word)

if phoneMatch:
    print ("keyword",word,"is a mobile phone number.")
elif idMatch:
    print ("keyword",word,"is a id.")
elif emailMatch:
    print ("keyword",word,"is a email.")
else:
    print ("error!")