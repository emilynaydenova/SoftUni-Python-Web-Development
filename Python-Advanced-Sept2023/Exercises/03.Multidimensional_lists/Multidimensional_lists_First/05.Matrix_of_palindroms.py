rows, columns = [int(x) for x in input().split()]
matrix = []

for i in range(rows):
    base_letter = chr(ord('a') + i)
    matrix.append([])
    for j in range(columns):
        middle_letter = chr(ord(base_letter) + j)

        palindrom = base_letter+middle_letter+base_letter
        matrix[i].append(palindrom)

[print(' '.join(row)) for row in matrix]