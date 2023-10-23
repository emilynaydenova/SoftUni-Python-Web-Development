from collections import deque

clothes = deque([int(x) for x in input().split()])

rack_capacity = int(input())
racks_count = 1
current_rack_capacity = 0

while clothes:
    cloth_piece = clothes.pop()
    if current_rack_capacity + cloth_piece <= rack_capacity:
        current_rack_capacity += cloth_piece
    else:
        current_rack_capacity = cloth_piece
        racks_count += 1

print(racks_count)

# --------------------
