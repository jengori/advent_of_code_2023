from collections import defaultdict

num_red_cubes = 12
num_green_cubes = 13
num_blue_cubes = 14

sum_of_possible_games = 0

with open("input.txt") as f:

    for line in f:
        game_number = line.strip().split(": ")[0].split(" ")[1]
        num_rounds = len(line.split(": ")[1].split("; "))
        game_possible = True
        game_round = 0

        while game_round < num_rounds and game_possible:

            cubes = line.strip().split(": ")[1].split(";")[game_round].split(", ")
            cubes[0] = cubes[0].strip()
            cubes_dict = defaultdict(int)
            for entry in cubes:
                cubes_dict[entry.split(" ")[1]] += int(entry.split(" ")[0])

            if cubes_dict["red"] > 12 or cubes_dict["green"] > 13 or cubes_dict["blue"] > 14:
                game_possible = False

            game_round += 1

        if game_possible:
            sum_of_possible_games += int(game_number)

print(sum_of_possible_games)
