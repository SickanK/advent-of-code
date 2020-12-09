import math
import re
from tools.input import Input, strToArr, strToInt, intToStr, arrToStr, newlineParse

i = Input(2020, 9).getData()
# i = Input(2020, 9).getFromExample()


def PartOne(info, step=25):
    info = strToArr(info)
    info = strToInt(info)

    startIndex = step
    currentNum = info[startIndex]
    isSum = False
    for i in range(startIndex, len(info)):
        currentNum = info[i]
        for j in range(i-startIndex, i):
            for u in range(i-startIndex, i):
                if(info[j] + info[u] == info[i]):
                    isSum = True
        if(isSum):
            isSum = False
        else:
            break

    return currentNum


def sumOfRange(arr, start, end):
    total = 0
    for i in range(start, end):
        total += arr[i]
    return total


def PartTwo(info):
    noParseInfo = info
    info = strToArr(info)
    info = strToInt(info)

    nst = PartOne(noParseInfo, 25)
    r, i, j = [], 0, 0
    while i < len(info):
        if(sumOfRange(info, i, j) < nst):
            j += 1
        elif(sumOfRange(info, i, j) > nst):
            i += 1
        else:
            for u in range(i, j):
                r.append(info[u])
            break

    r = sorted(r)
    return r[0] + r[len(r)-1]


# print(i)
print(PartOne(i))
print(PartTwo(i))
