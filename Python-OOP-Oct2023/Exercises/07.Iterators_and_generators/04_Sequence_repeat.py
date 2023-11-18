class sequence_repeat:
    def __init__(self, in_sequence, num):
        self.in_sequence = in_sequence
        self.num = num
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.num > 0:
            if self.idx == len(self.in_sequence):
                self.idx = 0
            self.idx += 1
            self.num -= 1
            return self.in_sequence[self.idx - 1]
        raise StopIteration()


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
print()
result = sequence_repeat('I Love Python', 18)
for item in result:
    print(item, end ='')


# My 2021
# class sequence_repeat:
#
#     def __init__(self, in_sequence, num):
#         self.in_sequence = in_sequence
#         self.num = num
#         self.idx = 0
#         self.len_seq = len(in_sequence)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         # if self.len_seq + self.idx < self.num:
#         #     self.idx += self.len_seq
#         #     return self.in_sequence
#         # else:
#         while self.idx < self.num:
#             self.idx += 1
#             return self.in_sequence[(self.idx - 1) % self.len_seq]
#         raise StopIteration()
