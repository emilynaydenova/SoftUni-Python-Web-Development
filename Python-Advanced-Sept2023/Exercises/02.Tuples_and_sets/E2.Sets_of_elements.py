n, m = map(int, input().split())
# n,m = tuple([int(x) for x in input().split()])
a = set()
b = set()

[a.add(input()) for _ in range(n)]
[b.add(input()) for _ in range(m)]

c = a & b    # intersection
[print(x) for x in c]
