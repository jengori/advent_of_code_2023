with open("input.txt") as f:
    platform = [[char for char in line.strip()] for line in f.readlines()]

for row in platform:
    print(row)

rocks_sliding = True
while rocks_sliding:
    moves = 0
    for i in range(1, len(platform)):
        for j in range(len(platform[i])):
            if platform[i][j] == 'O' and platform[i-1][j] == '.':
                moves += 1
                platform[i][j] = '.'
                platform[i-1][j] = 'O'
    if moves == 0:
        rocks_sliding = False

print()
for row in platform:
    print(row)

total_load = 0
for i in range(len(platform)):
    load = platform[::-1][i].count('O') * (i+1)
    total_load += load

print(total_load)


