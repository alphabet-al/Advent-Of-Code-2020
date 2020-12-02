input = r'C:\Users\alanv\PythonCode\Projects\Advent of Code 2020\Day1\input.txt'

with open(input, 'r') as f:
    data = [int(i) for i in f.read().split()]

data.sort()

# print(data)

answer = 0
index = 0

for i in data:
    index += 1
    data2 = data[index:]
    data3 = data[index+1:]
    for j in data2:
        for k in data3:
            if i+j+k == 2020:
                print(i,j,k)
                answer = i*j*k
print(answer)