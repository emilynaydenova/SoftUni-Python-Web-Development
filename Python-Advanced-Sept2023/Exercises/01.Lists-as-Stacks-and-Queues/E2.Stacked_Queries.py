from collections import deque


def f1(s, *arg):
    s.append(int(arg[0]))


def f2(s):
    if s:
        s.pop()


def f3(s):
    if s:
        print(max(s))


def f4(s):
    if s:
        print(min(s))


ops = {
    "1": f1,
    "2": f2,
    "3": f3,
    "4": f4,
}

n = int(input())
stack = deque()

for _ in range(n):
    action, *args = input().split()
    # call a function from ops
    ops[action](stack, *args)

# print in reverse order
print(', '.join([str(stack.pop()) for _ in range(len(stack))]))


#
# if action == '1':
#     stack.append(int(args[0]))
# elif action == '2' and stack:
#     stack.pop()
# elif action == '3' and stack:
#     print(max(stack))
# elif action == '4' and stack:
#     print(min(stack))


# python 3.10
# match action:
#     case "1":
#         stack.append(int(args[0]))
#     case "2":
#         if stack:
#             stack.pop()
#     case "3":
#         if stack:
#             print(max(stack))
#     case "4":
#         if stack:
#             print(min(stack))
#     case _:
#         continue
# ------------------------
#
# class Stack:  # on the right
#     def __init__(self):
#         self.stack_list = []
#
#     def is_empty(self):
#         return len(self.stack_list) == 0
#
#     def push(self, value):
#         self.stack_list.append(value)
#
#     def pop(self):
#         return self.stack_list.pop()
#
# n = int(input())
# s = Stack()
# for _ in range(n):
#     command = input().split()
#     action = command[0]
#     if action == '1':
#         s.push(int(command[1]))
#     elif action == '2' and not s.is_empty():
#         s.pop()
#     elif action == '3' and not s.is_empty():
#         print(max(s.stack_list))
#     elif action == '4' and not s.is_empty():
#         print(min(s.stack_list))
#
# t = []
# while not s.is_empty():
#     t.append(str(s.pop()))
# print(', '.join(t))
#
#
