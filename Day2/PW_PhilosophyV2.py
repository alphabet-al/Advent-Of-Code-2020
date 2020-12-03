import re

input = r'C:\Users\alanv\PythonCode\Projects\Advent of Code 2020\Day2\pw_input.txt'

with open(input, 'r') as f:
    data = [i for i in f.readlines()]

# print(data)
f_data = [re.split('[-: \n]',i) for i in data]
# print(f_data)

def pw_valid(crit):
    pos1 = int(crit[0])
    pos2 = int(crit[1])
    char = str(crit[2])
    string = str(crit[4])

    if string[pos1-1] == char and string[pos2-1] == char:
        return False
    elif string[pos1-1] == char:
        return True
    elif string[pos2-1] == char:
        return True
    else:
        return False
    

count = 0

for i in f_data:
    if pw_valid(i):
        count += 1
    
print(count)