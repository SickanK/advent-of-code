import math
import re
from tools.input import Input, strToArr, strToInt, intToStr, arrToStr

i = Input(2020, 2).getData()


def PartOne(info):
    info = strToArr(info)
    count = 0

    for i in info:
        arr = re.split('\-|\:| ', i)

        minc = int(arr[0])
        maxc = int(arr[1])
        c = arr[2]
        text = list(arr("")[4])
        ccount = 0

        for x in text:
            if(x == c):
                ccount += 1

        if(ccount <= maxc and ccount >= minc):
            count += 1

        ccount = 0

    return count


def PartTwo(info):
    info = strToArr(info)
    count = 0

    for i in info:
        arr = re.split('\-|\:| ', i)

        minc = int(arr[0])
        maxc = int(arr[1])
        c = arr[2]
        text = list(arr("")[4])
        ccount = 0

        for x in range(0, len(text)):
            if(x+1 == minc or x+1 == maxc):
                if(text[x] == c):
                    ccount += 1

        if(ccount > 0 and ccount < 2):
            count += 1

        ccount = 0

    return count


# print(i)
print(PartOne(i))
print(PartTwo(i))
