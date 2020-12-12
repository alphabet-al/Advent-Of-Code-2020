from itertools import combinations as com
y = [16, 34, 56]
x = [5, 6, 11]
combinations = [com(x,i) for i in range(1, len(x))]
# combinations = []

# for i in range(2, len(x)):
#     y = list(com(x,i))
#     combinations.append(y)

print(combinations)
# y = com(x,2)

# z = [i for i in y]

# print(z)

# print(list(z[0]))

# mod = x + list(z[0])
# print(mod)
for i in combinations:
    for j in i:
        check_list = y + list(j)
        print(check_list)
        