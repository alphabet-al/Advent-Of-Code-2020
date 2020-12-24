import re

data = 'sesenwnenenewseeswwswswwnenewsewsw'

split_data = re.findall(r'se|ne|sw|nw|e|w', data)

print(split_data)