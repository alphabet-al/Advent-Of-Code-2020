# y = 0
# x = 1
# z = -1

# key = '(' + str(y) + ',' + str(x) + ',' + str(z) + ')'
# print(key)

# dict = {}

# dict[key] = 23

# g = dict['(0,1,-1)']

# print(g)


# state = True
# x = 5

# if state == True and (x < 2 or x > 4):
#     state = False


# print(state)

search_area = [(-1, 1, 1), (0, 1, 1), (1, 1, 1),
               (-1, 0, 1), (0, 0, 1), (1, 0, 1), # Relative Z + 1 
               (-1,-1, 1), (0,-1, 1), (1,-1, 1),

               (-1, 1, 0), (0, 1, 0), (1, 1, 0),
               (-1, 0, 0)       ,     (1, 0, 0), # Relative Z = 0
               (-1,-1, 0), (0,-1, 0), (1,-1, 0),

               (-1, 1,-1), (0, 1,-1), (1, 1,-1),
               (-1, 0,-1), (0, 0,-1), (1, 0,-1), # Relative Z - 1
               (-1,-1,-1), (0,-1,-1), (1,-1,-1),
               ]

for i in search_area:
    print(i[0], i[1], i[2])