def concatenate(*args, **kwargs):
    text = ''.join(args)

    for k, v in kwargs.items():
        if k in text:
            text = text.replace(k, v)
    return text
# replace(old,new)
# All occurrences of the specified phrase will be replaced,
# if nothing else is specified.

print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
