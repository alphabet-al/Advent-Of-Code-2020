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

--- Part Two ---
It's getting pretty expensive to fly these days - not because of ticket prices, but because of the ridiculous number of bags you need to buy!

Consider again your shiny gold bag and the rules from the above example:

faded blue bags contain 0 other bags.
dotted black bags contain 0 other bags.
vibrant plum bags contain 11 other bags: 5 faded blue bags and 6 dotted black bags.
dark olive bags contain 7 other bags: 3 faded blue bags and 4 dotted black bags.
So, a single shiny gold bag must contain 1 dark olive bag (and the 7 bags within it) plus 2 vibrant plum bags (and the 11 bags within 
each of those): 1 + 1*7 + 2 + 2*11 = 32 bags!

Of course, the actual rules have a small chance of going several levels deeper than this example; be sure to count all of the bags, 
even if the nesting becomes topologically impractical!

Here's another example:

shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
In this example, a single shiny gold bag must contain 126 other bags.

How many individual bags are required inside your single shiny gold bag?

'''
#######################################################################################################################################
import re

input = r'C:\Users\alanv\PythonCode\Projects\Advent of Code 2020\Day7\bag_data.txt'

with open( input, 'r') as f:
    bag_rules = [chunk.split(' contain ') for chunk in f.read().split('\n')]

bag_rules_beta = []

for i in bag_rules:
    temp = []
    for j in i:
        temp.append(re.sub(r' bag[s. ]+', '', j))
    bag_rules_beta.append(temp)

class Bag:
    def __init__(self, color, contents):
        self.color = color
        self.contents = [i.split(' ', 1) for i in re.findall(r'\d\s\w+\s\w+', contents)]
        self.dict = {k.replace(' ', '_'):int(v) for v,k in self.contents}

    def __repr__(self):
        return '{0}'.format(self.color)

    def search(self, query):
        if str(query) in self.dict.keys():
            return self.color

    def look_in_bag(self):
        return self.dict.items()


# code to instantiate all bag colors in bag_rules_beta.
bag_list = [Bag(i.replace(' ','_'),j) for i,j in bag_rules_beta]

def search_all_bags(searchq):
    bags_in_bags = [searchq]
    bag_brain = []
    # count = 0
   
    while len(bags_in_bags) != 0:
        bags_in_bags_in_bags = bags_in_bags
        bags_in_bags = []
 
        for i in bags_in_bags_in_bags:
            for j in bag_list:
                if j.search(i):
                    if j not in bag_brain:
                        bags_in_bags.append(j)
                        bag_brain.append(j)
                    else:
                        continue

    return len(bag_brain)
  
print(search_all_bags('shiny_gold'))

def how_many_in_a_bag(q, qty):
    bag_of_holding = []
    bag_processing = [(q, qty)]
    bag_check = 1
      
    while len(bag_processing) != 0: 
        bag_proc_deuce = bag_processing
        bag_processing = []
          
        for k,v in bag_proc_deuce:    
            for i in bag_list:
                if str(i) == k:
                    for j,m in i.look_in_bag():
                        # if j not in bag_of_holding:
                            bag_processing.append((j,v*m))
                            bag_of_holding.append((j,(v*m)))                            
    count = 0
    for i in bag_of_holding:
        count += i[1]
    return count

print(how_many_in_a_bag('shiny_gold', 1))