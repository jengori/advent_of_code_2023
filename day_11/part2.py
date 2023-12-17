from itertools import *

with open("input.txt") as f:
    data = [line.strip() for line in f.readlines()]

empty_rows = []
for i, line in enumerate(data):
    if line == "."*len(line):
        empty_rows.append(i)

empty_cols = []
for i in range(len(data[0])):
    if "".join([row[i] for row in data]) == "."*len(data):
        empty_cols.append(i)

galaxies = {}
galaxy_num_generator = count(1)
for i, row in enumerate(data):
    for j, item in enumerate(row):
        if row[j] == "#":
            new_row_num = i
            new_col_num = j
            for empty_row in empty_rows:
                if empty_row < i:
                    new_row_num += (1000000-1)
            for empty_col in empty_cols:
                if empty_col < j:
                    new_col_num += (1000000-1)

            galaxies[next(galaxy_num_generator)] = [new_row_num, new_col_num]

galaxy_pairs = list(combinations([n for n in range(1, next(galaxy_num_generator))], 2))
sum_of_path_lengths = 0


for pair in galaxy_pairs:
    path_length = abs(galaxies[pair[0]][0]-galaxies[pair[1]][0]) + abs(galaxies[pair[0]][1]-galaxies[pair[1]][1])
    sum_of_path_lengths += path_length

print(sum_of_path_lengths)
