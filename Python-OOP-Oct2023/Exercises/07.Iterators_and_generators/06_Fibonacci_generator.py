def fibonacci():
    first_num = 0
    second_num = 1

    while True:
        yield first_num
        first_num, second_num = second_num, (first_num + second_num)


generator = fibonacci()
for i in range(10):
    print(next(generator))
print()
generator = fibonacci()
for i in range(1):
    print(next(generator))

# _____________________

def fibonacci2():
    i = 0
    while True:
        yield fib_n(i)
        i += 1


def fib_n(n):
    if n in (0, 1):
        return n
    return fib_n(n - 1) + fib_n(n - 2)

generator = fibonacci2()
for i in range(7):
    print(next(generator))