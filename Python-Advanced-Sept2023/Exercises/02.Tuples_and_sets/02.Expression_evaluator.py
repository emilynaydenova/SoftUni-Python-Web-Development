import math
from collections import deque

expression = input().split()
stack = deque()

for el in expression:
    if el in ['+', '-', '*', '/']:

        if len(stack) > 1:
            res = stack.popleft()

            if el == '+':
                while stack:
                    res += stack.pop()
            elif el == '-':
                while stack:
                    res -= stack.popleft()
            elif el == '*':
                while stack:
                    res *= stack.popleft()
            elif el == '/':
                while stack:
                    res /= stack.popleft()
                res = math.floor(res)

            stack.append(res)
    else:
        stack.append(int(el))

print(stack.pop())
