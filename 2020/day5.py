import math
import re
from tools.input import Input, strToArr, strToInt, intToStr, arrToStr

i = Input(2020, 5).getData()
# i = "BFFFBBFRRR,FFFBBBFRRR,BBFFBBFRLL"


def PartOne(info):
    info = strToArr(info)
    highid = 0

    for i in info:
        fbmin = 0
        fbmax = 127
        lrmin = 0
        lrmax = 7
        for x in i:
            if(x == "F"):
                d = fbmax-fbmin
                fbmax -= math.floor(d/2)
            if(x == "B"):
                a = fbmax-fbmin
                fbmin += math.ceil(a/2)
            if(x == "L"):
                s = lrmax-lrmin
                lrmax -= math.floor(s/2)
            if(x == "R"):
                y = lrmax-lrmin
                lrmin += math.ceil(y/2)

        tid = fbmin * 8 + lrmin
        if(tid > highid):
            highid = tid

    return highid


def PartTwo(info):
    info = strToArr(info)
    ids = []

    for i in info:
        fbmin = 0
        fbmax = 127
        lrmin = 0
        lrmax = 7
        for x in i:
            if(x == "F"):
                d = fbmax-fbmin
                fbmax -= math.floor(d/2)
            if(x == "B"):
                a = fbmax-fbmin
                fbmin += math.ceil(a/2)
            if(x == "L"):
                s = lrmax-lrmin
                lrmax -= math.floor(s/2)
            if(x == "R"):
                y = lrmax-lrmin
                lrmin += math.ceil(y/2)
        ids.append(fbmin * 8 + lrmin)

    ids = sorted(ids)
    missing = 0

    for i in range(1, len(ids)-1):
        if(ids[i+1]-1 != ids[i]):
            missing = ids[i] + 1

    return missing


# print(i)
print(PartOne(i))
print(PartTwo(i))
