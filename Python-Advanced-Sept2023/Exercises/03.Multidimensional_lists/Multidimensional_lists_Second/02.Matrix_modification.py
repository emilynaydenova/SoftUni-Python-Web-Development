n = int(input())
a = [[int(x) for x in input().split()] for _ in range(n)]

while True:
    command = input()
    if command == 'END':
        break
    action, *values = command.split()
    i, j, v = [int(x) for x in values]

    if not (0 <= i < n and 0 <= j < n):
        print("Invalid coordinates")
        continue

    if action == 'Add':
        a[i][j] += v
    elif action == 'Subtract':
        a[i][j] -= v

[print(' '.join([str(x) for x in row])) for row in a]
