big_box = ["Orchild", "Mickey Mouse", "Orange", "Cat", "Cow", "Leon Tree", "Red Pepper"]
#plants = ["Orchild", "Orange", "Leon Tree", "Red Pepper"]
animals = ["Mickey Mouse", "Cat", "Cow"]
for obj in big_box:
    if (obj != animals):
        print (obj,"watered")
        continue
   

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


