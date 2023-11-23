# <b><i><u>Hello, Peter, George</u></i></b>

def make_bold(func):
    def wrapper(*args):
        result = f'<b>{func(*args)}</b>'
        return result

    return wrapper


def make_italic(func):
    def wrapper(*arg):
        result = f'<i>{func(*arg)}</i>'
        return result

    return wrapper


def make_underline(func):
    def wrapper(*arg):
        result = f'<u>{func(*arg)}</u>'
        return result

    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


print(greet("Peter"))


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


print(greet_all("Peter", "George"))
