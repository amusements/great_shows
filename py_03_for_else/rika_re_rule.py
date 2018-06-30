big_box = ["Orchild", "Mickey Mouse", "Orange", "Cat", "Cow", "Lemon Tree", "Red Pepper"]
animal = ["Mickey Mouse", "Cat", "Cow"]


# TODO: Using for-loop & continue to add water on plants, but not animal
# OUTPUT:
#   Orchild watered.
#   Orange waterd.
#   Lemon Tree watered.
#   Red Pepper waterd.
def add_water_on_plants():
    for thing in big_box:
        if thing in animal:
    	    continue
        print(thing)

# TODO: Using for-loop & break to feed Cow only
# OUTPUT:
#   Cow feeded.
def feed_cow():
    for thing in big_box:
        if thing == "Cow":
            print(thing+" feeded")
            break

# TODO: Using for-loop & else to wash a car
# OUTPUT:
#   No car to wash.
def wash_car():
    for thing in big_box:
        if thing == "Car":
            break
    else:
        print("No car to wash")

print("[Practice 1] Using for-loop & continue to add water on plants, but not animal")
add_water_on_plants()
print("\n[Practice 2] Using for-loop & break to feed Cow only")
feed_cow()
print("\n[Practice 3] Using for-loop & else to wash a car")
wash_car()
