n = int(input())
a = [input().split() for _ in range(n)]

# Bunny's coordinates
x, y = [(i, j) for i in range(n) for j in range(n) if a[i][j] == 'B'][0]

max_points = 0
max_direction = None

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}
points = {
    'up': 0,
    'down': 0,
    'left': 0,
    'right': 0
}

movement = {
    'up': [],
    'down': [],
    'left': [],
    'right': []
}

for direction, v in directions.items():
    cur_x, cur_y = x, y

    while 0 <= (cur_x + v[0]) < n and 0 <= (cur_y + v[1]) < n:
        cur_x += v[0]
        cur_y += v[1]
        if a[cur_x][cur_y] == 'X':
            break
        else:
            points[direction] += int(a[cur_x][cur_y])
            movement[direction].append((cur_x, cur_y))

max_points = 0
max_dir = 'up'
for direction, eggs in points.items():
    if eggs >= max_points:
        max_points = eggs
        max_dir = direction

print(max_dir)
for cc in movement[max_dir]:
    print(list(cc))

print(max_points)
