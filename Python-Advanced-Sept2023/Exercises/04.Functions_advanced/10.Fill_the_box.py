def fill_the_box(*args):
    finish_idx = args.index('Finish')
    height, length, width, *rest = [int(x) for x in args[:finish_idx]]
    cubes_possible = height * length * width
    current_cubes = 0

    for idx, cub in enumerate(rest):
        if current_cubes + cub < cubes_possible:
            current_cubes += cub
        elif current_cubes + cub >= cubes_possible:
            cub -= cubes_possible - current_cubes
            rest[idx] = cub
            cubes_left = sum(rest[idx:])

            return f"No more free space! You have {cubes_left} more cubes."

    else:
        return f"There is free space in the box. You could put {cubes_possible - current_cubes} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
