# Loop lists 

list = ["apple","banana","cherry"]
for x in list:        
    print(x)


print()

# loop through the index numbers
# user range() and len() functions 
cars = ["bmw","ford","toyota","mercedes"]
for i in range(len(cars)):
    print(cars[i])


print()

# Using While Loop
i = 0
while i < len(cars):    #Print all items, using a while loop to go through all the index numbers
    print(cars[i])
    i += 1

print()

# looping using list comprehension
[print(x) for x in cars] 

print()
watches = ["casio","titan","ducati"]
print(watches)

print()
for i in range(len(watches)):
    print(watches[i])

    