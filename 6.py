data = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""".split("\n")

guard_symbol_to_direction = {
    '^': (0, -1),
    'v': (0, 1),
    '>': (1, 0),
    '<': (-1, 0)
}

direction_iteration = {
    (0,-1): (1, 0),
    (1, 0): (0, 1),
    (0, 1): (-1, 0),
    (-1, 0): (0,-1)
}

obstruction_locations = set()
guard_location = None
guard_direction = None

data_height = len(data)
data_width = len(data[0])

for y in range(0, data_height):
    row = data[y]
    for x in range(0, data_width):
        cell = row[x]
        if cell == '#':
            obstruction_locations.add( (x,y) )
        elif cell in guard_symbol_to_direction:
            guard_location = (x,y)
            guard_direction = guard_symbol_to_direction[cell]


visited_locations = set()
visited_locations.add(guard_location)

while True:
    next_location = (guard_location[0] + guard_direction[0], guard_location[1] + guard_direction[1])

    if next_location in obstruction_locations:
        guard_direction = direction_iteration[guard_direction]
        continue

    guard_location = next_location

    if guard_location[0] < 0 or guard_location[1] < 0 or guard_location[0] >= data_width or guard_location[1] >= data_height:
        break

    #print(guard_location)

    visited_locations.add( guard_location )
    
#print(visited_locations)
print(len(visited_locations))

    

