from shapely import Polygon

with open("input.txt") as f:
    data = [line.strip() for line in f.readlines()]

points = [[0, 0]]
corners = [[0, 0]]
edge_squares = 0

for line in data:
    direction = line.split(" ")[0]
    number = int(line.split(" ")[1])
    edge_squares += number

    if direction == "R":
        corners.append((corners[-1][0], corners[-1][1]+number))

    elif direction == "L":
        corners.append((corners[-1][0], corners[-1][1] - number))

    elif direction == "U":
        corners.append((corners[-1][0] - number, corners[-1][1]))

    elif direction == "D":
        corners.append((corners[-1][0] + number, corners[-1][1]))

polygon = Polygon(corners)
print(polygon.area + edge_squares/2 + 1)
