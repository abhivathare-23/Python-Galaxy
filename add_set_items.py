# add set items 
# once a set is created we cannot change its items but we can add new item
# using add() method

set = {"apple","mango","cherry"}
set.add("orange")
print(set)


print()
# add elements from another set to current set, use update() method 

cars = {"bmw","ford","mustang"}
set.update(cars)
print(set)



print()
# add any itterable
# add elements of list to set

list = ["python","java"]
sets = {"javascript","c++"}

sets.update(list)
print(sets)

