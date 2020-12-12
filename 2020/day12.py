import timeit
import math
import re
from tools.input import Input, strToArr, strToInt, intToStr, arrToStr, newlineParse

i = Input(2020, 12).getData()
# i = Input(2020, 12).getFromExample()


def PartOne(info):
    info = strToArr(info)
    directions = ["E", "S", "W", "N"]
    instructions = {"E": [1, 0], "S": [0, 1],
                    "W": [-1, 0], "N": [0, -1], "R": 1, "L": -1}
    direction = 0
    vector = [0, 0]

    for i in info:
        arguments = re.findall(r"[a-zA-Z]|[\d]*", i)
        if(re.match(r"[ESWN]", i)):
            vector[0] += instructions[arguments[0]][0]*int(arguments[1])
            vector[1] += instructions[arguments[0]][1]*int(arguments[1])
        elif(re.match(r"[RL]", i) != None):
            direction += instructions[arguments[0]]*(int(arguments[1])/90)
            direction = int((direction+4) % 4)
        else:
            dire = directions[direction]
            vector[0] += instructions[dire][0]*int(arguments[1])
            vector[1] += instructions[dire][1]*int(arguments[1])

    return abs(vector[0]) + abs(vector[1])


def PartTwo(info):
    info = strToArr(info)
    instructions = {"E": [1, 0], "S": [0, 1],
                    "W": [-1, 0], "N": [0, -1], "R": 1, "L": -1}
    ship = [0, 0]
    waypoint = [10, -1]

    for i in info:
        arguments = re.findall(r"[a-zA-Z]|[\d]*", i)
        if(re.match(r"[ESWN]", i)):
            waypoint[0] += instructions[arguments[0]][0]*int(arguments[1])
            waypoint[1] += instructions[arguments[0]][1]*int(arguments[1])
        elif(re.match(r"[RL]", i) != None):
            direction = int(instructions[arguments[0]]*(int(arguments[1])/90))
            savedWaypoint = [*waypoint]

            if(direction == -1):
                direction = 3
            elif(direction == -3):
                direction = 1

            if(direction == 1):
                waypoint[0] = savedWaypoint[1]*-1
                waypoint[1] = savedWaypoint[0]
            elif(abs(direction) == 2):
                waypoint[0] *= -1
                waypoint[1] *= -1
            elif(direction == 3):
                waypoint[0] = savedWaypoint[1]
                waypoint[1] = savedWaypoint[0]*-1
        else:
            ship[0] += waypoint[0] * int(arguments[1])
            ship[1] += waypoint[1] * int(arguments[1])
    return abs(ship[0]) + abs(ship[1])


# print("Input: \n", i)
print("--------Results--------")
print("Part 1:", PartOne(i))
print("Part 2:", PartTwo(i))

# Runtime
print("\n--------Runtime--------")
print("Part 1:", str((timeit.timeit(
    f"PartOne(i)", globals=locals(), number=1000))) + "ms")
print("Part 2:", str((timeit.timeit(
    f"PartTwo(i)", globals=locals(), number=1000))) + "ms")
