# Robotics

from collections import deque
from datetime import datetime, timedelta
from time import time

robots_params = input().split(';')

start_time = datetime.strptime(input(), '%H:%M:%S')  # 1900-01-01 08:00:00
# print(start_time.strftime('%H:%M:%S'))  # 08:00:00

# input start_time
hh, mm, ss = [int(x) for x in input().split(':')]  # [hh,mm,ss]
start_time_seconds = hh*3600 + mm*60 + ss

robots = {}  # {name: [processing_time, available_at]}
for robot in robots_params:
    parts = robot.split('-')
    robots[parts[0]] = [int(parts[1]), 0]
# {'ROB': [15, 0], 'SS2': [10, 0], 'NX8000': [3, 0]}


items = deque()  # products
next_item = input()
while next_item != 'End':
    items.append(next_item)
    next_item = input()
# deque(['detail', 'glass', 'wood', 'apple'])

current_time = 0  # start
while items:
    start_time_seconds += 1
    next_item = items.popleft()
    for robot in robots.items():  # ('ROB', [15, 0])
        if robot[1][1] <= current_time:  # robot is available
            robot[1][1] = current_time + robot[1][0]  # will be available again at ...
            time_str = (start_time + timedelta(seconds=current_time)).strftime('%H:%M:%S')
            print(f'{robot[0]} - {next_item} [{time_str}]')
            break  # only if there is free robot

    else:
        items.append(next_item)

# -----------------------------------

from collections import deque  # allow print deque


def plus_one_second(clock):  # [hh,mm,ss+1]
    clock[2] += 1
    if clock[2] >= 60:
        clock[2] = 0
        clock[1] += 1
        if clock[1] >= 60:
            clock[0] += 1
            clock[1] = 0
            if clock[0] >= 24:
                clock[0] = 0
    return clock  # [hh,mm,ss]


# input Robots
robots = input().split(';')
free_robots = deque()  # name
busy_robots = deque()  # [name, current_time]
init_processing_times = {}  # name : processing_time

for r in robots:
    name, seconds = r.split('-')
    free_robots.append(name)  # deque
    init_processing_times[name] = int(seconds)  # dict

# input start_time
start_time = [int(x) for x in input().split(':')]  # [hh,mm,ss]

# input products
products = deque()
while True:
    product = input()
    if product == 'End':
        break
    products.append(product)

while products:
    # product is coming from the line each second
    start_time = plus_one_second(start_time)
    product = products.popleft()  # <-

    if free_robots:  # there are free robots
        robot_name = free_robots.popleft()  # <-
        robot_time = init_processing_times[robot_name]
        busy_robots.append([robot_name, robot_time])  # <+

        # log record
        time = f'[{start_time[0]:02d}:{start_time[1]:02d}:{start_time[2]:02d}]'
        print(f'{robot_name} - {product} {time}')
    else:
        # there is not a free robot
        products.append(product)  # <+

    # test if some robot has finished -> move it to free robots
    for robot in busy_robots:
        robot[1] -= 1
        if robot[1] <= 0:
            name = robot[0]
            free_robots.append(name)  # <+
    busy_robots = [robot for robot in busy_robots if robot[1] > 0]

# ??? защо освободен робот се добавя с append към свободните роботи.
# Така не се ли пренарежда началният ред на роботите?
