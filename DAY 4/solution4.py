X=int(input("enter no of colleges: "))
Y=int(input("enter no of students: "))
Z=int(input("enter no of passed students: "))
total=X*Y
if Z > total / 2:
    print("yes")
else:
    print("no")
