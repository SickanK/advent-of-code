import math
import re
from tools.input import Input, strToArr, strToInt, intToStr, arrToStr, newlineParse

i = Input(2020, 6).getData()


def PartOne(info):
    info = strToArr(info)
    info = newlineParse(info)

    arr = []
    tempArr = []
    for a in info:
        if(a == ""):
            arr.append(tempArr)
            tempArr = []
        else:
            tempArr.append(a)
    arr.append(tempArr)
    info = arr

    t1 = 0
    for i in info:
        t2 = []
        for a in i:
            for l in a:
                t2.append(l)
        t1 += len(list(dict.fromkeys(t2)))
        t2 = []

    return t1


def PartTwo(info):
    info = strToArr(info)
    info = newlineParse(info)

    t1 = 0
    t2 = []
    for i in info:
        t2.append(i)

    for l in t2:
        d = list(dict.fromkeys(l))

        if(len(l) == 1):
            t1 += len(l[0])
        elif(len(d) == 1):
            t1 += len(d[0])
        else:
            e = []
            for q in l:
                for x in q:
                    e.append(x)

            de = list(dict.fromkeys(e))
            for f in range(len(list(de))):
                if(e.count(de[f]) == len(l)):
                    t1 += 1

    return t1


# print(i)
print(PartOne(i))
print(PartTwo(i))
