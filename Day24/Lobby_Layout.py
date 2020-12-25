'''
--- Day 24: Lobby Layout ---
Your raft makes it to the tropical island; it turns out that the small crab was an excellent navigator. You make your way to the resort.

As you enter the lobby, you discover a small problem: the floor is being renovated. You can't even reach the check-in desk until they've finished installing the new tile floor.

The tiles are all hexagonal; they need to be arranged in a hex grid with a very specific color pattern. Not in the mood to wait, you offer to help figure out the pattern.

The tiles are all white on one side and black on the other. They start with the white side facing up. The lobby is large enough to fit whatever pattern might need to appear there.

A member of the renovation crew gives you a list of the tiles that need to be flipped over (your puzzle input). Each line in the list identifies a single tile that needs to be flipped by giving a series of steps starting from a reference tile in the very center of the room. (Every line starts from the same reference tile.)

Because the tiles are hexagonal, every tile has six neighbors: east, southeast, southwest, west, northwest, and northeast. These directions are given in your list, respectively, as e, se, sw, w, nw, and ne. A tile is identified by a series of these directions with no delimiters; for example, esenee identifies the tile you land on if you start at the reference tile and then move one tile east, one tile southeast, one tile northeast, and one tile east.

Each time a tile is identified, it flips from white to black or from black to white. Tiles might be flipped more than once. For example, a line like esew flips a tile immediately adjacent to the reference tile, and a line like nwwswee flips the reference tile itself.

Here is a larger example:

sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew
In the above example, 10 tiles are flipped once (to black), and 5 more are flipped twice (to black, then back to white). After all of these instructions have been followed, a total of 10 tiles are black.

Go through the renovation crew's list and determine which tiles they need to flip. After all of the instructions have been followed, how many tiles are left with the black side up?

Your puzzle answer was 351.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
The tile floor in the lobby is meant to be a living art exhibit. Every day, the tiles are all flipped according to the following rules:

Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white.
Any white tile with exactly 2 black tiles immediately adjacent to it is flipped to black.
Here, tiles immediately adjacent means the six tiles directly touching the tile in question.

The rules are applied simultaneously to every tile; put another way, it is first determined which tiles need to be flipped, then they are all flipped at the same time.

In the above example, the number of black tiles that are facing up after the given number of days has passed is as follows:

Day 1: 15
Day 2: 12
Day 3: 25
Day 4: 14
Day 5: 23
Day 6: 28
Day 7: 41
Day 8: 37
Day 9: 49
Day 10: 37

Day 20: 132
Day 30: 259
Day 40: 406
Day 50: 566
Day 60: 788
Day 70: 1106
Day 80: 1373
Day 90: 1844
Day 100: 2208
After executing this process a total of 100 times, there would be 2208 black tiles facing up.

How many tiles will be black after 100 days?

Answer: 
 

Although it hasn't changed, you can still get your puzzle input.

You can also [Share] this puzzle. 

'''

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

        current_pos = lobby.upd_pos(0,0,0)
        do_instruction(i, lobby, current_pos)

    for i in lobby.floor_map.values():
        if i.state is False:
            count += 1



    return count

def do_instruction(line, lob, current_pos):
 
    for i in line:

        if i == 'e':
            current_pos = lob.upd_pos(current_pos.x + 1, current_pos.y - 1, current_pos.z)
        elif i == 'w':
            current_pos = lob.upd_pos(current_pos.x - 1, current_pos.y + 1, current_pos.z)
        elif i == 'ne':
            current_pos = lob.upd_pos(current_pos.x + 1, current_pos.y, current_pos.z - 1)
        elif i == 'sw':
            current_pos = lob.upd_pos(current_pos.x - 1, current_pos.y, current_pos.z + 1)  
        elif i == 'nw':
            current_pos = lob.upd_pos(current_pos.x, current_pos.y + 1, current_pos.z - 1)
        elif i == 'se':
            current_pos = lob.upd_pos(current_pos.x, current_pos.y - 1, current_pos.z + 1) 

    current_pos.change_state()


if __name__ == "__main__":
    input = r"C:\Users\alanv\PythonCode\Projects\Advent of Code 2020\Day24\input.txt"

    with open(input, 'r') as f:
        data = f.read().split()

        print('{} tiles with black side up'.format(lay_tile(data)))
