list1 =[1,2,3,4,5]
list2 =[6,7,8,9]
for item in list1:
    if item in list2:
        print("Overlapping")
    else:
        print("Not Overlapping")
