n, m = [int(x) for x in input().split()]

lair = []
# Player's position
x, y = (None, None)
# bunnies are marked with "B", the player is marked with "P"
for i in range(n):
    row = list(input())
    lair.append(row)
    # first position of the Player
    if 'P' in row:
        x, y = i, row.index('P')

is_won = False
is_dead = False
old_x, old_y = x, y
directions = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

exploded = []
B_explosion = [(-1, 0), (1, 0), (0, -1), (0, 1)]

movements = input()
for mov in movements:
    # P-movement
    old_x, old_y = x, y
    x += directions[mov][0]
    y += directions[mov][1]

    if (not 0 <= x < n) or (not 0 <= y < m):
        lair[old_x][old_y] = '.'
        is_won = True  # will finish

    elif (x, y) != (old_x, old_y):
        lair[old_x][old_y] = '.'
        cell = lair[x][y]
        if cell == 'B':
            is_dead = True  # will finish

        elif cell == '.':
            lair[x][y] = 'P'

    # B-exploding
    for i in range(n):
        for j in range(m):
            if lair[i][j] == 'B' and (i, j) not in exploded:

                for t in B_explosion:
                    t1 = i + t[0]
                    t2 = j + t[1]
                    if 0 <= t1 < n and 0 <= t2 < m:
                        if lair[t1][t2] == '.':
                            lair[t1][t2] = 'B'
                            exploded.append((t1, t2))
                        elif lair[t1][t2] == 'P':
                            lair[t1][t2] = 'B'
                            exploded.append((t1, t2))
                            is_dead = True



    exploded = []
    if is_won or is_dead:
        break

for row in lair:
    print(''.join(row))
if is_won:
    print(f'won: {old_x} {old_y}')
else:
    print(f'dead: {x} {y}')
