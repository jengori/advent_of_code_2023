def get_rows(line):
    rows = [line]
    curr = line
    cont = True

    while cont:
        next_row = [curr[i+1] - curr[i] for i in range(len(curr) - 1)]
        rows.append(next_row)
        if len(set(next_row)) != 1:
            curr = next_row
        else:
            cont = False

    return rows


def get_next_number(line):
    rows = get_rows(line)[::-1]
    for i in range(len(rows)-1):
        rows[i+1].append(rows[i+1][-1]+rows[i][-1])
    return rows[-1][-1]


def get_previous_number(line):
    rows = get_rows(line)[::-1]
    for i in range(len(rows)-1):
        rows[i+1].insert(0, rows[i+1][0]-rows[i][0])
    return rows[-1][0]


def solve_part_1(file):
    with open(file) as f:
        data = [[int(num) for num in line.split()] for line in f.readlines()]

    result = 0
    for line in data:
        result += get_next_number(line)

    return result


def solve_part_2(file):
    with open(file) as f:
        data = [[int(num) for num in line.split()] for line in f.readlines()]

    result = 0
    for line in data:
        result += get_previous_number(line)

    return result


print(solve_part_1("input.txt"))
print(solve_part_2("input.txt"))
