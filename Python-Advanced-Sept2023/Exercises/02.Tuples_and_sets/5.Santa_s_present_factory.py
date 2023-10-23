from collections import deque, defaultdict


def get_key_from_value(d, val):
    keys = [k for k, v in d.items() if v == val]
    if keys:
        return keys[0]
    return None


# dictionary key must be of a type that is immutable.
# For example, you can use an integer, float, string, or Boolean
# as a dictionary key.
presents = {
    'Doll': 150,
    'Wooden train': 250,
    'Teddy bear': 300,
    'Bicycle': 400,
}
toys = defaultdict(int)

boxes_of_materials = deque([int(x) for x in input().split()])
magic_levels = deque([int(x) for x in input().split()])

while boxes_of_materials and magic_levels:
    box = boxes_of_materials.pop()
    magic = magic_levels.popleft()

    total_magic = box * magic

    if total_magic < 0:
        boxes_of_materials.append(box + magic)
    elif total_magic > 0:
        if total_magic in presents.values():
            present = get_key_from_value(presents, total_magic)
            toys[present] += 1
        else:
            boxes_of_materials.append(box + 15)
    elif box == 0 or magic == 0:
        if box != 0:
            boxes_of_materials.append(box)
        elif magic != 0:
            magic_levels.appendleft(magic)

if ('Doll' in toys and 'Wooden train' in toys) or \
        ('Teddy bear' in toys and 'Bicycle' in toys):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if boxes_of_materials:
    boxes_of_materials.reverse()
    print(f"Materials left: {', '.join([str(x) for x in boxes_of_materials])}")
if magic_levels:
    print(f"Magic left: {', '.join([str(x) for x in magic_levels])}")

for k, v in sorted(toys.items()):
    print(f'{k}: {v}')
