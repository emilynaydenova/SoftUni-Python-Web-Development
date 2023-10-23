n = int(input())
a = [[int(x) for x in input().split()] for _ in range(n)]

sum_prime_diagonal = sum([a[i][i] for i in range(n)])
sum_second_diagonal = sum([a[i][-1-i] for i in range(n)])

print(abs(sum_prime_diagonal - sum_second_diagonal))

