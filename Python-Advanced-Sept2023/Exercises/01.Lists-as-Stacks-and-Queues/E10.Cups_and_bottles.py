from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = deque([int(x) for x in input().split()])

wasted = 0

while cups and bottles:
    cup = cups.popleft()
    while cup > 0:
        bottle = bottles.pop()
        if bottle > cup:
            wasted += bottle - cup
            break
        cup -= bottle
        if not bottle:
            break
if bottles:
    print(f'Bottles: {" ".join([str(x) for x in bottles])}')
if cups:
    print(f'Cups: {" ".join([str(x) for x in cups])}')
print(f'Wasted litters of water: {wasted}')
