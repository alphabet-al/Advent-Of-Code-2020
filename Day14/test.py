from itertools import permutations
from itertools import combinations
from random import randint

# for t in permutations(range(10), 10):
#     if t.index(2) < t.index(8) < t.index(3) < t.index(9) < t.index(4) and t.index(5) < t.index(9) < t.index(4) and t.index(2) < t.index(8) < t.index(1):
#         print(t)

# for i in permutations('111010'):
#     if i[1] == 1 and i[2] == 1 and i[3] == 0 and i[4] == 1:

# count = 2
# x = '1'
# for i in range(count):
#     x += '0'
# print(x)
# # for i in permutations('10'):
# #     print(i)
# for i in combinations('10', 2)
#     print(i)

import itertools
count = 2
lst = list(itertools.product([0, 1], repeat=count))
print(lst)
print(lst[1][1])