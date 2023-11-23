def cache(func):
    def wrapper(arg):
        value = func(arg)
        wrapper.log[arg] = value
        return value

    wrapper.log = {} # new attribute for wrapper
    return wrapper



@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(3)
print(fibonacci.log)

fibonacci(4)
print(fibonacci.log)

# from functools import lru_cache
#
# @lru_cache(maxsize=None)
# def fibonacci(n):
#     if n < 2:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# fibonacci(3)
# print(fibonacci.cache_info())
