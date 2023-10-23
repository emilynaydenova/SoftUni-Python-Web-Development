def even_odd_filter(**odd_even):
    dd = {}
    if 'odd' in odd_even:
        dd['odd'] = [x for x in odd_even['odd'] if x % 2 == 1]

    if 'even' in odd_even:
        dd['even'] = [x for x in odd_even['even'] if x % 2 == 0]

    dd = dict(sorted(dd.items(), key=lambda item: len(item[1])))

    return dd


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))

print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
