rows, columns = [int(x) for x in input().split()]
a = [[x for x in input().split()] for _ in range(rows)]

while True:
    command = input().split()
    action = command[0]
    if action == 'END':
        break
    if action != 'swap' or len(command) != 5:
        print("Invalid input!")
        continue
    # better is by validation instead of try-except
    try:
        row1, col1, row2, col2 = [int(command[i]) for i in range(1, 5)]
        a[row1][col1], a[row2][col2] = a[row2][col2], a[row1][col1]

        [print(' '.join([str(x) for x in row])) for row in a]
    except:  # don't define the kind of error
        print("Invalid input!")


# -------------
# def shuffle_matrix(row1, col1, row2, col2):
#     matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
#
#
# rows, columns = [int(x) for x in input().split()]
# matrix = [input().split() for x in range(rows)]
#
# while True:
#     command = input()
#     if command == "END":
#         break
#     if not command.startswith("swap") or len(command.split()) != 5:
#         print("Invalid input!")
#         continue
#     row_1, col_1, row_2, col_2 = [int(x) for x in command.split()[1:]]
#     if row_1 in range(rows) and col_1 in range(columns) and row_2 in range(rows) and col_2 in range(columns):
#         shuffle_matrix(row_1, col_1, row_2, col_2)
#         [print(" ".join(element)) for element in matrix]
#     else:
#         print("Invalid input!")