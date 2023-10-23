n = int(input())
a = [input().split() for _ in range(n)]
directions = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1),
    }

tea_bags = 0
# Alice' coordinates
x, y = [(i, j) for i in range(n) for j in range(n) if a[i][j] == 'A'][0]

while True:
    command = input()

    move = directions[command]
    go_x = x + move[0]
    go_y = y + move[1]
    a[x][y] = '*'

    if not (0 <= go_x < n and 0 <= go_y < n):
        print("Alice didn't make it to the tea party.")
        break

    elif a[go_x][go_y] == 'R':
        a[go_x][go_y] = '*'
        print("Alice didn't make it to the tea party.")
        break

    take = a[go_x][go_y]
    if take.isdigit():
        tea_bags += int(take)
        if tea_bags >= 10:
            a[go_x][go_y] = '*'
            print("She did it! She went to the party.")
            break

    a[go_x][go_y] = 'A'
    x, y = go_x, go_y

[print(' '.join(row)) for row in a]
