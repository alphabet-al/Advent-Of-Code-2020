
class Cube:

    def __init__(self, y, x, z, state = False):
        self.y = y
        self.x = x
        self.z = z
        self.state = state

    def __str__(self):
        return 'Cube class with {} state'.format(self.state)

    def __repr__(self):
        return 'Cube({},{},{},{})'.format(self.y, self.x, self.z, self.state)

    def change_state(self):
        self.state = not self.state
        return self.state





class Space:

    def __init__(self):
        self.dict = {}
        self.old_dict = {}

    def __str__(self):
        return 'Space class'

    def __repr__(self):
        return 'Space()'

    def ini_cube(self, y, x, z, state):
        key = self.coord_to_key(y, x, z)
        newCube = Cube(y, x, z, state)
        self.dict[key] = newCube


    def coord_to_key(self, y, x, z):
        key = '(' + str(y) + ',' + str(x) + ',' + str(z) + ')'
        return key


    def adj_search(self, key_val):

        search_area = [ (-1,-1,-1), (0,-1,-1), (1,-1,-1),
                        (-1, 0,-1), (0, 0,-1), (1, 0,-1), # Relative Z - 1 
                        (-1, 1,-1), (0, 1,-1), (1, 1,-1),

                        (-1,-1, 0), (0,-1, 0), (1,-1, 0),
                        (-1, 0, 0), (0, 0, 0), (1, 0, 0), # Relative Z = 0
                        (-1, 1, 0), (0, 1, 0), (1, 1, 0),
                       
                        (-1,-1, 1), (0,-1, 1), (1,-1, 1),
                        (-1, 0, 1), (0, 0, 1), (1, 0, 1), # Relative Z + 1
                        (-1, 1, 1), (0, 1, 1), (1, 1, 1),
                      ]

        active_count = 0

        for i in search_area:
            y = self.dict[key_val].y + i[0]
            x = self.dict[key_val].x + i[1]
            z = self.dict[key_val].z + i[2]

            key = self.coord_to_key(y,x,z)

            if key not in self.old_dict:

                newCube = Cube(y, x, z)
                self.dict[key] = newCube

            else:

                if self.dict[key] == True:
                    active_count += 1

        return active_count


    def cube_eval_state(self, key_val, active_count):

        if self.dict[key_val].state == True and (active_count < 2 or active_count > 3):
            self.dict[key_val].state = self.dict[key_val].change_state()
            # self.dict[key_val] = self.dict[key_val].state
        elif self.dict[key_val].state == False and active_count == 3:
            self.dict[key_val].state = self.dict[key_val].change_state()
            # self.dict[key_val] = self.dict[key_val].state
            

    def start_cycle(self):
        self.old_dict = self.dict.copy()
        
        for i in self.old_dict.keys():
            active_count = self.adj_search(i)
            self.cube_eval_state(i, active_count)




def load_map(data, uni):
    z = 0
    
    for row in range(len(data)):
        for column in range(len(data[0])):
            if data[row][column] == '.':
                uni.ini_cube(row, column, z, state = False)
            elif data[row][column] == '#':
                uni.ini_cube(row, column, z, state = True)    



def tesseract(data, cycle):
    mcu = Space()
    load_map(data, mcu)
    cube_active = 0

    for i in range(cycle):
        mcu.start_cycle()
        
    for i in mcu.dict.values():
        if i.state == True:
            # print(i)
            cube_active += 1
    
    return cube_active, cycle

###------------------------------------------------------------------------------------

if __name__ == "__main__":
    input = r'C:\Users\alanv\PythonCode\Projects\Advent of Code 2020\day17\input.txt'

    with open(input, 'r') as f:
        data = f.read().split('\n')
        cycle_length = 6
        

    a, b = tesseract(data, cycle_length)

    print('{0} Cubes in active state at end of {1} cycle boot process'. format(a, b))