"""
 --- Day 17: Conway Cubes ---
As your flight slowly drifts through the sky, the Elves at the Mythical Information Bureau at the North Pole contact you. They'd like some help debugging a malfunctioning experimental energy source aboard one of their super-secret imaging satellites.

The experimental energy source is based on cutting-edge technology: a set of Conway Cubes contained in a pocket dimension! When you hear it's having problems, you can't help but agree to take a look.

The pocket dimension contains an infinite 3-dimensional grid. At every integer 3-dimensional coordinate (x,y,z), there exists a single cube which is either active or inactive.

In the initial state of the pocket dimension, almost all cubes start inactive. The only exception to this is a small flat region of cubes (your puzzle input); the cubes in this region start in the specified active (#) or inactive (.) state.

The energy source then proceeds to boot up by executing six cycles.

Each cube only ever considers its neighbors: any of the 26 other cubes where any of their coordinates differ by at most 1. For example, given the cube at x=1,y=2,z=3, its neighbors include the cube at x=2,y=2,z=2, the cube at x=0,y=2,z=3, and so on.

During a cycle, all cubes simultaneously change their state according to the following rules:

If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube becomes inactive.
If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.
The engineers responsible for this experimental energy source would like you to simulate the pocket dimension and determine what the configuration of cubes should be at the end of the six-cycle boot process.

For example, consider the following initial state:

.#.
..#
###
Even though the pocket dimension is 3-dimensional, this initial state represents a small 2-dimensional slice of it. (In particular, this initial state defines a 3x3x1 region of the 3-dimensional space.)

Simulating a few cycles from this initial state produces the following configurations, where the result of each cycle is shown layer-by-layer at each given z coordinate (and the frame of view follows the active cells in each cycle):

Before any cycles:

z=0
.#.
..#
###


After 1 cycle:

z=-1
#..
..#
.#.

z=0
#.#
.##
.#.

z=1
#..
..#
.#.


After 2 cycles:

z=-2
.....
.....
..#..
.....
.....

z=-1
..#..
.#..#
....#
.#...
.....

z=0
##...
##...
#....
....#
.###.

z=1
..#..
.#..#
....#
.#...
.....

z=2
.....
.....
..#..
.....
.....


After 3 cycles:

z=-2
.......
.......
..##...
..###..
.......
.......
.......

z=-1
..#....
...#...
#......
.....##
.#...#.
..#.#..
...#...

z=0
...#...
.......
#......
.......
.....##
.##.#..
...#...

z=1
..#....
...#...
#......
.....##
.#...#.
..#.#..
...#...

z=2
.......
.......
..##...
..###..
.......
.......
.......
After the full six-cycle boot process completes, 112 cubes are left in the active state.

Starting with your given initial configuration, simulate six cycles. How many cubes are left in the active state after the sixth cycle? 

"""
class Cube:

    def __init__(self, y, x, z, w, state = False):
        self.y = y
        self.x = x
        self.z = z
        self.w = w
        self.state = state

    def __str__(self):
        return 'Cube class with {} state'.format(self.state)

    def __repr__(self):
        return 'Cube({},{},{},{})'.format(self.y, self.x, self.z, self.w, self.state)

    def change_state(self):
        self.state = not self.state
        # return self.state





