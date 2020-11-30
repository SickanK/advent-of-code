import math
from tools.input import Input, strToArr, strToInt

i = Input(2019, 1).getData()


def PartOne(info):
    info = strToArr(info)
    info = strToInt(info)
    sum = 0
    for i in info:
        sum += math.floor(i/3)-2
    return sum


def PartTwo(info):
    info = strToArr(info)
    info = strToInt(info)
    sum, s = 0, 0

    for i in info:
        s = math.floor(i/3)-2
        while (s >= 0):
            sum += s
            s = math.floor(s/3)-2

    return sum


print(PartOne(i))
print(PartTwo(i))
