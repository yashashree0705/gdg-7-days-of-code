def n(a, b):
     for num in range(a, b + 1):
         if num % 5 == 0 and num % 7 == 0:
             print("FooBar")
         elif num % 5 == 0:
             print("Foo")
         elif num % 7 == 0:
             print("Bar")
         else:
             print("Baz")

a=int(input("enter number: "))
b=int(input("enter number: "))
n(a,b)