class Space:

    def __init__(self):
        self.dict = {}
        self.old_dict = {}
        self.transition = []

        self.search_area = [ (-1,-1,-1,-1), (0,-1,-1,-1), (1,-1,-1,-1),
                             (-1, 0,-1,-1), (0, 0,-1,-1), (1, 0,-1,-1), # 
                             (-1, 1,-1,-1), (0, 1,-1,-1), (1, 1,-1,-1),

                             (-1,-1, 0,-1), (0,-1, 0,-1), (1,-1, 0,-1),
                             (-1, 0, 0,-1), (0, 0, 0,-1), (1, 0, 0,-1), # Relative W - 1
                             (-1, 1, 0,-1), (0, 1, 0,-1), (1, 1, 0,-1),
                       
                             (-1,-1, 1,-1), (0,-1, 1,-1), (1,-1, 1,-1),
                             (-1, 0, 1,-1), (0, 0, 1,-1), (1, 0, 1,-1), #
                             (-1, 1, 1,-1), (0, 1, 1,-1), (1, 1, 1,-1),
                            
                             (-1,-1,-1, 0), (0,-1,-1, 0), (1,-1,-1, 0),
                             (-1, 0,-1, 0), (0, 0,-1, 0), (1, 0,-1, 0), # 
                             (-1, 1,-1, 0), (0, 1,-1, 0), (1, 1,-1, 0),

                             (-1,-1, 0, 0), (0,-1, 0, 0), (1,-1, 0, 0),
                             (-1, 0, 0, 0),               (1, 0, 0, 0), # Relative W = 0
                             (-1, 1, 0, 0), (0, 1, 0, 0), (1, 1, 0, 0),
                       
                             (-1,-1, 1, 0), (0,-1, 1, 0), (1,-1, 1, 0),
                             (-1, 0, 1, 0), (0, 0, 1, 0), (1, 0, 1, 0), # 
                             (-1, 1, 1, 0), (0, 1, 1, 0), (1, 1, 1, 0),
                           
                             (-1,-1,-1, 1), (0,-1,-1, 1), (1,-1,-1, 1),
                             (-1, 0,-1, 1), (0, 0,-1, 1), (1, 0,-1, 1), # 
                             (-1, 1,-1, 1), (0, 1,-1, 1), (1, 1,-1, 1),

                             (-1,-1, 0, 1), (0,-1, 0, 1), (1,-1, 0, 1),
                             (-1, 0, 0, 1), (0, 0, 0, 1), (1, 0, 0, 1), # Relative W + 1
                             (-1, 1, 0, 1), (0, 1, 0, 1), (1, 1, 0, 1),
                       
                             (-1,-1, 1, 1), (0,-1, 1, 1), (1,-1, 1, 1),
                             (-1, 0, 1, 1), (0, 0, 1, 1), (1, 0, 1, 1), #
                             (-1, 1, 1, 1), (0, 1, 1, 1), (1, 1, 1, 1),
                            ]

    def __str__(self):
        return 'Space class'

    def __repr__(self):
        return 'Space()'


    def create_adj_cubes(self):
        pass


    def ini_cube(self, y, x, z, w, state):
        key = self.coord_to_key(y, x, z, w)
        newCube = Cube(y, x, z, w, state)
        self.dict[key] = newCube


    def coord_to_key(self, y, x, z, w):
        key = '(' + str(y) + ',' + str(x) + ',' + str(z) + str(w) + ')'
        return key


    def adj_search(self, key_val):
        
        for i in self.search_area:
            y = self.dict[key_val].y + i[0]
            x = self.dict[key_val].x + i[1]
            z = self.dict[key_val].z + i[2]
            w = self.dict[key_val].w + i[3]

            key = self.coord_to_key(y,x,z,w)

            if key not in self.old_dict:

                newCube = Cube(y, x, z, w)
                self.dict[key] = newCube

    def check_cubes(self, key_val):

        active_count = 0

        for i in self.search_area:
            y = self.dict[key_val].y + i[0]
            x = self.dict[key_val].x + i[1]
            z = self.dict[key_val].z + i[2]
            w = self.dict[key_val].w + i[3]


            key = self.coord_to_key(y,x,z,w)

            if key not in self.dict:
                pass
            
            else:

                if self.old_dict[key].state == True:
                    active_count += 1
        
        self.cube_eval_state(key_val, active_count)



       


    def cube_eval_state(self, key_val, active_count):

        if self.old_dict[key_val].state == True and (active_count < 2 or active_count > 3):
            self.transition.append(key_val)
            # self.dict[key_val].change_state()
            # self.dict[key_val] = self.dict[key_val].state
        elif self.old_dict[key_val].state == False and active_count == 3:
            self.transition.append(key_val)
            # self.dict[key_val].change_state()
            # self.dict[key_val] = self.dict[key_val].state
            

    def start_cycle(self):
        self.old_dict = self.dict.copy()

        for i in self.old_dict.keys():
            if self.old_dict[i].state is True:
                self.adj_search(i)
        
        self.old_dict = self.dict.copy()

        for i in self.old_dict.keys():
            self.check_cubes(i)





def load_map(data, uni):
    z = w = 0
    
    for row in range(len(data)):
        for column in range(len(data[0])):
            if data[row][column] == '.':
                uni.ini_cube(row, column, z, w, state = False)
            elif data[row][column] == '#':
                uni.ini_cube(row, column, z, w, state = True)    



def tesseract(data, cycle):
    mcu = Space()
    load_map(data, mcu)
    cube_active = 0

    for i in range(cycle):
        mcu.start_cycle()
  
        for i in mcu.transition:
            mcu.dict[i].change_state()
        
        mcu.transition.clear()
        
    for i in mcu.dict.values():
        if i.state == True:
            cube_active += 1
    
    return cube_active, cycle




    



            

if __name__ == "__main__":
    input = r'C:\Users\alanv\PythonCode\Projects\Advent of Code 2020\day17\input.txt'

    with open(input, 'r') as f:
        data = f.read().split('\n')
        cycle_length = 6
        

    a, b = tesseract(data, cycle_length)

    print('{0} Cubes in active state at end of {1} cycle boot process'. format(a, b))