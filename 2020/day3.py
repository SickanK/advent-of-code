
import math
import re
from tools.input import Input, strToArr, strToInt, intToStr, arrToStr

i = Input(2020, 3).getData()


def PartOne(info, right=3, down=1):
    info = strToArr(info)

    i, total, info = 0, 0, info[0:len(info):down]
    for t in list(info):
        if(i >= len(t)):
            i -= len(t)

        if(t[i] == '#'):
            total += 1
        i += right

    return total


def PartTwo(info):
    t1 = PartOne(info, 1, 1)
    t2 = PartOne(info, 3, 1)
    t3 = PartOne(info, 5, 1)
    t4 = PartOne(info, 7, 1)
    t5 = PartOne(info, 1, 2)

    return t1 * t2 * t3 * t4 * t5


# print(i)
print(PartOne(i))
print(PartTwo(i))
