from collections import defaultdict


class Game:

    def __init__(self, s: str):
        """creates a game object from a string of the kind contained in each line of input.txt"""
        self.s = s
        self.round = 0

    def get_game_number(self):
        """returns the number of the game"""
        return int(self.s.strip().split(": ")[0].split(" ")[1])

    def get_num_rounds(self):
        """returns the number of rounds in the game"""
        return len(self.s.split(": ")[1].split("; "))

    def get_cubes_list(self):
        """returns a list of cubes shown in the current game round, e.g. ["red 3", "green 2", "blue 5"]"""
        cubes = self.s.strip().split(": ")[1].split(";")[self.round].split(", ")
        cubes[0] = cubes[0].strip()
        return cubes

    def is_possible(self, cubes_available: dict):
        """returns true if a game is possible using the number of cubes of each color
        contained in cubes_available dict"""
        while self.round < self.get_num_rounds():
            for entry in self.get_cubes_list():
                color = entry.split(" ")[1]
                if int(entry.split(" ")[0]) > cubes_available[color]:
                    return False

            self.round += 1

        return True

    def get_power_of_minimum_set_of_cubes(self):
        """returns the power of the minimum set of cubes that are required for the game"""
        min_cubes_dict = defaultdict(int)

        while self.round < self.get_num_rounds():
            for entry in self.get_cubes_list():
                min_cubes_dict[entry.split(" ")[1]] = max(int(entry.split(" ")[0]), min_cubes_dict[entry.split(" ")[1]])

            self.round += 1

        return min_cubes_dict["red"] * min_cubes_dict["green"] * min_cubes_dict["blue"]


available_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}

sum_of_possible_games = 0

with open("input.txt") as f:
    for line in f:
        game = Game(line)
        if game.is_possible(available_cubes):
            sum_of_possible_games += game.get_game_number()

print(f"The answer to part 1 is {sum_of_possible_games}")

sum_of_powers = 0

with open("input.txt") as f:
    for line in f:
        game = Game(line)
        sum_of_powers += game.get_power_of_minimum_set_of_cubes()

print(f"The answer to part 2 is {sum_of_powers}")
