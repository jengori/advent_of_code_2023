from collections import defaultdict

with open("input.txt") as f:
    initialization_sequence = f.read().split(",")


def hash_algorithm(s):
    i = 0
    val = 0

    while i < len(s):
        val += ord(s[i])
        val = val * 17
        val = val % 256
        i += 1

    return val


boxes = defaultdict(list)

for item in initialization_sequence:
    if "-" in item:
        box = hash_algorithm(item[:-1])
        for lens in boxes[box]:
            if lens[0] == item[:-1]:
                boxes[box].remove(lens)

    if "=" in item:
        box = hash_algorithm(item[:-2])
        labels_in_box = [item[0] for item in boxes[box]]
        if item[:-2] not in labels_in_box:
            boxes[box].append([item[:-2], int(item[-1])])
        else:
            boxes[box][labels_in_box.index(item[:-2])][1] = int(item[-1])

total_focussing_power = 0
for key in boxes.keys():
    for lens in boxes[key]:
        focussing_power = (key+1)*lens[1]*(boxes[key].index(lens) + 1)
        total_focussing_power += focussing_power

print(total_focussing_power)
