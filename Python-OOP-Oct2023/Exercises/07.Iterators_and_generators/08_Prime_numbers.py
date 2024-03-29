def get_primes(numbers: list):
    for num in numbers:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))

def get_primes(seq):
    for el in seq:
        if el > 1:
            x = 2
            while x < el:
                if el % x == 0:
                    break
                x += 1
            else:
                yield el
