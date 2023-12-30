import math

with open("input.txt") as f:
    data = f.readlines()
    blank_line = data.index("\n")


workflows = {}
parts = []
result = 0

for n in range(0, blank_line):
    workflows[data[n].strip()[:-1].split("{")[0]] = [item.split(":") if ":" in item else item for item in data[n].strip()[:-1].split("{")[1].split(",")]

for n in range(blank_line+1, len(data)):
    parts.append({"x": int(data[n].strip()[1:-1].split(",")[0][2::]),
                  "m": int(data[n].strip()[1:-1].split(",")[1][2::]),
                  "a": int(data[n].strip()[1:-1].split(",")[2][2::]),
                  "s": int(data[n].strip()[1:-1].split(",")[3][2::])})


for part in parts:
    status = None
    workflow = "in"

    while not status:

        for rule in workflows[workflow]:
            workflow_before_applying_rule= workflow
            if type(rule) == list:
                if "<" in rule[0]:
                    if part[rule[0].split("<")[0]] < int(rule[0].split("<")[1]):
                        workflow = rule[1]

                else:
                    if part[rule[0].split(">")[0]] > int(rule[0].split(">")[1]):
                        workflow = rule[1]

            else:
                workflow = rule

            if workflow == "A":
                status = "A"
            elif workflow == "R":
                status = "R"

            if status or workflow != workflow_before_applying_rule:
                break

    if status == "A":
        result += part["x"] + part["m"] + part["a"] + part["s"]


print(result)
