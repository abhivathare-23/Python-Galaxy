# Taking input from user and calculating percentage and grade

s1=int(input("Enter sub1 marks : "))
s2=int(input("Enter sub2 marks : "))
s3=int(input("Enter sub3 marks : "))
s4=int(input("Enter sub4 marks : "))
s5=int(input("Enter sub5 marks : "))

total=s1+s2+s3+s4+s5
per=total/5

if per>=80:
    print("A Grade With : ",per," Percentage")
elif per>=60:
    print("B Grade With : ",per," Percentage")
else:
    print("C Grade With : ",per," Percentage")

    





