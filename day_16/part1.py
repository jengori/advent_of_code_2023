import pygame

with open("input.txt") as f:
    layout = [[x for x in line.strip()] for line in f.readlines()]
    activated = [["." for n in range(len(layout[0]))] for m in range(len(layout))]
    activated[0][0] = "#"

beams = []
visited = []


class Beam:
    def __init__(self, direction: str, position: list):
        self.position = position
        self.direction = direction
        self.symbol = layout[self.position[0]][self.position[1]]

    def move_right(self):
        if self.position[1] < len(layout[1])-1:
            self.position = [self.position[0], self.position[1]+1]
            self.symbol = layout[self.position[0]][self.position[1]]
            self.modify_behaviour()
            activated[self.position[0]][self.position[1]] = "#"
            visited.append([self.direction, self.position])
        else:
            beams.remove(self)

    def move_left(self):
        if self.position[1] > 0:
            self.position = [self.position[0], self.position[1]-1]
            self.symbol = layout[self.position[0]][self.position[1]]
            self.modify_behaviour()
            activated[self.position[0]][self.position[1]] = "#"
            visited.append([self.direction, self.position])
        else:
            beams.remove(self)

    def move_up(self):
        if self.position[0] > 0:
            self.position = [self.position[0]-1, self.position[1]]
            self.symbol = layout[self.position[0]][self.position[1]]
            self.modify_behaviour()
            activated[self.position[0]][self.position[1]] = "#"
            visited.append([self.direction, self.position])
        else:
            beams.remove(self)

    def move_down(self):
        if self.position[0] < len(layout)-1:
            self.position = [self.position[0]+1, self.position[1]]
            self.symbol = layout[self.position[0]][self.position[1]]
            self.modify_behaviour()
            activated[self.position[0]][self.position[1]] = "#"
            if [self.direction, self.position] in visited:
                beams.remove(self)
            else:
                visited.append([self.direction, self.position])
        else:
            beams.remove(self)

    def modify_behaviour(self):
        # if the beam encounters a ".", do nothing
        if self.symbol == ".":
            pass

        #  if the beam encounters a "-"
        elif self.symbol == "-":
            # if the beam is travelling left or right, do nothing
            if self.direction in ["L", "R"]:
                pass
            # if the beam is travelling upwards or downwards:
            else:
                if self.position[1] == 0:
                    self.direction = "R"
                elif self.position[1] == len(layout[0])-1:
                    self.direction = "L"
                else:
                    self.direction = "L"
                    new_beam = Beam("R", self.position)
                    beams.append(new_beam)

        #  if the beam encounters a "|"
        elif self.symbol == "|":
            # if the beam is travelling upwards or downwards, do nothing
            if self.direction in ["U", "D"]:
                pass
            # if the beam is travelling left or right:
            else:
                if self.position[0] == 0:
                    self.direction = "D"
                elif self.position[0] == len(layout)-1:
                    self.direction = "U"
                else:
                    self.direction = "U"
                    new_beam = Beam("D", self.position)
                    beams.append(new_beam)

        #  if the beam encounters a "\"
        elif self.symbol == "\\":
            if self.direction == "R":
                self.direction = "D"
            elif self.direction == "L":
                self.direction = "U"
            elif self.direction == "U":
                self.direction = "L"
            elif self.direction == "D":
                self.direction = "R"

        #  if the beam encounters a "/"
        elif self.symbol == "/":
            if self.direction == "R":
                self.direction = "U"
            elif self.direction == "L":
                self.direction = "D"
            elif self.direction == "U":
                self.direction = "R"
            elif self.direction == "D":
                self.direction = "L"


initial_beam = Beam("R", [0, 0])
beams.append(initial_beam)
visited.append([initial_beam.direction, initial_beam.position])

pygame.init()
width = 5*110
height = 5*110
fps = 40
clock = pygame.time.Clock()

window = pygame.display.set_mode((width, height))

cont = True

while cont:

    window.fill("midnightblue")

    for place in visited:
        pygame.draw.rect(window, "gold", (5*place[1][0], 5*place[1][1], 5, 5))

    for beam in beams:
        if beam.direction == "R":
            beam.move_right()

        elif beam.direction == "L":
            beam.move_left()

        elif beam.direction == "U":
            beam.move_up()

        else:
            beam.move_down()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cont = False

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()


result = 0
for line in activated:
    for symbol in line:
        if symbol == "#":
            result += 1

print(f"The answer to part 1 is {result}")
