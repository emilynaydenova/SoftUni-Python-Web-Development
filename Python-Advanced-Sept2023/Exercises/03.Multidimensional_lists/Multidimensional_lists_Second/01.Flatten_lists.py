matrix = [pp.split() for pp in input().split('|')][::-1]
print(matrix)
flatten_matrix = [num for row in matrix for num in row]

print(*flatten_matrix)

"""
flatten = []
for row in matrix:
    for num in row:
        flatten.append(num)
print(*flatten)
"""