import re

input = r'C:\Users\alanv\PythonCode\Projects\Advent of Code 2020\Day18\tdata1.txt'

with open(input, 'r') as f:
    data = f.read().split('\n')

print(data)

pattern_RE_add = re.compile(r'(\d+\s\+\s\d+)')

match = re.search(pattern_RE_add, data[0])

print(match.group(0))

x = match.group(0)
print(x)