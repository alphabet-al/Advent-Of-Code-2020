'''
--- Day 7: Handy Haversacks ---
You land at the regional airport in time for your next flight. In fact, it looks like you'll even have time to 
grab some food: all flights are currently delayed due to issues in luggage processing.

Due to recent aviation regulations, many rules (your puzzle input) are being enforced about bags and their contents; 
bags must be color-coded and must contain specific quantities of other color-coded bags. Apparently, nobody responsible 
for these regulations considered how long they would take to enforce!

For example, consider the following rules:

light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.

These rules specify the required contents for 9 bag types. In this example, every faded blue bag is empty, 
every vibrant plum bag contains 11 bags (5 faded blue and 6 dotted black), and so on.

You have a shiny gold bag. If you wanted to carry it in at least one other bag, how many different bag colors would be 
valid for the outermost bag? (In other words: how many colors can, eventually, contain at least one shiny gold bag?)

In the above rules, the following options would be available to you:

A bright white bag, which can hold your shiny gold bag directly.
A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
A dark orange bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
A light red bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
So, in this example, the number of bag colors that can eventually contain at least one shiny gold bag is 4.

How many bag colors can eventually contain at least one shiny gold bag? (The list of rules is quite long; make sure you get all of it.)
'''
#######################################################################################################################################
import re

input = r'C:\Users\alanv\PythonCode\Projects\Advent of Code 2020\Day7\bag_data.txt'

with open( input, 'r') as f:
    bag_rules = [chunk.split(' contain ') for chunk in f.read().split('\n')]
    # bag_rules = [[re.sub(r' bag[s. ]+', '', chunk)] for chunk in f.read().split('\n')]

bag_rules_beta = []

for i in bag_rules:
    temp = []
    for j in i:
        # print(j)
        temp.append(re.sub(r' bag[s. ]+', '', j))
        # bag_rules_beta.append([re.sub(r' bag[s. ]+', '', i)])
    bag_rules_beta.append(temp)

# print(bag_rules_beta)

class Bag:
    def __init__(self, color, contents):
        self.color = color
        self.contents = [i.split(' ', 1) for i in re.findall(r'\d\s\w+\s\w+', contents)]
        self.dict = {k.replace(' ', '_'):int(v) for v,k in self.contents}

    def __repr__(self):
        return '{0}'.format(self.color)

    def search(self, query):
        if query in self.dict.keys():
            return self.color

twilight = Bag('rainbow', '2 striped silver, 4 mirrored maroon, 5 shiny gold, 1 dotted gold')

# print(twilight.contents)
# print(twilight.dict)
bags_in_bags = []
# bags_in_bags.append(twilight.search('shiny_gold'))
# print(bags_in_bags)

bag_list = [Bag(i.replace(' ','_'),j) for i,j in bag_rules_beta]
# print(bag_list)

print(bag_list[0].color)

'''
def primary_baglist(bags):
    for i in bags:
        # print(i[0])
        i[0] = i[0].replace(' ', '_')
        bag_list.append(i[0])

primary_baglist(bag_rules_beta)

def pop_bags(bl):
    for i in bl:
        i = Bag('rainbow', '2 striped silver, 4 mirrored maroon, 5 shiny gold, 1 dotted gold')
        print(dark_maroon.color)

pop_bags(bag_list)
'''