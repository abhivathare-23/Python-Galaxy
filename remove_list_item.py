# Remove list items

# remove specified item from the list
list = ["apple","banana","cherry"]
list.remove("banana")  # remove banana from the list
print(list)

cars = ["bmw","ford","toyota","mercedes","ford"]
cars.remove("ford")     # remove first occurrence of ford from the list
print(cars)


# remove item at specified index
fruits = ["mango","kiwi","orange"]
fruits.pop(1)
print(fruits)  # remove item at index 1 (kiwi)

laptops = ["asus","hp","lenovo","dell"]
laptops.pop()
print(laptops)      #If you do not specify the index, the pop() method removes the last item


#The del keyword also removes the specified index:
del laptops[2]
print(laptops) # remove item at index 2 (lenovo) 

vegies = ["carrot","potato","cabbage"]
del vegies # delete the entire list
#print(vegies)  # this will raise an error because the list no longer exists

cities = ["banglore","mumbai","pune"]
print(cities)

cities.clear()  # remove all items from the list
print(cities)