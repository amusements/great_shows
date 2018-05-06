#!/usr/local/bin/python3

''' ----- search practice -----'''

Keyword = input("Type Keyword: ")
k=0
with open("py_01_search_text/article.txt","r") as f:
	for line in f:
		words = line.split()
		for i in words:
			if (i ==Keyword):
				k=k+1
	print("We have found", k, "matched in article")