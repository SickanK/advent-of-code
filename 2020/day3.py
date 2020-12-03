import math
import re
from tools.input import Input, strToArr, strToInt, intToStr, arrToStr

i = Input(2020, 3).getData()


def PartOne(info):
    info = strToArr(info)

    tempTrees = []
    trees = []
    for i in range(0, len(info)):
        for j in range(0, len(info[i])):
            if(info[i][j] == '#'):
                tempTrees.append(j)
            else:
                tempTrees.append(0)

        trees.append(tempTrees)
        tempTrees = []

    i = 0
    total = 0
    info = info[0:len(info):2]
    for t in list(info):
        if(i >= 31):
            i -= 31

        if(t[i] == '#'):
            total += 1

        i += 1

    return total


def PartTwo(info):
    info = strToArr(info)

    return 0


# print(i)
print(PartOne(i))
print(PartTwo(i))
