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


result = 0
for item in initialization_sequence:
    result += hash_algorithm(item)

print(result)