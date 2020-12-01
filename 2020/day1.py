import math
from tools.input import Input, strToArr, strToInt, intToStr, arrToStr

i = Input(2020, 1).getData()


def PartOne(info):
    info = strToArr(info)
    info = strToInt(info)

    for i in info:
        for j in info:
            if(j + i == 2020):
                return i * j
    return 0


def PartTwo(info):
    info = strToArr(info)
    info = strToInt(info)

    for i in info:
        for j in info:
            for x in info:
                if(j + i + x == 2020):
                    return i * j * x
    return 0


print(i)
print(PartOne(i))
print(PartTwo(i))
