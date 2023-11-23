#https://www.geeksforgeeks.org/class-as-decorator-in-python/

class store_results:
    _FILE_NAME = "results.txt"

    # decorator
    def __init__(self, function):
        self.function = function
        with open(store_results._FILE_NAME, 'w') as file:
            pass

    # wrapper
    def __call__(self, *args):
        with open(store_results._FILE_NAME, 'a') as file:
            func_result = self.function(*args)
            result = f"Function '{self.function.__name__}' was called. " \
                     f"Result: {func_result}\n"
            file.write(result)

@store_results
def add(a, b):
    return a + b

@store_results
def mult(a, b):
    return a * b

add(2, 2)
mult(6, 4)
