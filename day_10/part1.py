import math

directions_to_tiles = {"N": ["|", "7", "F", "S"],
                       "E": ["-", "7", "J", "S"],
                       "S": ["|", "J", "L", "S"],
                       "W": ["-", "F", "L", "S"]}


def get_neighbours(tile: tuple):
    neighbours = {}
    if tile[0] > 0:
        neighbours["N"] = (tile[0] - 1, tile[1])
    if tile[1] < len(field[0])-1:
        neighbours["E"] = (tile[0], tile[1]+1)
    if tile[0] < len(field)-1:
        neighbours["S"] = (tile[0]+1, tile[1])
    if tile[1] > 0:
        neighbours["W"] = (tile[0], tile[1]-1)
    return neighbours


with open("input.txt") as f:
    field = [line.strip() for line in f.readlines()]

starting_point = None

for i, line in enumerate(field):
    if 'S' in line:
        starting_point = (i, line.index('S'))


starting_point_neighbours = get_neighbours(starting_point)
loop = [starting_point]


if field[starting_point_neighbours["N"][0]][starting_point_neighbours["N"][1]] in "|7F":
    loop.append(starting_point_neighbours["N"])

elif field[starting_point_neighbours["E"][0]][starting_point_neighbours["E"][1]] in "-7J":
    loop.append(starting_point_neighbours["E"])

elif field[starting_point_neighbours["S"][0]][starting_point_neighbours["S"][1]] in "|JL":
    loop.append(starting_point_neighbours["S"])

elif field[starting_point_neighbours["W"][0]][starting_point_neighbours["W"][1]] in "-FL":
    loop.append(starting_point_neighbours["W"])

previous_tile = loop[0]
current_tile = loop[1]

while current_tile != starting_point:

    current_tile_neighbours = get_neighbours(current_tile)

    for direction in current_tile_neighbours.keys():
        if field[current_tile[0]][current_tile[1]] in directions_to_tiles["NESW"[(("NESW".index(direction))+2) % 4]] \
                and field[current_tile_neighbours[direction][0]][current_tile_neighbours[direction][1]] \
                in directions_to_tiles[direction] \
                and current_tile_neighbours[direction] != previous_tile:
            loop.append(current_tile_neighbours[direction])

    previous_tile = current_tile
    current_tile = loop[-1]

print(math.floor(len(loop)/2))
