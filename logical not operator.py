#logical not operator

l=10
if not l:
    print("Boolean value of l is True")
    if not(l%3==0 or l%5==0):
        print("10 is not divisible by either 3 or 5")
    else:
        print("10 is divisible by either 3 or 5")
        