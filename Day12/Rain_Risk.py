""" 
--- Day 12: Rain Risk ---
Your ferry made decent progress toward the island, but the storm came in faster than anyone expected. The ferry needs to take evasive actions!

Unfortunately, the ship's navigation computer seems to be malfunctioning; rather than giving a route directly to safety, it produced extremely 
circuitous instructions. When the captain uses the PA system to ask if anyone can help, you quickly volunteer.

The navigation instructions (your puzzle input) consists of a sequence of single-character actions paired with integer input values. After 
staring at them for a few minutes, you work out what they probably mean:

Action N means to move north by the given value.
Action S means to move south by the given value.
Action E means to move east by the given value.
Action W means to move west by the given value.
Action L means to turn left the given number of degrees.
Action R means to turn right the given number of degrees.
Action F means to move forward by the given value in the direction the ship is currently facing.
The ship starts by facing east. Only the L and R actions change the direction the ship is facing. (That is, if the ship is facing east and the next 
instruction is N10, the ship would move north 10 units, but would still move east if the following action were F.)

For example:

F10
N3
F7
R90
F11
These instructions would be handled as follows:

F10 would move the ship 10 units east (because the ship starts by facing east) to east 10, north 0.
N3 would move the ship 3 units north to east 10, north 3.
F7 would move the ship another 7 units east (because the ship is still facing east) to east 17, north 3.
R90 would cause the ship to turn right by 90 degrees and face south; it remains at east 17, north 3.
F11 would move the ship 11 units south to east 17, south 8.
At the end of these instructions, the ship's Manhattan distance (sum of the absolute values of its east/west position and its north/south position) from
 its starting position is 17 + 8 = 25.

Figure out where the navigation instructions lead. What is the Manhattan distance between that location and the ship's starting position?

"""
def navigate(data):
    start_y, start_x = 0, 0
    curr_y, curr_x = start_y, start_x
    # heading = 'E' # can be 'N', 'E', 'S', or 'W'
    bearing = 90 # bearing is relative to 'N' being 0,  'R' and 'L' changing bearing in pos(R) or neg(L) degrees
    curr_y, curr_x = move_ship(data, curr_y, curr_x, bearing)

    return manhattan(start_y, start_x, curr_y, curr_x)


def move_ship(data, curr_y, curr_x, bearing):
    
    for i in data:
        e1 = i[0]
        e2 = i[1]

        if e1 == 'N' or (e1 == 'F' and bearing == 0):
            curr_y -= e2
        elif e1 == 'S' or (e1 == 'F' and bearing == 180):
            curr_y += e2
        elif e1 == 'E' or (e1 == 'F' and bearing == 90):
            curr_x += e2
        elif e1 == 'W' or (e1 == 'F' and bearing == 270):
            curr_x -= e2
        elif e1 == 'R':
            bearing = (bearing + e2) % 360
        elif e1 == 'L':
            bearing = (bearing - e2) % 360

    return curr_y, curr_x
    
def manhattan(start_y, start_x, curr_y, curr_x):
    abs_y = abs(curr_y - start_y)
    abs_x = abs(curr_x - start_x)

    manhattan = abs_y + abs_x

    return manhattan









import re

if __name__ == "__main__":
    
    input = r'C:\Users\alanv\PythonCode\Projects\Advent of Code 2020\Day12\input.txt'

    with open(input, 'r') as f:
        data = f.read().split()
        split_data = [re.findall('\d+|\D+', i) for i in data]
        
        for i in split_data:
            i[1] = int(i[1])

    print('Manhattan Distance: {0}'.format(navigate(split_data)))


