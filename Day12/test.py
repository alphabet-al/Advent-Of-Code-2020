import re

s='f10'

x = re.findall('\d+|\D+', s)

print(x)