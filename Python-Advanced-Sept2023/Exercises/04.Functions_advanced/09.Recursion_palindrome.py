def palindrome(word, idx):
    if idx == len(word) // 2:
        return f'{word} is a palindrome'
    if word[idx] != word[-1 - idx]:
        return f'{word} is not a palindrome'
    return palindrome(word, idx + 1)  # next, next,...


print(palindrome("aaa", 0))
print(palindrome("abccba", 0))
print(palindrome("abcba", 0))
print(palindrome("peter", 0))


# def palindrome(word, idx):
#     while idx < len(word) // 2:
#         if not word[idx] == word[-1 - idx]:
#             return f'{word} is not a palindrome'
#         idx += 1
#     return f'{word} is a palindrome'
