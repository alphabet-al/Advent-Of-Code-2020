class Toboggan:
    def __init__(self, map, right, down):
        self.map = map
        self.right = right
        self.down = down
        self.current_pos = [0,0] # [y,x] coordinates, y positive down and x positive to right 
        self.width = len(self.map[0])
        self.ht = len(self.map) - 1
        self.trees = []

    def upd_pos(self):
        self.current_pos[0], self.current_pos[1] = [self.current_pos[0] + self.down, self.current_pos[1] + self.right]
        # print(self.current_pos)

    def inspect_current_pos(self):
        self.char = self.map[self.current_pos[0]][self.current_pos[1] % self.width]
        # print(self.char, self.current_pos)
        
        if self.char == '#':
            self.trees.append('X')

    def traverse(self):
        while self.current_pos[0] <= self.ht:
            # print(self.current_pos[0], self.ht)
            self.inspect_current_pos()
            self.upd_pos()
      
    def tree_count(self):
        return len(self.trees)

input = r'C:\Users\alanv\PythonCode\Projects\Advent of Code 2020\Day3\map_data.txt'

with open(input, 'r') as m:
    map = m.read().split()

path1 = Toboggan(map, 1, 1)
path2 = Toboggan(map, 3, 1)
path3 = Toboggan(map, 5, 1)
path4 = Toboggan(map, 7, 1)
path5 = Toboggan(map, 1, 2)

path1.traverse()
path2.traverse()
path3.traverse()
path4.traverse()
path5.traverse()

total = path1.tree_count() * path2.tree_count() * path3.tree_count() * path4.tree_count() * path5.tree_count()
print(total)
