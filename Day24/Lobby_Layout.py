import re

class Cell:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.state = True # True = White, False = Black

    def __str__(self):
        return 'Cell ({},{},{}) state is {}'.format(self.x, self.y, self.z, self.state)

    def __repr__(self):
        return 'Cell ({},{},{}) state is {}'.format(self.x, self.y, self.z, self.state)

    def change_state(self):
        self.state = not self.state


class Floor:

    def __init__(self):
        self.floor_map = {}

    def ini(self, x, y, z, key):
        # key = self.coord_to_key(x, y, z)
        newCell = Cell(x, y, z)
        self.floor_map[key] = newCell

        return newCell
        


    def coord_to_key(self, x, y, z):
        key = '(' + str(x) + ',' + str(y) + ',' + str(z) + ')'
        return key


    def upd_pos(self, x, y, z):
        key = self.coord_to_key(x, y, z)

        if key not in self.floor_map:
            newCell = self.ini(x, y, z, key)
            
            return newCell

        else:

            return self.floor_map[key]

def lay_tile(data):
    lobby = Floor()
    split_data = [re.findall(r'se|ne|sw|nw|e|w', i) for i in data]
    
    count = 0

    for i in split_data:
        # print(i)
        current_pos = lobby.upd_pos(0,0,0)
        do_instruction(i, lobby, current_pos)
        # for i in lobby.floor_map.values():
        #     if i.state is False:
        #         print(i)


    for i in lobby.floor_map.values():
        if i.state is False:
            count += 1

    print(count)

def do_instruction(line, lob, current_pos):
 
    for i in line:

        if i == 'e':
            current_pos = lob.upd_pos(current_pos.x + 1, current_pos.y, current_pos.z)
        elif i == 'w':
            current_pos = lob.upd_pos(current_pos.x - 1, current_pos.y, current_pos.z)
        elif i == 'ne':
            current_pos = lob.upd_pos(current_pos.x, current_pos.y, current_pos.z - 1)
        elif i == 'sw':
            current_pos = lob.upd_pos(current_pos.x, current_pos.y, current_pos.z + 1)  
        elif i == 'nw':
            current_pos = lob.upd_pos(current_pos.x, current_pos.y + 1, current_pos.z)
        elif i == 'se':
            current_pos = lob.upd_pos(current_pos.x, current_pos.y - 1, current_pos.z) 

    current_pos.change_state()


if __name__ == "__main__":
    input = r"C:\Users\alanv\PythonCode\Projects\Advent of Code 2020\Day24\t_input.txt"

    with open(input, 'r') as f:
        data = f.read().split()

        # print(data)

        lay_tile(data)