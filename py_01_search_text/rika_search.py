inputText = input("Please enter keyword for search: ")

file = open("article.txt", "r")
fileContent = file.readlines()
file.close()

inputTextLower = inputText.lower()
matchedCount = 0;
for line in fileContent:
    for word in line.split():
        wordLower = word.lower()
        matchedCount += wordLower.count(inputTextLower)

print("Keyword {}: We have found {} matched in article".format(inputText, matchedCount))
