from collections import deque


data = [1,5,7,6,2,3,9,8,4]
# data = [3,8,9,1,2,5,4,6,7]
cont = deque()
temp = []
destination_cup = None
moves = 100


for i in data:
    cont.append(i)

current_cup = data[0]

for i in range(moves):
    rotation_count = 0

    if (cont.index(current_cup)) != len(data) - 1:
        rotation_count += cont.index(current_cup) + 1
        cont.rotate(-(cont.index(current_cup) + 1))
       

    for _ in range(3):
        temp.append(cont.popleft())

    for i in range(1, len(data) + 1):
        if (current_cup - i) in cont:
            destination_cup = (current_cup - i)
            break
        if (current_cup - i) <= min(data):
            if max(data) in cont:
                destination_cup = max(data)
                break
            elif (max(data) - i) in cont:
                destination_cup = max(data) - i
                break

    rotation_count += cont.index(destination_cup) + 1
    cont.rotate(-(cont.index(destination_cup) + 1))
    

    for i in reversed(temp):
        cont.appendleft(i)

    temp.clear()

    current_cup = cont[(cont.index(current_cup) + 1)]

    cont.rotate(rotation_count)

print(*cont)

cont.rotate(-(cont.index(1)))

print(*cont)