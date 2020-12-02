input = r'C:\Users\alanv\PythonCode\Projects\Advent of Code 2020\Day1\input.txt'

with open(input, 'r') as f:
    data = [int(i) for i in f.read().split()]


# print(data)
# data2 = data[1:]
answer = 0
k = 0

for i in data:
    k += 1
    data2 = data[k:]
    for j in data2:
        if i+j == 2020:
            print(i,j)
            answer = i*j
print(answer)