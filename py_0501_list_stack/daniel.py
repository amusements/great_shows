
result = []
for i in range (1,21):
	a = i**2
	result.append(a)
##Q1
print(result[:5]) 
##Q2
print(result[10]) 
##Q3
result.reverse()
print(result.pop()) 
##Q4
result.insert(12, "I am rock")
print(result)
##Q5
result.remove("I am rock")
print(result)


