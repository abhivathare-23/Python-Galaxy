# python sets
# sets are used to store multiple items in single variable
# sets are unordered, unchangable and unindexed
myset = {"apple","mango","cherry"}
print(myset)
# sets are written with curly brackets


cars = {"bmw","ford","mustang","ford"}
print(cars)
# do not allow duplicate values

print()
# value True and 1 are considered same value in sets
set2 = {"banana","mango",1,True,2}
print(set2)

print()
# value False and 0 considered same value in sets
thisset = {1,"mango",False,0,"kiwi"}
print(thisset)


print()
# get the length of the set
# len()

print(len(thisset))
print(len(set2))
print(len(cars))



print()
# set items data types
p = {"apple","mango"}
m = {1,2,3}
n = {True,False,True}

print(p)
print(m)
print(n)


print()
#set can contain diff data types

set1 = {"ab",17,"True",37,"male"}
print(set1)

print()
#type()
print(type(set1))
print(type(cars))


# set() constructor
tset = set(("apple","banana","mango"))
# note- double round bracket
print(tset)
