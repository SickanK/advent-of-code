import math
import re
from tools.input import Input, strToArr, strToInt, intToStr, arrToStr, newlineParse

i = Input(2020, 11).getData()
# i = Input(2020, 11).getFromExample()


def PartOne(info):
    info = strToArr(info)

    for i in range(len(info)):
        info[i] = list(info[i])

    for _ in range(100):
        arr = []
        for a in info:
            arr.append([*a])

        for row in range(len(info)):

            for indexOfRow in range(len(info[row])):
                ut = []
                for a in arr:
                    ut.append([*a])
                    adjacentSeats = 0

                if(ut[row][indexOfRow-1] == "#" and indexOfRow > 0):
                    adjacentSeats += 1

                if (indexOfRow < len(ut[row])-1):
                    if(ut[row][indexOfRow+1] == "#"):
                        adjacentSeats += 1

                for y in range(-1, 2):
                    if (((y == 1 and indexOfRow < len(ut[row])-1) or y != 1) and row > 0):
                        if(y != -1):
                            if(ut[row-1][indexOfRow+y] == "#"):
                                adjacentSeats += 1
                        elif(indexOfRow > 0):
                            if(ut[row-1][indexOfRow+y] == "#"):
                                adjacentSeats += 1

                for y in range(-1, 2):
                    if (((y == 1 and indexOfRow < len(ut[row])-1) or y != 1) and row < len(ut)-1):
                        if(y != -1):
                            if(ut[row+1][indexOfRow+y] == "#"):
                                adjacentSeats += 1
                        elif(indexOfRow > 0):
                            if(ut[row+1][indexOfRow+y] == "#"):
                                adjacentSeats += 1

                if(ut[row][indexOfRow] == "L" and adjacentSeats == 0):
                    info[row][indexOfRow] = "#"

                if(ut[row][indexOfRow] == "#" and adjacentSeats >= 4):
                    info[row][indexOfRow] = "L"

    occupiedSeats = 0
    for i in info:
        for j in list(i):
            if(j == "#"):
                occupiedSeats += 1

    return occupiedSeats


def findValidNeighbours(vec, arr):
    total = 0
    arrMult = [[0, -1], [1, -1], [1, 0], [1, 1],
               [0, 1], [-1, 1], [-1, 0], [-1, -1]]
    for i in range(8):
        tVec = [*vec]
        tVec[0] += arrMult[i][0]
        tVec[1] += arrMult[i][1]
        while (tVec[0] >= 0 and tVec[1] >= 0 and tVec[1] < len(arr) and tVec[0] < len(arr[tVec[1]])):
            cVal = arr[tVec[1]][tVec[0]]
            if(cVal != "."):
                if(cVal == "#"):
                    total += 1
                break
            tVec[0] += arrMult[i][0]
            tVec[1] += arrMult[i][1]
    return total


def PartTwo(info):
    info = strToArr(info)
    output = []
    lastOutput = []
    state = []

    for i in info:
        output.append(list(i))
        state.append(list(i))

    while output != lastOutput:
        for i in range(len(output)):
            for j in range(len(output[i])):
                changedVal = output[i][j]
                neighbours = findValidNeighbours([j, i], output)
                if(changedVal == "L" and neighbours == 0):
                    state[i][j] = "#"
                if(changedVal == "#" and neighbours >= 5):
                    state[i][j] = "L"
        lastOutput = [*output]
        for i in range(len(state)):
            output[i] = list("".join(state[i]))

    occupiedSeats = 0
    for i in output:
        for j in list(i):
            if(j == "#"):
                occupiedSeats += 1

    return occupiedSeats


# print(i)
print(PartOne(i))
print(PartTwo(i))
