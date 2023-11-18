from itertools import permutations


def possible_permutations(list_elements):
    for per in permutations(list_elements):
        yield list(per)


[print(n) for n in possible_permutations([1, 2, 3])]
