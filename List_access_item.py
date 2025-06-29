list=["apple","Mango","Banana","Orange","Kiwi","Melon","Cherry"]

print(len(list)) # this shows length of the list

print(list[1])   # this shows item  at index 1

print(list[-2])  # negative indexing -1 is last item 

print(list[3:5])

print(list[2:])  # this shows all items from index 2 to end

print(list[:4])  # this shows all items from start to index 4

print(list[-4:-1])  # this shows items from index -4 to -1 (not including -1)



# Check if item exists in list
# To determine if a specified item is present in a list use the (in) keyword:

if "Mango" in list:
    print("yes, Mango is in the list")


