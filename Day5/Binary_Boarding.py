def search(code):
    x1, y1, x2, y2 = [0, 0, 7, 127]
    search_row = code[:7]
    search_column = code[-3:]

    for i in search_row:
        m = (y2 - y1) // 2
        if i == 'F':
            y2 = y1 + m
        if i == 'B':
            y1 = y2 - m

    for i in search_column:
        m = (x2 - x1) // 2
        if i == 'L':
            x2 = x1 + m
        if i == 'R':
            x1 = x2 - m

    seat_location = (x1, y1)
    seat_id = seat_location[1] * 8 + seat_location[0]
    
    # print('{0}: row {1}, column {2}, seat ID {3}'.format(code, seat_location[1], seat_location [0], seat_id))

    return seat_id
    
    

input = r'C:\Users\alanv\PythonCode\Projects\Advent of Code 2020\Day5\seat_data.txt'

with open(input, 'r') as f:
    data = [i for i in f.read().split()]

seat_id_list = []

for i in data:
    seat_id_list.append(search(i))

seat_id_list.sort()
min_seat = seat_id_list[0]
max_seat = seat_id_list[-1]

print('Highest seat ID {0}'.format(max_seat))
print('Lowest seat ID {0}'.format(min_seat))

for i in range(min_seat, max_seat):
    if i not in seat_id_list:
        my_seat = i

print('My Seat is ID {0}'.format(my_seat))
