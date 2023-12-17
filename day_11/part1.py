from itertools import *

with open("input.txt") as f:
    data = [line.strip() for line in f.readlines()]

expanded = []
for line in data:
    if line == "."*len(line):
        expanded.append(line)
    expanded.append(line)

extra_rows = 0
for i in range(len(data[0])):
    if "".join([row[i] for row in data]) == "."*len(data):
        for j in range(len(expanded)):
            expanded[j] = expanded[j][:i+extra_rows]+'.'+expanded[j][i+extra_rows:]
        extra_rows += 1

galaxies = {}
galaxy_num_generator = count(1)
for i, row in enumerate(expanded):
    for j in range(len(row)):
        if row[j] == "#":
            galaxies[next(galaxy_num_generator)] = [i, j]

galaxy_pairs = list(combinations([n for n in range(1, next(galaxy_num_generator))], 2))
sum_of_path_lengths = 0

for pair in galaxy_pairs:
    path_length = abs(galaxies[pair[0]][0]-galaxies[pair[1]][0]) + abs(galaxies[pair[0]][1]-galaxies[pair[1]][1])
    sum_of_path_lengths += path_length

print(sum_of_path_lengths)
