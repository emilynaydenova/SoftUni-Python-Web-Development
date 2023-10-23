def age_assignment(*args, **kwargs):
    people = {}
    for name in args:
        if name[0] in kwargs:
            people[name] = kwargs[name[0]]

    people = dict(sorted(people.items()))

    output = []
    for name, age in people.items():
        output.append(f"{name} is {age} years old.")
    return '\n'.join(output)


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
