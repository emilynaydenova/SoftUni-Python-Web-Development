first_seq = set(int(x) for x in input().split())
second_seq = set(int(x) for x in input().split())

n = int(input())

for _ in range(n):
    a, b, *c = input().split()
    command_line = f'{a} {b}'
    nums = [int(num) for num in c]

    if command_line == 'Check Subset':
        print(first_seq.issubset(second_seq) or second_seq.issubset(first_seq))
    elif command_line == 'Add First':
        first_seq.update(nums)
    elif command_line == 'Add Second':
        second_seq.update(nums)
    elif command_line == 'Remove First':
        first_seq.difference_update(nums)

    elif command_line == 'Remove Second':
        second_seq.difference_update(nums)

s1 = sorted(first_seq)
s2 = sorted(second_seq)
if first_seq:
    print(", ".join([str(x) for x in s1]))
if second_seq:
    print(", ".join([str(x) for x in s2]))


# My first solution
"""
first_seq = set(int(x) for x in input().split())
second_seq = set(int(x) for x in input().split())

n = int(input())

for _ in range(n):
    command_line = input()

    if command_line == 'Check Subset':
        print(first_seq.issubset(second_seq) or second_seq.issubset(first_seq))
    else:
        line = command_line.split()
        nums = [int(num) for num in line[2:]]
        if line[0] == 'Add':
            if line[1] == 'First':
                first_seq.update(nums)
            elif line[1] == 'Second':
                second_seq.update(nums)
        elif line[0] == 'Remove':
            if line[1] == 'First':
                for num in nums:
                    if num in first_seq:
                        first_seq.remove(num)
            elif line[1] == 'Second':
                for num in nums:
                    if num in second_seq:
                        second_seq.remove(num)

s1 = sorted(first_seq)
s2 = sorted(second_seq)
if first_seq:
    print(", ".join([str(x) for x in s1]))
if second_seq:
    print(", ".join([str(x) for x in s2]))
    """
