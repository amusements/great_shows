#!/usr/local/bin/python3


'''----- 九九乘法表 -----
for i in range(1,10):
	for j in range(1,10):
		print ("{}*{}={}\t".format(i,j,i*j),end="")
	print()
'''

'''----- Rigt Triangle -----

for i in range (0,3):
	for j in range (i+1):
		print ("*",end="")
	print()
'''

'''----- Tree ----- '''

x = 6
c = "*"

## for cone ##
for i in range(x):
	print((c*i).rjust(x-1)+c+(c*i).ljust(x-1))

## for bottom ##
for i in range(x-2):
	print((c*3).center(x*2))