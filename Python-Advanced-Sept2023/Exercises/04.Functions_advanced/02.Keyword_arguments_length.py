def kwargs_length(**kwargs):
    return len(kwargs)


# Keyword arguments
dictionary = {
    'name': 'Peter',
    'age': 25
}
print(kwargs_length(**dictionary))

dictionary = {}
print(kwargs_length(**dictionary))
