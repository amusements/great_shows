big_box = ["Orchild", "Mickey Mouse", "Orange", "Cat", "Cow", "Leon Tree", "Red Pepper"]

# TODO: Using for-loop & continue to add water on plants, but not animal
# OUTPUT:
#   Orchild watered.
#   Orange waterd.
#   Leon Tree watered.
#   Red Pepper waterd.

for item in big_box:
	if item in ["Mickey Mouse", "Cat", "Cow"]:	
		continue
	else:
		print (item + " water")
	#plants = ['Orchild', 'Orange', 'Leon Tree', 'Red Pepper']
	#if item in plants:
	#	print (item + " water")


# TODO: Using for-loop & break to feed Cow only
# OUTPUT:
#   Cow feeded.

for item in big_box:
	if item == "Cow":
		print(item + " feeded")
		break

# TODO: Using for-loop & else to wash a car
# OUTPUT:
#   No car to wash.

for item in big_box:
	if item == "Car":
		print("I found a car")
		break
else:
	print("No car to wash")