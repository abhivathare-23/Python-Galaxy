# update tuples - Tuples are unchangeable, meaning that you cannot change, 
# add, or remove items once the tuple is created. But there are some workarounds.
# You can convert the tuple into a list, change the list, and convert the list back into a tuple.

x =("apple","mango","cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

print()
# add items
thistuple = ("apple","mango","kiwi")
m = list(thistuple)
m.append("orange")
thistuple = tuple(m)
print(thistuple)

# add tuple to a tuple
l = ("cherry",)
thistuple += l
print(thistuple)


print()
# remove items - you cannot remove items in tuple
# Convert the tuple into a list, remove item, and convert it back into a tuple:

cars = ("bmw","ford","mustang")
j = list(cars)
j.remove("ford")
cars = tuple(j)
print(cars)

# or we can delete tuple completly - the del keyword
vegies  = ("flower","carrot","onion")
del vegies
print(vegies)   #this will raise error cause tuple is no longer exist



