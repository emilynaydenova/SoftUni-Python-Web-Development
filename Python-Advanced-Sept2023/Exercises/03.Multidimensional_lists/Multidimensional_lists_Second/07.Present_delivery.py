def move_Santa(direction, row, column, kids, gifts):
    moving = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1)
    }

    new_row = row + moving[direction][0]
    new_column = column + moving[direction][1]

    if 0 <= new_row < n and 0 <= new_column < n:
        if a[new_row][new_column] == 'V':
            a[row][column] = '-'
            a[new_row][new_column] = 'S'
            kids -= 1
            gifts -= 1

        elif a[new_row][new_column] in ['X', '-']:
            a[row][column] = '-'
            a[new_row][new_column] = 'S'
        #     Cookies
        elif a[new_row][new_column] == 'C':
            a[row][column] = '-'
            a[new_row][new_column] = 'S'
            for key, value in moving.items():
                rr = new_row + value[0]
                cc = new_column + value[1]

                if a[rr][cc] == 'V' and gifts > 0:
                    a[rr][cc] = '-'
                    kids -= 1
                    gifts -= 1
                elif a[rr][cc] == 'X' and gifts > 0:
                    a[rr][cc] = '-'
                    gifts -= 1
                if gifts == 0:
                    break
    return kids, gifts


# main program's inputs
presents = int(input())  # count of presents
n = int(input())  # size of the neighborhood
a = [[x for x in input().split()] for _ in range(n)]
# Nice kids' houses
v = nice_kids = len([(i, j) for i in range(n) for j in range(n) if a[i][j] == 'V'])


while True:
    command = input()
    if command == 'Christmas morning':
        break
    #  find Santa's coordinates
    sr, sc = [(i, j) for i in range(n) for j in range(n) if a[i][j] == 'S'][0]

    v, presents = move_Santa(command, sr, sc, v, presents)
    if presents == 0:
        break


if presents == 0 and v > 0:
    print("Santa ran out of presents!")
for line in a:
    print(' '.join(line))

if v == 0:
    print(f'Good job, Santa! {nice_kids} happy nice kid/s.')
else:
    print(f'No presents for {v} nice kid/s.')

# 5
# 4
# - X V -
# - S - V
# - - - -
# X - - -
# up
# right
# down
# right
# Christmas morning
