# coding=UTF-8
import os
os.chdir('/Users/linda.hsu/dev/great_shows/py_01_search_text')

word = input('Input your world: ').strip()
with open('article.txt', 'r') as f:
    #print(sum(line.count(word) for line in f))
    print ("keyword",(word),":We have found",(sum(line.count(word) for line in f)),"matched in article")