import numpy
import math
import re

with open("input.txt") as f:
    data = f.readlines()
    times = [int(x) for x in re.findall('[0-9]+', data[0])]
    distances = [int(x) for x in re.findall('[0-9]+', data[1])]


def get_ways_to_win(t, d):
    roots = numpy.roots([1, -t, d])
    win_range = abs(math.ceil(roots[0]) - math.ceil(roots[1]))

    if roots[0] % 1 == 0:
        return win_range - 1
    return win_range


def solve_part_1():
    result = 1
    for i, time in enumerate(times):
        result *= get_ways_to_win(time, distances[i])
    return result


def solve_part_2():
    time = int("".join([str(time) for time in times]))
    distance = int("".join([str(distance) for distance in distances]))
    return get_ways_to_win(time, distance)


print(solve_part_1())
print(solve_part_2())
