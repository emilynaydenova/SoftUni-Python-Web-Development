rows, columns = [int(x) for x in input().split()]
a = [[ch for ch in input().split()] for _ in range(rows)]

square_matrix = 0

for i in range(rows - 1):
    for j in range(columns - 1):
        if a[i][j] == a[i][j + 1] == a[i + 1][j] == a[i + 1][j + 1]:
            square_matrix += 1

print(square_matrix)


