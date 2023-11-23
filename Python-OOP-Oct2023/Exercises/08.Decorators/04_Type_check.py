
def type_check(dec_arg):  # type - int,float,str, ....
    def decorator(func):
        def wrapper(func_arg):
            if not isinstance(func_arg, dec_arg):
                return 'Bad Type'
            return func(func_arg)
        return wrapper

    return decorator


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2('Not A Number'))


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
