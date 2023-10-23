n = int(input())  # square matrix size

a = [[int(j) for j in input().split()] for _ in range(n)]

for bomb in input().split():
    row, column = [int(x) for x in bomb.split(',')]
    value_of_bomb = a[row][column]
    if value_of_bomb <= 0:
        continue
    a[row][column] = 0  # bomb explodes

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            x = row + i
            y = column + j

            if 0 <= x < n and 0 <= y < n and a[x][y] > 0:
                a[x][y] -= value_of_bomb

flattened = [num for row in a for num in row]
alive_cells = [x for x in flattened if x > 0]

print(f'Alive cells: {len(alive_cells)}')
print(f'Sum: {sum(alive_cells)}')

[print(' '.join([str(x) for x in row])) for row in a]
