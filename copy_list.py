#Copy list
# use built-in list method copy() to copy a list

list_values = ["apple","banana","cherry"]
list2 = list_values.copy()
print(list2)


print()
# list() method - another way to copy a list

thislist = ["bmw","ford","mustang","mercedes"]
mylist = list(thislist)
print(mylist)

print()
# use slice operator to copy a list using slice operator [:]
list2 = ["john","arya","sansa"]
list3 = list2[:]
print(list3)



