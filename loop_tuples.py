# Loop though tuple
# using for loop

tuple = ("apple","mango","banana")
for x in tuple:
    print(x)


print()
# loop through the index numbers
# use range() and len() function to create iterable

# print all items by referring their index number

cars = ("bmw","ford","mustang")
for i in range(len(cars)):
    print(cars[i])


print()
# using a while loop
# Use the len() function to determine the length of the tuple, 
# then start at 0 and loop your way through the tuple items by referring to their indexes.

vegies = ("flower","onion","carrot")
m = 0
while m < len(vegies):
    print(vegies[m])
    m = m + 1


