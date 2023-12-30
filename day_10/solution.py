import pygame
import matplotlib.path
import numpy
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

print(f"The answer to part 1 is {math.floor(len(loop)/2)}")

loop = [(point[0]*2, point[1]*2) for point in loop]
new_loop = []
for i in range(len(loop)-1):
    if loop[i][0]<loop[i+1][0]:
        new_loop.append(loop[i])
        new_loop.append((loop[i][0] + 1, loop[i][1]))

    elif loop[i][0]>loop[i+1][0]:
        new_loop.append(loop[i])
        new_loop.append((loop[i][0] - 1, loop[i][1]))

    elif loop[i][1]>loop[i+1][1]:
        new_loop.append(loop[i])
        new_loop.append((loop[i][0], loop[i][1] - 1))

    elif loop[i][1] < loop[i+1][1]:
        new_loop.append(loop[i])
        new_loop.append((loop[i][0], loop[i][1] + 1))

points = []
for x in range(140):
    for y in range(140):
        if (x*2,y*2) not in new_loop:
            points.append((x*2, y*2))

p = matplotlib.path.Path(numpy.array(new_loop))
contained = list(p.contains_points(numpy.array(points)))

pygame.init()
width = 3*280
height = 3*280

window = pygame.display.set_mode((width, height))

for x in new_loop:
    pygame.draw.rect(window, color="hotpink", rect=(x[0]*3, x[1]*3, 3, 3))

result = 0
for n in range(len(points)):
    if contained[n]:
        result += 1
        pygame.draw.rect(window, color="chartreuse", rect=(points[n][0] * 3, points[n][1] * 3, 3, 3))

print(f"The answer to part 2 is {result}")

continue_game = True


while continue_game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continue_game = False

    pygame.display.flip()

pygame.quit()
