big_box = ["Orchild", "Mickey Mouse", "Orange", "Cat", "Cow", "Leon Tree", "Red Pepper"]
for obj in big_box:
    if (obj == "Mickey Mouse" or obj == "Cat" or obj == "Cow"):
        continue
    print (obj,"watered")
 

for obj in big_box:
    if (obj == "Cow"):
       print (obj,"feeded")
       break


for obj in big_box:
    if (obj == "car"):
        print (obj,"is a car")
        break
else:
    print ("No car to wash")