with open("input.txt") as f:
    platform = [[char for char in line.strip()] for line in f.readlines()]


def tilt_n(p):
    while True:
        moves = 0
        for i in range(1, len(p)):
            for j in range(len(p[i])):
                if p[i][j] == 'O' and p[i - 1][j] == '.':
                    moves += 1
                    p[i][j] = '.'
                    p[i - 1][j] = 'O'
        if moves == 0:
            return p


def tilt_w(p):
    while True:
        moves = 0
        for i in range(1, len(p[0])):
            for j in range(len(p)):
                if p[j][i] == 'O' and p[j][i-1] == '.':
                    moves += 1
                    p[j][i] = '.'
                    p[j][i-1] = 'O'
        if moves == 0:
            return p


def tilt_s(p):
    p_reversed = p[::-1]
    while True:
        moves = 0
        for i in range(1, len(p)):
            for j in range(len(p[i])):
                if p_reversed[i][j] == 'O' and p_reversed[i - 1][j] == '.':
                    moves += 1
                    p_reversed[i][j] = '.'
                    p_reversed[i - 1][j] = 'O'
        if moves == 0:
            return p_reversed[::-1]


def tilt_e(p):
    p_reversed = [row[::-1] for row in p]
    while True:
        moves = 0
        for i in range(1, len(p[0])):
            for j in range(len(p)):
                if p_reversed[j][i] == 'O' and p_reversed[j][i-1] == '.':
                    moves += 1
                    p_reversed[j][i] = '.'
                    p_reversed[j][i-1] = 'O'
        if moves == 0:
            return [row[::-1] for row in p_reversed]


total_loads = []
for _ in range(100):
    platform = tilt_n(platform)
    platform = tilt_w(platform)
    platform = tilt_s(platform)
    platform = tilt_e(platform)
    total_load = 0
    for i in range(len(platform)):
        load = platform[::-1][i].count('O') * (i + 1)
        total_load += load

    total_loads.append(total_load)

# from observation of repeating pattern in total_loads, I determined that the answer is:
print(total_loads[97 + ((1000000000-98) % 36)])
