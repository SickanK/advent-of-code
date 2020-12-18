import numpy as np
import timeit
import math
import re
from tools.input import Input, strToArr, strToInt, intToStr, arrToStr, newlineParse

i = Input(2020, 17).getData()
i = Input(2020, 17).getFromExample()


def findValidNeighbours(vec, arr):
    total = 0
    arrMult = [[0, -1], [1, -1], [1, 0], [1, 1],
               [0, 1], [-1, 1], [-1, 0], [-1, -1]]

    for i in range(8):
        tVec = [*vec]
        tVec[0] += arrMult[i][0]
        tVec[1] += arrMult[i][1]
        if(tVec[0] >= 0 and tVec[1] >= 0 and tVec[1] < len(arr) and tVec[0] < len(arr[tVec[1]])):
            cVal = arr[tVec[1]][tVec[0]]
            if(cVal == "#"):
                total += 1
            tVec[0] += arrMult[i][0]
            tVec[1] += arrMult[i][1]
    return total


def PartOne(info):
    # noParseInfo = info
    info = strToArr(info)
    layers = [info]
    cordLen = [len(info[0]), len(info), 0]
    newLayer = [["."*(len(layers[0][0])+12)]*(len(layers[0][0])+12)]

    for _ in range(6):
        for i in enumerate(layers[0]):
            layers[0][i[0]] = f".{i[1]}."

        toAdd = "."*len(layers[0][0])
        layers = [[toAdd, *layers[0], toAdd]]

    layers = [*newLayer, *layers, *newLayer]
    tempLayers = []

    for _ in range(6):
        cordLen[0] += 2
        cordLen[1] += 2
        cordLen[2] += 1
        vec = [0, 0]
        for z in range(len(layers)):
            tempCol = []
            for y in range(len(layers[z])):
                vec[1] = y
                tempRow = []
                for x in range(len(layers[z][y])):
                    vec[0] = x
                    total = 0
                    total += findValidNeighbours(vec, layers[z])

                    if(z+1 < len(layers)):
                        if(layers[z+1][y][x] == "#"):
                            total += 1
                        total += findValidNeighbours(vec,
                                                     layers[z+1])
                    if(z != 0):
                        if(layers[z-1][y][x] == "#"):
                            total += 1
                        total += findValidNeighbours(vec, layers[z-1])

                    if(layers[z][y][x] == "." and total == 3):
                        tempRow.append("#")
                    elif(layers[z][y][x] == "#" and total == 2 or total == 3):
                        tempRow.append("#")
                    elif(layers[z][y][x] == "#"):
                        tempRow.append(".")
                    else:
                        tempRow.append(layers[z][y][x])

                tempCol.append("".join(tempRow))
            tempLayers.append(tempCol)
        layers = [*newLayer, *tempLayers, *newLayer]
        tempLayers = []
    for i in layers:
        for j in enumerate(i):
            print(j[0], j[1])
        print("-----------END------------")

    t = 0
    for i in layers:
        for j in i:
            for y in j:
                if(y == "#"):
                    t += 1

    return t


def PartTwo(info):
    # noParseInfo = info
    info = strToArr(info)
    layers = [info]
    newLayer = [["."*(len(layers[0][0])+12)]*(len(layers[0][0])+12)]

    for _ in range(6):
        for i in enumerate(layers[0]):
            layers[0][i[0]] = f".{i[1]}."

        toAdd = "."*len(layers[0][0])
        layers = [[toAdd, *layers[0], toAdd]]

    layers = [newLayer*6*4, [layers], newLayer*6*4]

    for _ in range(2):
        tempLayers = []
        for w in range(len(layers)):
            tempBefore = []
            for z in range(len(layers[w])):
                tempCol = []
                for y in range(len(layers[w][z])):
                    tempRow = []
                    for x in range(len(layers[w][z][y])):
                        total = 0

                        for wi in range(-1, 2):
                            for zi in range(-1, 2):
                                for yi in range(-1, 2):
                                    for xi in range(-1, 2):
                                        if(xi == zi == yi == wi == 0):
                                            pass
                                        else:
                                            if(w+wi < len(layers) and w+wi >= 0 and z+zi < len(layers[w]) and z+zi >= 0 and y+yi < len(layers[w][z]) and y+yi >= 0 and x+xi < len(layers[w][z][y]) and x+xi >= 0):
                                                if(layers[w+wi][z+zi][y+yi][x+xi] == "#"):
                                                    total += 1

                        if(layers[w][z][y][x] == "." and total == 3):
                            tempRow.append("#")
                        elif(layers[w][z][y][x] == "#" and total != 2 and total != 3):
                            tempRow.append(".")
                        else:
                            tempRow.append(layers[w][z][y][x])

                    tempCol.append("".join(tempRow))
                tempBefore.append(tempCol)
            tempLayers.append(tempBefore)
        layers = [*tempLayers]
        for i in layers:
            for j in i:
                for y in enumerate(j):
                    print(y[0], y[1])
            print("-----------END------------")

    t = 0
    for i in layers:
        for j in i:
            for y in j:
                for x in y:
                    if(x == "#"):
                        t += 1

    return t


print("Input:\n", i)
# print("--------Results--------")
# print("Part 1:", PartOne(i))
print("Part 2:", PartTwo(i))

# Runtime
# print("\n--------Runtime--------")
# print("Part 1:", str((timeit.timeit(
#     f"PartOne(i)", globals=locals(), number=1000))) + "ms")
# print("Part 2:", str((timeit.timeit(
#     f"PartTwo(i)", globals=locals(), number=1000))) + "ms")
