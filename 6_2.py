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
visited_locations.add((guard_location, guard_direction))

guard_location_start = guard_location
guard_direction_start = guard_direction

while True:
    next_location = (guard_location[0] + guard_direction[0], guard_location[1] + guard_direction[1])

    if next_location in obstruction_locations:
        guard_direction = direction_iteration[guard_direction]
        continue

    guard_location = next_location

    if guard_location[0] < 0 or guard_location[1] < 0 or guard_location[0] >= data_width or guard_location[1] >= data_height:
        break

    #print(guard_location)

    visited_locations.add( (guard_location, guard_direction) )
    
#print(visited_locations)
#print(len(visited_locations))

def check_if_obstruction_creates_loop(obstruction_location):
    if obstruction_location[0] < 0 or obstruction_location[0] >= data_width or obstruction_location[1] < 0 or obstruction_location[1] >= data_height:
        return False

    if obstruction_location in obstruction_locations:
        return False
    
    visited_locations_2 = set()

    guard_location = guard_location_start
    guard_direction = guard_direction_start

    visited_locations_2.add( (guard_location, guard_direction) )
    
    while True:
        next_location = (guard_location[0] + guard_direction[0], guard_location[1] + guard_direction[1])

        if next_location in obstruction_locations or next_location == obstruction_location:
            guard_direction = direction_iteration[guard_direction]
            continue

        guard_location = next_location

        if guard_location[0] < 0 or guard_location[1] < 0 or guard_location[0] >= data_width or guard_location[1] >= data_height:
            return False

        if (guard_location, guard_direction) in visited_locations_2:
            #print( obstruction_location, (guard_location, guard_direction) )
            return True

        #print(guard_location)

        visited_locations_2.add( (guard_location, guard_direction) )

result = set()
for (loc, dr) in visited_locations:
    obstr_loc = (loc[0] + dr[0], loc[1] + dr[1])
    if check_if_obstruction_creates_loop(obstr_loc):
        #print(obstr_loc)
        result.add(obstr_loc)

print(len(result))
