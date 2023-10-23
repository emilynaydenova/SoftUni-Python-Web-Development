from collections import deque


def matches(opened, closed):  # matches('[',']') for example
    opens = "([{"
    closers = ")]}"
    return opens.index(opened) == closers.index(closed)


expression = input()
stack_brackets = deque()

is_balanced = 'YES'
for bracket  in expression:
    if bracket in '([{':
        stack_brackets.append(bracket)
    elif bracket in ')]}':
        if len(stack_brackets) == 0:
            is_balanced = 'NO'
            break
        last_saved_bracket = stack_brackets.pop()

        if not matches(last_saved_bracket, bracket):
            is_balanced = 'NO'
            break

if stack_brackets:  # not empty
    is_balanced = 'NO'
print(is_balanced)
