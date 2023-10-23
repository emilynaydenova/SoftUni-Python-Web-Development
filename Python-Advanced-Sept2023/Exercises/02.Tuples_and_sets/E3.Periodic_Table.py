count = int(input())
elements = set()

[elements.update(input().split()) for _ in range(count)]
[print(el) for el in elements]
# for _ in range(count):
#     [elements.add(x) for x in input().split()]
#[print(el) for el in elements]
