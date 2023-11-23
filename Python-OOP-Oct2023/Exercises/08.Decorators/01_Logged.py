# decorator's arg is a function, that it is decorated

def logged(some_func):    # decorator wrap function
    def wrapper(*args):
        # can do something before call a function
        result = some_func(*args)    # run function
        # do somthing after calling the function
        return f'you called {some_func.__name__}({", ".join([str(a) for a in args])})\n' \
               f'it returned {result}'
       
    return wrapper


@logged
def func(*args):
    return 3 + len(args)

print(func(4, 4, 4))

# ----------

@logged
def sum_func(a, b):
    return a + b

print(sum_func(1, 4))
