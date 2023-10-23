# Track Tour
# https://pastebin.com/FSFAFDim

from collections import deque
pumps = deque()  # (amount of petrol ,distance in kilometers)
tank = 0

pumps_count = int(input())

for _ in range(pumps_count):
    pumps.append([int(x) for x in input().split()])

current_pump_index = 0

while current_pump_index < pumps_count:
    tank = 0
    for i in range(pumps_count):
        (amount, distance) = pumps[i]
        tank += amount - 1 * distance  # 1l per 1 km
        if tank < 0:
            # ----
            pumps.rotate(-1)  # rotate right to left
            # -----
            current_pump_index += 1
            break   # continue with next pump as start
    else:  # full circle
        break
print(current_pump_index)

# 3
# 1 5
# 10 3
# 3 4
# deque([[1, 5], [10, 3], [3, 4]])
# deque([[10, 3], [3, 4], [1, 5]])
# 1