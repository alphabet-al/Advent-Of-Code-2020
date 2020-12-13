# from itertools import combinations as com

# input = r'C:\Users\alanv\PythonCode\Projects\Advent of Code 2020\Day10\input.txt'

# with open(input, 'r') as f:
#     data = [int(i) for i in f.read().split()]
#     data.sort()

# combinations = [list(com(data,i)) for i in range(1, 5)]

# for i in combinations:
#     print(len(i)) 

       

ef_cache = {}

def expensive_func(num):
    if num in ef_cache:
        return ef_cache[num]

    print("Computing {}....".format(num))
    result = num * num
    ef_cache[num] = result
    return result

result = expensive_func(4)
print(result)

result = expensive_func(10)
print(result)

result = expensive_func(4)
print(result)

result = expensive_func(10)
print(result)

print(ef_cache)