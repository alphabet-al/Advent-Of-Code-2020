""" 
--- Day 11: Seating System ---
Your plane lands with plenty of time to spare. The final leg of your journey is a ferry that goes directly to the tropical island where you can
 finally start your vacation. As you reach the waiting area to board the ferry, you realize you're so early, nobody else has even arrived yet!

By modeling the process people use to choose (or abandon) their seat in the waiting area, you're pretty sure you can predict the best place to sit.
 You make a quick map of the seat layout (your puzzle input).

The seat layout fits neatly on a grid. Each position is either floor (.), an empty seat (L), or an occupied seat (#). For example, the initial seat
 layout might look like this:

L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
Now, you just need to model the people who will be arriving shortly. Fortunately, people are entirely predictable and always follow a simple set of rules.
 All decisions are based on the number of occupied seats adjacent to a given seat (one of the eight positions immediately up, down, left, right, or diagonal
  from the seat). The following rules are applied to every seat simultaneously:

If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
Otherwise, the seat's state does not change.

Floor (.) never changes; seats don't move, and nobody sits on the floor.

After one round of these rules, every seat in the example layout becomes occupied:

#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##
After a second round, the seats with four or more occupied adjacent seats become empty again:

#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##
This process continues for three more rounds:

#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##
#.#L.L#.##
#LLL#LL.L#
L.L.L..#..
#LLL.##.L#
#.LL.LL.LL
#.LL#L#.##
..L.L.....
#L#LLLL#L#
#.LLLLLL.L
#.#L#L#.##
#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##

At this point, something interesting happens: the chaos stabilizes and further applications of these rules cause no seats to change state! Once people 
stop moving around, you count 37 occupied seats.

Simulate your seating area by applying the seating rules repeatedly until no seats change state. How many seats end up occupied? 

--- Part Two ---
As soon as people start to arrive, you realize your mistake. People don't just care about adjacent seats - they care about the first seat they can see 
in each of those eight directions!

Now, instead of considering just the eight immediately adjacent seats, consider the first seat in each of those eight directions. For example, the empty 
seat below would see eight occupied seats:

.......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#.....
The leftmost empty seat below would only see one empty seat, but cannot see any of the occupied ones:

.............
.L.L.#.#.#.#.
.............
The empty seat below would see no occupied seats:

.##.##.
#.#.#.#
##...##
...L...
##...##
#.#.#.#
.##.##.
Also, people seem to be more tolerant than you expected: it now takes five or more visible occupied seats for an occupied seat to become empty 
(rather than four or more from the previous rules). The other rules still apply: empty seats that see no occupied seats become occupied, seats 
matching no rule don't change, and floor never changes.

Given the same starting layout as above, these new rules cause the seating area to shift around as follows:

L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##
#.LL.LL.L#
#LLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLLL.L
#.LLLLL.L#
#.L#.##.L#
#L#####.LL
L.#.#..#..
##L#.##.##
#.##.#L.##
#.#####.#L
..#.#.....
LLL####LL#
#.L#####.L
#.L####.L#
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##LL.LL.L#
L.LL.LL.L#
#.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLL#.L
#.L#LL#.L#
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.#L.L#
#.L####.LL
..#.#.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.LL.L#
#.LLLL#.LL
..#.L.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#
Again, at this point, people stop shifting around and the seating area reaches equilibrium. Once this occurs, you count 26 occupied seats.

Given the new visibility method and the rule change for occupied seats becoming empty, once equilibrium is reached, how many seats end up occupied?

"""

def occupado(data, los = False):
    current_map = data[:]
    old_map = current_map[:]
    old_occupied_seat_count = 0
    current_occupied_seat_count = None
    number_of_rounds = 1

    while old_occupied_seat_count != current_occupied_seat_count:
        adj_dict = init_adjacency(old_map) # function to initialize adjacency map
        current_map = update_map(old_map, current_map, adj_dict, los)
        # print_map(current_map) # debug instruction
        old_occupied_seat_count = current_occupied_seat_count
        current_occupied_seat_count = count_occupied_seats(current_map)
        print('{0} number of occupied seats at the end of round # {1}'\
                         .format(current_occupied_seat_count, number_of_rounds))
        number_of_rounds += 1
        old_map = current_map[:]
        
  

    

def print_map(current_map):
    for i in current_map:
        temp =  ''.join(i)
        print (temp)

def init_adjacency(old_map):
    adj_dict = {}
    row_length = len(old_map)
    col_length = len(old_map[0])

    for row in range(row_length):
        for col in range(col_length):
            if old_map[row][col] == 'L':
                adj_dict[(row, col)] = 0
            elif old_map[row][col] == '#':
                adj_dict[(row, col)] = 1
            elif old_map[row][col] == '.':
                adj_dict[(row, col)] = None

    return adj_dict

    
    
def check_adjacency(y_coor, x_coor, adj_dict):
    adj_pointers = [( -1, -1 ), ( 0, -1 ), ( 1, -1 ), ( -1, 0 ), ( 1, 0 ), ( -1, 1 ), ( 0, 1 ), ( 1, 1 ) ]
    adj_counter = 0

    for i in adj_pointers:
        key_to_lookup = (y_coor + i[0], x_coor + i[1])
        while True:
            
            if key_to_lookup in adj_dict and adj_dict[key_to_lookup] != None:
                adj_counter += adj_dict[key_to_lookup]
                break
            elif key_to_lookup in adj_dict and adj_dict[key_to_lookup] == None:
                key_to_lookup = key_to_lookup[0] + i[0], key_to_lookup[1] + i[1]
                continue     
            elif key_to_lookup not in adj_dict:
                break
                

    return adj_counter



def update_map(old_map, current_map, adj_dict, los):
    row_length = len(current_map)
    col_length = len(current_map[0])

    for row in range(row_length):
        for col in range(col_length):
            adj_counter = check_adjacency(row,col, adj_dict)
            if old_map[row][col] == 'L' and adj_counter == 0:
                current_map[row][col] = '#'
            elif old_map[row][col] == '#' and adj_counter >= 4 and los == False:
                current_map[row][col] = 'L'
            elif old_map[row][col] == '#' and adj_counter >= 5 and los == True:
                current_map[row][col] = 'L'

    return current_map

def count_occupied_seats(current_map):
    count = 0
    for i in current_map:
        # if i == '#':
            count += i.count('#')
    return count
 


if __name__ == "__main__":
    
    input = r'C:\Users\alanv\PythonCode\Projects\Advent of Code 2020\Day11\input.txt'

    with open(input, 'r') as f:
        data = [list(i.strip()) for i in f.readlines()]

        # for i in data:
        #     print(i)


    occupado(data, los = True)
 

    