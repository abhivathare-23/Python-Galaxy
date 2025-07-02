# Sort lists 
# sort list Alphanumerically
# sort() assending by default

list = ["ab","virat","chris","rajat","jitesh","krunal"]
list.sort()
print(list)


# sort list numerically
list2 = [34,64,63,24,42,86]
list2.sort()
print(list2)

# sort decending use - reverse=True
list.sort(reverse=True)
print(list)


# sort list decending numerically
list2.sort(reverse=True)
print(list2)


print()

# customize sort function
# customize function using keyword argument key = function

def myfunc(n):
    return abs(n-50)

dlist = [100,50,65,82,23]
dlist.sort(key=myfunc)
print(dlist)

print()

#case insensitive sort
#capital letters being sorted before lower case letters
flist = ["banana","Orange","Kiwi","apple","cherry"]
flist.sort()
print(flist)

print()
#if you want a case-insensitive sort function, use str.lower as a key function
flist.sort(key = str.lower)
print(flist)


print()
# Reverse order
flist.reverse()
print(flist)



