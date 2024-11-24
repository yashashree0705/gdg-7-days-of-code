def mat(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    a = set()
    b = set()
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                a.add(i)
                b.add(j)
    for i in range(rows):
        for j in range(cols):
            if i in a or j in b:
                matrix[i][j] = 0
n, m = map(int, input("Enter rows and columns: ").split())
matrix = [list(map(int, input().split())) for j in range(n)]
mat(matrix)
print("output: ")
for row in matrix:
    print(*row)
