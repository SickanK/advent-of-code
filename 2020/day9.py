import math
import re
from tools.input import Input, strToArr, strToInt, intToStr, arrToStr, newlineParse

i = Input(2020, 9).getData()
# i = Input(2020, 9).getFromExample()


def PartOne(info):
    info = strToArr(info)
    info = newlineParse(info)

    return 0


def PartTwo(info):
    noParsedInfo = info
    info = newlineParse(info)

    return 0


print(i)
print(PartOne(i))
print(PartTwo(i))
