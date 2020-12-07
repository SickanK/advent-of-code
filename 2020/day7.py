import math
import re
import os
import requests as req
from os.path import join, dirname
from tools.input import Input, strToArr, strToInt, intToStr, arrToStr, newlineParse

i = Input(2020, 7).getData()
i = Input(2020, 7).getFromExample()


def PartOne(info):
    info = strToArr(info)
    # info = newlineParse(info)

    sa = []
    res = []

    for i in info:
        sa.append(i.split("contain"))

    pa = []
    tempPa = []
    for s in sa:
        if(len(s) < 2):
            tempPa.append(s[0])
        else:
            pa.append(tempPa)
            tempPa = []
            tempPa.append(s[0])
            tempPa.append(s[1])

    pa.append(tempPa)

    containsShiny = []
    tempActive = ""
    for a in pa:
        for o in a:
            if(tempActive == ""):
                tempActive = o
            else:
                r = re.findall(r"shiny gold", o)
                if(len(r) > 0):
                    nTempActive = tempActive[::-1][2::][::-1]
                    containsShiny.append(nTempActive)
        tempActive = ""

    tempActive2 = ""
    c = False
    for _ in range(0, 6):
        for a in pa:
            for o in a:
                if(tempActive2 == ""):
                    tempActive2 = o
                else:

                    for p in containsShiny:
                        r = re.findall(rf"{p}", o)
                        if(len(r) > 0):
                            c = True

                    if(c == True):
                        nTempActive2 = tempActive2[::-1][2::][::-1]
                        containsShiny.append(nTempActive2)
                    c = False
                [res.append(x) for x in containsShiny if x not in res]
            tempActive2 = ""

    return len(res)


def recursiveP2(pa, argument, cts):
    try:
        for a in pa:
            r = re.findall(argument, a[0])
            if(len(r) > 0):
                for o in range(len(a)):
                    u = re.findall(r"no other bag", a[o])
                    if(o > 0 and len(u) == 0):
                        q = re.split(r"\d", a[o])
                        q = q[1][1::][::-1][2::][::-1]
                        num = re.split(r"\D", a[o])
                        cts.append(int(num[1]))
                        for _ in range(int(num[1])):
                            recursiveP2(pa, q, cts)
    except Exception as e:
        print(e)

    return 0


def PartTwo(info):
    info = strToArr(info)

    sa = []

    for i in info:
        sa.append(i.split("contain"))

    pa = []
    tempPa = []
    for s in sa:
        if(len(s) < 2):
            tempPa.append(s[0])
        else:
            pa.append(tempPa)
            tempPa = []
            tempPa.append(s[0])
            tempPa.append(s[1])
    pa.append(tempPa)

    cts = []
    recursiveP2(pa[1::], "shiny gold bags ", cts)

    total = 0
    for i in cts:
        total += i

    return total


# print(i)
print(PartOne(i))
print(PartTwo(i))
