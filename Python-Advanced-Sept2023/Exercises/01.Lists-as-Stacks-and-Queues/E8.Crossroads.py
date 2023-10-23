# Crossroads
from collections import deque

green_time = int(input())   # seconds -> 1-100
window_time = int(input())  # seconds -> 0-100
cars = deque()
total_cars_passed = 0
is_crash = False

command = input()
while command  != 'END':
    if command != 'green':
        cars.append(command)
    elif command == 'green' and cars:
        current_time = green_time
        is_crash = False
        while cars:
            if current_time <= 0:
                break
            car = cars.popleft()
            if len(car) <= current_time:
                total_cars_passed += 1
                current_time -= len(car)
            elif len(car) <= (current_time + window_time):
                total_cars_passed += 1
                break
            else:
                print('A crash happened!')
                print(f'{car} was hit at {car[current_time + window_time]}.')
                is_crash = True
                break
    if is_crash:
        break
    command = input()
else:
    print('Everyone is safe.')
    print(f'{total_cars_passed} total cars passed the crossroads.')
