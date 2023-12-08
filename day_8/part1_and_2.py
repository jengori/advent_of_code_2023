import re
import math

nodes = {}

with open("input.txt") as f:
    data = f.readlines()
    rl_instructions = [0 if char == "L" else 1 for char in data[0].strip()]

    for line in data[2:]:
        nums = [x for x in re.findall('[A-Z]+', line)]
        nodes[nums[0]] = (nums[1], nums[2])

# part 1
moves = 1
current_node = nodes['AAA']
instruction_num = 0

while current_node[rl_instructions[instruction_num]] != "ZZZ":

    current_node = nodes[current_node[rl_instructions[instruction_num]]]
    instruction_num = (instruction_num + 1) % len(rl_instructions)
    moves += 1

print(f"The answer to part 1 is {moves}.")

# part 2
ghost_nodes = [nodes[key] for key in nodes.keys() if key[-1] == "A"]

# Some exploratory analysis of the input data, AKA "I wonder if any of these ghosts are following a cyclical pattern?"

# for each ghost, print the first 10 nodes ending in Z that it gets to, and the number of moves it takes to get there

cycle_lengths = []

for i, node in enumerate(ghost_nodes):

    moves_to_z = []

    moves = 1
    instruction_num = 0
    times = 0
    while times < 10:

        node = nodes[node[rl_instructions[instruction_num]]]
        moves += 1
        instruction_num = (instruction_num + 1) % len(rl_instructions)
        if node[rl_instructions[instruction_num]][-1] == "Z":
            moves_to_z.append({"node": node[rl_instructions[instruction_num]], "moves": moves})
            times += 1

    print(f"GHOST {i+1}:")
    for entry in moves_to_z:
        print(entry)

    cycle_length = moves_to_z[0]["moves"]
    cycle_lengths.append(cycle_length)

# Well, would you look at that? Each ghost is moving in a cyclical pattern, only ever visiting one node ending in Z.

print(f"The answer to part 2 is {math.lcm(*cycle_lengths)}.")
