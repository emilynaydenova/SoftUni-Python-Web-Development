n = int(input())
usernames = set()

[usernames.add(input()) for _ in range(n)]
print('\n'.join(usernames))
print(*usernames, sep='\n')
# [print(name) for name in usernames]

# one-liner
# print("\n".join({input() for _ in range(int(input()))}))
