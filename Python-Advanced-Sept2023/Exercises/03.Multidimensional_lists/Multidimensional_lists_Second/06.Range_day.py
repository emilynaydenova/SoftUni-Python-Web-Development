from collections import deque

size = 5
shooting_range = [[x for x in input().split()] for _ in range(size)]

n = int(input())
targets_all = [t for row in shooting_range for t in row].count('x')
targets_hit = []

for _ in range(n):
    if len(targets_hit) == targets_all:
        break
    command = deque(input().split())
    # Shooter's position
    x, y = [(i, j) for i in range(size) for j in range(size) if shooting_range[i][j] == 'A'][0]

    action = command.popleft()
    direction = command.popleft()
    if action == 'move':
        steps = int(command.popleft())
        if direction == 'up' and x - steps >= 0 and shooting_range[x - steps][y] == '.':
            shooting_range[x - steps][y] = 'A'
        elif direction == 'down' and x + steps < size and shooting_range[x + steps][y] == '.':
            shooting_range[x + steps][y] = 'A'
        elif direction == 'left' and y - steps >= 0 and shooting_range[x][y - steps] == '.':
            shooting_range[x][y - steps] = 'A'
        elif direction == 'right' and y + steps < size and shooting_range[x][y + steps] == '.':
            shooting_range[x][y + steps] = 'A'
        else:
            continue
        shooting_range[x][y] = '.'

    elif action == 'shoot':
        if direction == 'right':
            for j in range(y, size):
                if shooting_range[x][j] == 'x':
                    targets_hit.append([x, j])
                    shooting_range[x][j] = '.'
                    break
        elif direction == 'left':
            for j in range(y, -1, -1):  # !!! in reverse order
                if shooting_range[x][j] == 'x':
                    targets_hit.append([x, j])
                    shooting_range[x][j] = '.'
                    break
        elif direction == 'up':
            for i in range(x, -1,-1):  # !!! in reverse order
                if shooting_range[i][y] == 'x':
                    targets_hit.append([i, y])
                    shooting_range[i][y] = '.'
                    break
        elif direction == 'down':
            for i in range(x, size):
                if shooting_range[i][y] == 'x':
                    targets_hit.append([i, y])
                    shooting_range[i][y] = '.'
                    break

if len(targets_hit) == targets_all:
    print(f"Training completed! All {targets_all} targets hit.")
else:
    targets_left = targets_all - len(targets_hit)
    print(f"Training not completed! {targets_left} targets left.")

[print(t) for t in targets_hit]
"""
. . . . . 
. . . . . 
. . x . . 
. . . . . 
x x . . A 
3
shoot down
move right 2
shoot left
"""