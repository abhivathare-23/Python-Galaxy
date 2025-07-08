# unpacking a tuple
# when we create tuple ,we normally assign values to it, this is called 'packing' a tuple

fruits = ("apple","mango","cherry")
print(fruits)


# unpacking a tuple 
(green, yellow, red)  = fruits

print(green)
print(yellow)
print(red)


print()
# using asterisk *

tuple = ("apple","mango","cherry","raspberry","strawberry")

(g, y, *r) = tuple

print(g)
print(y)
print(r)

# Python will assign values to the variable 
# until the number of values left matches the number of variables left

print()
thistuple = ("apple","mango","papaya","pineapple","cherry")
(grn, *tropic, rd) = thistuple
print(grn)
print(tropic)
print(rd)




