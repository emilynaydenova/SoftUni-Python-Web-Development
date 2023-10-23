numbers = [int(x) for x in input().split()]
positives_sum = sum([x for x in numbers if x >= 0])
negatives_sum = sum([x for x in numbers if x < 0])

print(negatives_sum)
print(positives_sum)
if positives_sum < abs(negatives_sum):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")

# [s2 := s2 + x for x in in_list if x >= 0]
# [s1 := s1 + x for x in in_list if x < 0]

# -----------------
# lecturer's solution
def positive_negative(*args):
    pos_sum = 0
    neg_sum = 0
    for x in args:
        if x >= 0:
            pos_sum += x
        else:
            neg_sum += x
    return pos_sum,neg_sum


nums = [int(x) for x in input().split()]
pos,neg = positive_negative(nums)
print(neg)
print(pos)
if abs(neg) > pos:
    print('The negatives are stronger than the positives')
else:
    print('The positives are stronger than the negatives')
#
# # ---!!!-----------------
# positives = []
# negatives = []
# in_list = [int(x) for x in input().split()]
# [positives.append(x) if x >= 0 else negatives.append(x) for x in in_list]
# s1 = sum(negatives)
# s2 = sum(positives)
# print(s1)
# print(s2)
# if abs(s1) > s2:
#     print('The negatives are stronger than the positives')
# else:
#     print('The positives are stronger than the negatives')
#

# [s2 := s2 + x for x in in_list if x >= 0]
# [s1 := s1 + x for x in in_list if x < 0]