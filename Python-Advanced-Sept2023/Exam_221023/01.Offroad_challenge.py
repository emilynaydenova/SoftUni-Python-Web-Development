"""
John is quite an avid off-road fan. He bought a new jeep and made
the necessary improvements to it.
John is ready for new off-road adventures and can't wait to get started. In this challenge, he must save his fuel very carefully…
"""
from collections import deque

# All sequences always consist of four elements
COUNT = 4

fuel = deque([int(x) for x in input().split()])
consumption_idx = deque([int(x) for x in input().split()])
altitudes_quantities = deque([int(x) for x in input().split()])


altitude = 0

while fuel:
    f = fuel.pop()
    c = consumption_idx.popleft()
    q = altitudes_quantities.popleft()
    result = f - c

    altitude += 1
    if result >= q:
        print(f'John has reached: Altitude {altitude}')
    else:
        print(f'John did not reach: Altitude {altitude}')
        fuel.appendleft(f)
        altitude -= 1
        break

if altitude == COUNT:
    print("John has reached all the altitudes and managed to reach the top!")

elif len(fuel) == COUNT and altitude == 0:
    print("John failed to reach the top.")
    print("John didn't reach any altitude.")

else:
    print("John failed to reach the top.")
    print("Reached altitudes: ", end='')
    print(", ".join([f'Altitude {n}' for n in range(1, altitude + 1)]))

"""
Test inputs:

200 90 40 100
20 40 30 50
50 60 80 90

40 66 123 100
10 30 70 33
40 55 77 100

199 190 100 100
20 40 30 50
50 60 70 80

"""