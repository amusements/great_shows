word = format(input('Input yout word: ')).lower()
with open('article.txt','r') as f:
    for line in f:
        if word in line.lower():
                print ("keyword",(word),":We have found",(sum(line.count(word) for line in f)),"matched in article")