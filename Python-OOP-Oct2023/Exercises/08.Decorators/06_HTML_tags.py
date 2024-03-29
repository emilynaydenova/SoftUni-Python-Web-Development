def tags(tag):
    def decorator(func):
        def wrapper(*args):
            result = f'<{tag}>{func(*args)}</{tag}>'
            return result
        return wrapper
    return decorator

@tags('ul')
@tags('li')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))


@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))

