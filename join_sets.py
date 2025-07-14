# join sets 
# union() and update() method join all items from both sets
# intersection() method keeps only duplicates
# difference() method keeps items from first set that are not in other set()
# symmetric_difference() method keeps all items except the duplicates



# using union() method  /  we can use | operator instead union(), will give same result
pr = {"a","b","c"}
num  = {1,2,3,4}
cars = {"bmw","ford","mustang","buggati"}
name = {"abhi","rohit","varun"}

set = num.union(cars)
print(set)


print()
# use | to join two sets
set2 = num | cars
print(set2)


print()
# join multiple sets with union() method

myset = pr.union(num,cars,name)
print(myset)


print()
# using the | operator seperate sets with more | operator
# use | to join two sets

thisset = pr | num | cars | name
print(thisset)



print()
# join a set and tuple using union()
x = {"ab","cd","ef"}
y = (12,34,56)
z = x.union(y)
print(z)


print()
# update() method inserts all items from one set to another
# update() changes the original set and does not return a new set

veg = {"carrot","onion"}
nm = {1,2}
veg.update(nm)
print(veg)
# both union() and update() exclude any duplicate items


print()
# intersection - keep only the duplicates
# item present in both set will be shown
fruits = {"pineapple","orange","kiwi","python"}
lang = {"java","c++","python"}
flan = fruits.intersection(lang)
print(flan)

# we can use & operator instead intersection() method
flan2 = fruits & lang
print(flan2)


print()
#intersection_update() also keep only duplicates but it will change original set instead of returning new set

players ={"virat","sachin","dhoni","rohit"}
rank ={1,2,3,4,"sachin"}

players.intersection_update(rank)
print(players)



print()
# true and 1 are considered same value same goes for false and 0
k = {"apple",1,"banana",0,"cherry"}
l = {False,"google",1,"apple",2,True}

kl = k.intersection(l)
print(kl)



print()
# difference()  keep all items from set1 that are not in set2 , we can use - operator instead difference()
developers = {"james","denis","guido"}
languages = {"java","c","python","james"}

delang  = developers.difference(languages)
print(delang) 


print()
# difference_update() method to keep the items that are not present in both sets
setm = {"apple","banana","kiwi"}
setn = {"google","microsoft","apple"}

setm.difference_update(setn)
print(setm)



print()
# symmetric_difference() method will keep only elements that are not present in both sets 
setX = {"apple","banana","cherry"}
setY = {"google","microsoft","apple"}
setZ = setX.symmetric_difference(setY)   #We can use ^ operator instead 
                                            #setZ = setX ^ setY
print(setZ)


print()
# symmetric_difference_update() method to keep the items that are not present in both sets
setkl = {"apple","banana","cherry"}
setmn = {"google","microsoft","apple"}

setkl.symmetric_difference_update(setmn)
print(setkl)

