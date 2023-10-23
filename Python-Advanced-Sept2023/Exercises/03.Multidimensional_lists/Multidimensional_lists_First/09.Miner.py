field_size = int(input())
movements = input().split()

a = [[s for s in input().split()] for _ in range(field_size)]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

x, y = 0, 0  # position of miner - s
max_coal = 0
for i in range(field_size):
    for j in range(field_size):
        if a[i][j] == 's':        # start position of miner
            x, y = i, j
        elif a[i][j] == 'c':
            max_coal += 1         # total coals

coal = 0
for mov in movements:
    old_x, old_y = x, y
    # new coordinates of Miner
    x += directions[mov][0]
    y += directions[mov][1]
    if (not 0 <= x < field_size) or (not 0 <= y < field_size):
        x, y = old_x, old_y  # stay on the old position
        continue
    # move to the new coordinates
    a[old_x][old_y] = '*'
    if a[x][y] == 'e':
        print(f'Game over! ({x}, {y})')
        break
    elif a[x][y] == 'c':
        coal += 1
        if coal == max_coal:
            print(f'You collected all coal! ({x}, {y})')
            break
    a[x][y] = 's'
else:
    print(f'{max_coal-coal} pieces of coal left. ({x}, {y})')

print(*a)