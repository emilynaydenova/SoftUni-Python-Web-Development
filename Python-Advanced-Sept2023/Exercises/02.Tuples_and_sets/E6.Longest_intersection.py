n = int(input())
longest_set = set()

for _ in range(n):
    (range1, range2) = input().split('-')
    a1, a2 = range1.split(',')
    a = set(range(int(a1), int(a2) + 1))

    b1, b2 = range2.split(',')
    b = set(range(int(b1), int(b2) + 1))

    c = a & b

    if len(c) > len(longest_set):
        longest_set = c

print(f'Longest intersection is {list(longest_set)} with length {len(longest_set)}')
