file_location = r'C:\Users\alanv\PythonCode\Projects\Advent of Code 2020\Day6\custom_data.txt'

data = [chunk.split() for chunk in open(file_location).read().split("\n\n")]

print(data)
