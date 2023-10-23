#
# with list
stack = [x for x in input().split()]
t = [stack.pop() for _ in range(len(stack))]
print(' '.join(t))
#
# #
# #
# #
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
#
# s = Stack()
# [s.push(int(x)) for x in input().split()]
# t = []
# while not s.is_empty():
#     t.append(s.pop())
# print(' '.join([str(x) for x in t]))
#
# # ---------------------

from collections import deque
stack = deque(input().split(' '))
stack.reverse()
print(' '.join(stack))

# d= deque()
# [d.append(int(x)) for x in input().split()]
# d.reverse()
# t =[]
# [t.append(str(x)) for x in d]
# print(' '.join(t))
