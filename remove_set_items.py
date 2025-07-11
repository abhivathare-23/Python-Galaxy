# Remove set items
# use the remove() or discard() method

set1 = {"apple","banana","mango"}

set1.remove("apple")
print(set1)

# with discard() method
set1.discard("banana")
print(set1)


# remove random item using pop() method
cars = {"bmw","ford","mustang","buggati"}
x = cars.pop()
print(x)  # removed item
print(cars)  # set after removal



# clear() method empties the set

vegies = {"onion","carrot","bringle","califlower"}

vegies.clear()
print(vegies)       # it will show empty set


# del set
vram = {"gammix","wd","alketron"}
del vram
print(vram)  # error will show cause set is deleted







