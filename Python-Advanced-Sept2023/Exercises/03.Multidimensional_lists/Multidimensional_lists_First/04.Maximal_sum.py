import sys

rows, columns = [int(x) for x in input().split()]
a = [[int(x) for x in input().split()] for _ in range(rows)]

max_sum = -sys.maxsize # if =0 -> 80%
# max_sum = float('-inf')

top_left_corner = [0, 0]

for i in range(rows - 2):
    for j in range(columns - 2):
        total = 0
        for k in range(i, i + 3):
            for m in range(j, j + 3):
                total += a[k][m]
        if total > max_sum:
            max_sum = total
            top_left_corner = [i, j]

print(f'Sum = {max_sum}')

for i in range(top_left_corner[0], top_left_corner[0] + 3):
    print(' '.join([str(a[i][j]) for j in range(top_left_corner[1], top_left_corner[1] + 3)]))

# ---------


rows, columns = [int(x) for x in input().split()]
matrix = []
max_sum = -sys.maxsize
max_submatrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

for row in range(rows - 2):
    for col in range(columns - 2):
        submatrix = [
            [matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]],
            [matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]],
            [matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]
        ]
        sum_elements = sum(submatrix[0]) + sum(submatrix[1]) + sum(submatrix[2])
        if sum_elements > max_sum:
            max_sum = sum_elements
            max_submatrix = submatrix

print(f"Sum = {max_sum}")
for row in max_submatrix:
    print(" ".join(str(x) for x in row))