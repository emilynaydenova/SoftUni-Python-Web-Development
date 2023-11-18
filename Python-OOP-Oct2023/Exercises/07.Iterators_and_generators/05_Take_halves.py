import unittest


def solution():  # has 3 closures
    # a closure gives you access to an outer function's scope
    # from an inner function.
    def integers():  # generate infinite amount of integers
        num = 1
        while True:
            yield num
            num += 1

    def halves():  # generate halves of integers
        for i in integers():
            yield i / 2

    def take(n, seq):  # take first n of generator seq
        #  when call list(take(...))
        # for _ in range(n):
        #     yield next(seq)

        # when call take(....)
        result = []
        for _ in range(n):
            result.append(next(seq))
        return result

    return (take, halves, integers)  # tuple of referneces




take = solution()[0]
halves = solution()[1]
print(list(take(5, halves())))

take = solution()[0]
halves = solution()[1]
print(take(0, halves()))


take, halves, iii = solution()
print(take(5, halves()))
print(list(take(10, iii())))


