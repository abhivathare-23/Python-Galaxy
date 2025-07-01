# List Comprehension 

fruits = ["apple","banana","cherry","kiwi","mango"]
newlist = []

for x in fruits:
    if "a" in x:            # Check if "a" is present in the fruit name
        newlist.append(x)

print(newlist)


newlist1 = [x for x in fruits if "a" in x]
print(newlist1)

# newlist = [expression for item in iterable if condition == True]


newlist2 = [x for x in fruits if x != "apple"]
 # Only accept items that are not "apple":
print(newlist2)

# with no if statment
newlist3 = [x for x in fruits]
print(newlist3)

# we can use range() function to create an iterable
newlist4 = [x for x in range(10)]
print(newlist4)


# accept only numbers lower than 5
newlist5 = [m for m in range(10) if m<5]
print(newlist5)


# set values in the list to upper case 
newlist6 = [x.upper() for x in fruits]
print(newlist6)

# set all values in the new list to 'hello'
newlist7 = ['hello' for x in fruits]
print(newlist7)

# manipulate outcomes
# return "orange" instead of "banana"

nlist = [x if x != "banana" else "orange" for x in fruits]
print(nlist)
#Return the item if it is not banana, if it is banana return orange




