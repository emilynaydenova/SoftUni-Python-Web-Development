# Mu Online

HEALTH = 100
BITCOINS = 0

current_health = HEALTH
current_bitcoins = BITCOINS
line = input().split('|')

for i, room in enumerate(line):
    command, v = room.split()
    number = int(v)
    if command == 'potion':
        if (current_health + number) > 100:
            number = 100 - current_health
        current_health += number
        print(f'You healed for {number} hp.')
        print(f'Current health: {current_health} hp.')
    elif command == 'chest':
        current_bitcoins += number
        print(f'You found {number} bitcoins.')
    else:
        current_health -= number
        if current_health <= 0:
            print(f'You died! Killed by {command}.')
            print(f'Best room: {i + 1}')
            break
        print(f'You slayed {command}.')
else:
    print(f'You\'ve made it!')
    print(f'Bitcoins: {current_bitcoins}')
    print(f'Health: {current_health}')
