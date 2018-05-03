inputText = input("Please enter keyword for search: ")

file = open("article.txt", "r")
fileContent = file.readlines()
file.close()

matchedCount = 0;
for line in fileContent:
    for word in line.split():
        if word.find(inputText) != -1:
        	matchedCount += 1

print("Keyword {}: We have found {} matched in article".format(inputText, matchedCount))
