def group_match(group_list):
    gcount = 0
    for groups in group_list:
        print(groups)
        for i in ch:
            match = True
            for j in range(len(groups)):
                if i in groups[j] and match == True:
                    match = True
                else:
                    match = False
            # print(i, gcount)
            if match == True:
                gcount += 1
                print(i, gcount)

    return gcount

data = [['atxmhdzkjgivwcqu', 'conirfdgplhvsa', 'ghbvdefsaniyc'], ['c', 'c', 'cas', 'xc', 'cz'], ['sdxtfzo', 'stfzno'], ['t', 't', 't', 't', 't']]
# data = [['c', 'c', 'cas', 'xc', 'cz']]
# data = [['sdxtfzo', 'stfzno']]
# data = [['t', 't', 't', 't', 't']]



ch = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', \
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 

gcount = group_match(data)

print('Sum of all questions answered "YES" in a group: {0}'.format(gcount))
