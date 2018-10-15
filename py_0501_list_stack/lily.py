#!/Users/yaliyang/anaconda3/bin/python3

square_list = []

for i in range (1, 21):

    square_list.append(i**2)
    
print (square_list [0:5])

print (square_list [11])

square_list.reverse()

square_list.pop(0)

print (square_list)

square_list.reverse()

square_list.append(400)

print (square_list)

square_list.insert(12, "I am rock")

print (square_list)
   
square_list.remove("I am rock")

print (square_list)


