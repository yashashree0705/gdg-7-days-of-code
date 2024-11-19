def pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))
N = int(input("Enter the number for the pyramid: "))
pyramid(N)