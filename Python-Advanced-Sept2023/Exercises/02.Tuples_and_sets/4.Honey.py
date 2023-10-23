from collections import deque

bees = deque([int(x) for x in input().split()])
collected_nectar = deque([int(x) for x in input().split()])
honey_making = deque([x for x in input().split()])

total_honey = 0

while bees and collected_nectar:
    bee = bees.popleft()
    nectar = collected_nectar.pop()
    if nectar >= bee:
        operation = honey_making.popleft()
        if operation == '/' and nectar == 0:
            continue
        made_honey = abs(eval(f'{bee}{operation}{nectar}'))
        total_honey += made_honey
    else:
        bees.appendleft(bee)

print(f"Total honey made: {total_honey}")
if bees:
    print(f'Bees left: {", ".join([str(x) for x in bees])}')
if collected_nectar:
    print(f'Nectar left: {", ".join([str(x) for x in collected_nectar])}')
