import matplotlib.path
import numpy

with open("input.txt") as f:
    data = [line.strip() for line in f.readlines()]

points = [[0, 0]]
corners = [[0, 0]]

for line in data:
    direction = line.split(" ")[0]
    number = int(line.split(" ")[1])

    if direction == "R":
        for n in range(number):
            points.append([points[-1][0], points[-1][1] + 1])
        corners.append(points[-1])

    elif direction == "L":
        for n in range(number):
            points.append([points[-1][0], points[-1][1] - 1])
        corners.append(points[-1])

    elif direction == "U":
        for n in range(number):
            points.append([points[-1][0] - 1, points[-1][1]])
        corners.append(points[-1])

    elif direction == "D":
        for n in range(number):
            points.append([points[-1][0] + 1, points[-1][1]])
        corners.append(points[-1])

points.pop()
corners.pop()

all_points = []

for x in range(min([point[0] for point in points])+1, max([point[0] for point in points])+1):
    for y in range(min([point[1] for point in points])+1, max([point[1] for point in points])+1):
        if [x, y] not in points:
            all_points.append((x, y))


p = matplotlib.path.Path(numpy.array(corners))
contained = list(p.contains_points(numpy.array(all_points)))

print(contained.count(True) + len(points))
