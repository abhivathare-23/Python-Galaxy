# logical or operator

x=10
y=-10
z=0

if x>0 or y>0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")
    if y>0 or z>0:
        print("Either of the number  is greater than 0")
    else :
        print("No number is greater than 0")