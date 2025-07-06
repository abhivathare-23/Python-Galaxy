# Access tuple items

tuple = ("apple","banana","mango")
print(tuple)

# negative indexing
print(tuple[-1])

# range of indexes
# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new tuple with the specified items.
print()
fruits = ("apple","banana","cherry","mango","kiwi","melon")
print(fruits[2:5])
# The search will start at index 2 (included) and end at index 5 (not included).

print()
print(fruits[:4])
print(fruits[4:])

# range of negative indexes
print(fruits[-4:-1])


# check if item exists
thistuple = ("apple","banana","mango")
if "apple" in thistuple:
    print("yes, 'apple' is in the fruits tuple")

