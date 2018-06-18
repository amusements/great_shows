#!/Users/yaliyang/anaconda3/bin/python3

file = open('article.txt','r')

word = file.read()

file.close

show = input("Keyword : " ) 

output = word.count(show)

print("Keyword", show, ":", "We have found", output, " matched in the article")

 
