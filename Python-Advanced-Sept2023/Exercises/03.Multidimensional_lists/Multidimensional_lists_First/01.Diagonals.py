n = int(input())
matrix = [[int(x) for x in input().split(', ')] for _ in range(n)]

primary_diagonal = [matrix[i][i] for i in range(n)]
secondary_diagonal = [matrix[i][-1-i] for i in range(n)]
sum_of_primary = sum(primary_diagonal)
sum_of_secondary = sum(secondary_diagonal)
print(f'Primary diagonal: {", ".join([str(x) for x in primary_diagonal])}. Sum: {sum_of_primary}')
print(f'Secondary diagonal: {", ".join([str(x) for x in secondary_diagonal])}. Sum: {sum_of_secondary}')
