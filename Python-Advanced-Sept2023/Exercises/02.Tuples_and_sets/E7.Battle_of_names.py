N = int(input())
odd_numbers = set()
even_numbers = set()

for i in range(N):
    name = input()
    ascii_sum = sum([ord(ch) for ch in name])
    # ascii_sum =
    result = ascii_sum // (i + 1)
    if result % 2 == 0:
        even_numbers.add(result)
    else:
        odd_numbers.add(result)

even_sum = sum(even_numbers)  # a
odd_sum = sum(odd_numbers)    # b

if even_sum == odd_sum:
    s = odd_numbers | even_numbers  # b.union(a)
elif even_sum < odd_sum:
    s = odd_numbers - even_numbers  # b.differnce(a)
else:
    s = odd_numbers ^ even_numbers  # b.symmetric_differnce(a)

print(', '.join([str(x) for x in s]))
