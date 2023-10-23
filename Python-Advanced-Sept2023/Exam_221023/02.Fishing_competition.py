"""
You are a longtime captain of an old fishing vessel.
The new fishing season begins and you prepare your ship
to set sail in search of the big catch…
"""
QUOTA = 20

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

size = int(input())
fishing_area = [list(input()) for _ in range(size)]

me_x, me_y = None, None

for i in range(size):
    for j in range(size):
        if fishing_area[i][j] == 'S':
            me_x, me_y = i, j
            break

fishing_catch = 0
is_reached = False

while (command := input()) != 'collect the nets':
    new_x, new_y = me_x + directions[command][0], me_y + directions[command][1]

    # If you leave the fishing area  you will be moved to the opposite side of the one you were on
    if not 0 <= new_x < size or not 0 <= new_y < size:
        if command == 'right':
            new_y = 0
        elif command == 'left':
            new_y = size - 1
        elif command == 'up':
            new_x = size - 1
        elif command == 'down':
            new_x = 0

    fishing_cell = fishing_area[new_x][new_y]

    # move to a fish passage
    if fishing_cell.isdigit():
        fishing_catch += int(fishing_cell)
        # if ship reaches the quota
        if fishing_catch >= QUOTA and not is_reached:
            print("Success! You managed to reach the quota!")
            is_reached = True

    # ship falls into a whirlpool
    elif fishing_cell == 'W':
        print("You fell into a whirlpool! The ship sank and you lost the fish you caught. ", end='')
        print(f'Last coordinates of the ship: [{new_x},{new_y}]')
        break

    fishing_area[me_x][me_y] = '-'
    me_x, me_y = new_x, new_y
    fishing_area[me_x][me_y] = 'S'


else:
    if fishing_catch < QUOTA:
        print("You didn't catch enough fish and didn't reach the quota! ", end='')
        lack = QUOTA - fishing_catch
        print(f"You need {lack} tons of fish more.")

    if fishing_catch > 0:
        print(f"Amount of fish caught: {fishing_catch} tons.")

    [print(''.join([str(x) for x in row])) for row in fishing_area]

"""
Test inputs:

4
---S
----
9-5-
34--
down
down
right
down
collect the nets

5
S---9
777-1
W333-
11111
-----
down
down
right
down
collect the nets

5
S---9
777-1
--5--
11W11
988--
down
down
down
down
down
down
right
right
right
collect the nets

"""
