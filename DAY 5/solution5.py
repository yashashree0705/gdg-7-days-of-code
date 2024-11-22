n = int(input("Enter the size of the array: "))
pos=0
print("Enter the elements of the array:")
for i in range(n):
    num = int(input())  
    if num > 0:
        pos+= num  
print("Sum of all positive numbers:", pos)