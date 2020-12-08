import re
'''
s = '1,55,6,89,2|7,29,44,5,8|767,822,999'

ss = s.split('|')
# print(ss)

x = ['1,55,6,89,2', '7,29,44,5,8', '767,822,999']
list2 = []

for i in x:
    # print(i)
    list2.append([int(i) for i in i.split(',')])

print(list2)

list = [[int(i) for i in ss.split(',')] for ss in s.split('|')]
print(list)
'''

bag_rules = [['dark maroon bags', '2 striped silver bags, 4 mirrored maroon bags, 5 shiny gold bags, 1 dotted gold bag.'],
['dark coral bags', '4 pale blue bags, 3 wavy yellow bags, 4 vibrant tan bags, 3 striped purple bags.'],
['striped aqua bags', '1 pale aqua bag, 2 muted yellow bags, 4 pale maroon bags, 2 shiny coral bags.'],
['wavy coral bags', '4 pale purple bags, 2 bright olive bags.']]

bag_rules_beta = []

for i in bag_rules:
    temp = []
    for j in i:
        # print(j)
        temp.append(re.sub(r' bag[s. ]+', '', j))
        # bag_rules_beta.append([re.sub(r' bag[s. ]+', '', i)])
    bag_rules_beta.append(temp)

print(bag_rules_beta)