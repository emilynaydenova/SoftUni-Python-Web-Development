from collections import deque

n, m = [int(x) for x in input().split()]
snake = deque(input())

output = []

# for row in range(n):
#     s = ''
#     for col in range(m):
#         ch = snake.popleft()
#         s += ch
#         snake.append(ch)
#     if row % 2 != 0:
#         s = s[::-1]
#     output.append(s)
# [print(row) for row in output]

for row in range(n):
    output.append([''] * m)
    for col in range(m):
        ch = snake.popleft()
        if row % 2 == 0:
            output[row][col] = ch
        else:
            output[row][-1-col] = ch
        snake.append(ch)
[print(*row,sep='') for row in output]

