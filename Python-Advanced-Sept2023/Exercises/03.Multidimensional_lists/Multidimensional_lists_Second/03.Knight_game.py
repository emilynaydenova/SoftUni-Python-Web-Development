# Проверяваме кой кон може да вземе най-много коне->
# махаме го и продължаваме да търсим следващия такъв, докато
# не остане кон, който може да вземе друг кон.
# движението е Г-образно

n = int(input())
# initialize chess desk
a = [[ch for ch in input()] for _ in range(n)]

deleted = 0  # K -> 0
# Knight(кон) is moving in the shape of L
points = [(-1, -2), (1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1)]

while True:
    max_points = 0
    point = [0, 0]
    for i in range(n):
        for j in range(n):
            if a[i][j] == 'K':
                count = 0  # how many Knights can kill
                for pp in points:
                    m = i + pp[0]
                    p = j + pp[1]
                    if 0 <= m < n and 0 <= p < n:
                        if a[m][p] == 'K':
                            count += 1
                        if count > max_points:
                            point = [i, j]
                            max_points = count

    if max_points == 0:
        break
    else:  # delete 'K' with max_points
        x = point[0]
        y = point[1]
        a[x][y] = '0'
        deleted += 1

print(deleted)

