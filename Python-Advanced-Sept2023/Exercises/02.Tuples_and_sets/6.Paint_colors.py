from collections import deque

main_colors = ["red", "yellow", "blue"]
secondary_colors = {

        "orange": ['red', 'yellow'],
        "purple": ['red', 'blue'],
        "green": ['yellow', 'blue']
    }
collected_colors = []

line = deque(input().split())

while line:
    left = line.popleft()
    right = line.pop() if line else ''

    color = f'{left}{right}'
    if color in main_colors or color in secondary_colors:
        collected_colors.append(color)
        continue

    color = f'{right}{left}'
    if color in main_colors or color in secondary_colors:
        collected_colors.append(color)
        continue

    left = left[:-1]
    right = right[:-1]

    if left:
        line.insert(len(line) // 2, left)
    if right:
        line.insert(len(line) // 2, right)


for color in collected_colors:
    if color in secondary_colors:
        color_parts = secondary_colors[color]
        if not color_parts[0] in collected_colors or not color_parts[1] in collected_colors:
            collected_colors.remove(color)

print(collected_colors)
