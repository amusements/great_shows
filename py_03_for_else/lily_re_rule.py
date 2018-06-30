#!/Users/yaliyang/anaconda3/bin/python3
g_box = ["Orchild", "Mickey Mouse", "Orange", "Cat", "Cow", "Lemon Tree", "Red Pepper"]
# TODO: Using for-loop & continue to add water on plants, but not animal
# OUTPUT:
#   Orchild watered.
#   Orange waterd.
#   Lemon Tree watered.
#   Red Pepper waterd. 

# TODO: Using for-loop & break to feed Cow only
# OUTPUT:
#   Cow feeded.

# TODO: Using for-loop & else to wash a car
# OUTPUT:
#   No car to wash.

#plants = {"Orchild", "Orange", "Lemon Tree", "Red Pepper"}
#animals = {"Mickey Mouse", "Cat", "Cow"}

c_box = {
        "Orchild": "plant", "Mickey Mouse": "animal", "Orange": "plant", "Cat": "animal", 
        "Cow": "animal", "Lemon Tree": "plant", "Red Pepper": "plant"
        }


for key, value in c_box.items():
    if value == "animal":
        continue
    if value == "plant":
        print (key, "watered")


#for i in g_box:
#    if i == "Cow":
#        print ("Cow feeded")
#        break

           
#for i in g_box:
#   if i == "car":
#        print ("car washed")
#else:
#    print ("No car to wash")
    

