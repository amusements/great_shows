# Q1: Define a function which can generate and print a list where the values are square of numbers between 1 and 20. Then the function needs to print the first 5 elements in the list.
# Hint:
#   Use range() for loops.
#   Use list.append() to add values into a list.
#   Use [n1:n2] to slice a list
# OUTPUT:
#   1
#   4
#   9
#   16
#   25
squares = []
for x in range (21):
    squares.append(x**2)
print (squares[0:6])

# Q2: Base on Q1, please print the 11th element.
# Hint:
#   Use list.index()
print (squares[11])

# Q3: Base on Q1, reverse list and pop out the top element and print out.
# Hint:
#   Use list.reserse() and list.pop
squares.reverse()
#print (squares)
squares.pop(0)
print (squares)


# Q4: Base on Q1, please insert "I am rock" into 13th position, then print out each element in list.
# Hint:
#   Use list.insert() and for loop
squares.insert(13,"I am rock")
print (squares)
# Q5: Base on Q4, please remove "I am rock", then print out each element in list.
# Hint:
#   Use list.remove()
squares.remove("I am rock")
print (squares)

