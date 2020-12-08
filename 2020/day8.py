import math
import re
from tools.input import Input, strToArr, strToInt, intToStr, arrToStr, newlineParse

i = Input(2020, 8).getData()
# i = Input(2020, 8).getFromExample()


def PartOne(info, changeIndex=-1, changeInfo=""):
    info = strToArr(info)
    acc = 0
    i = 0
    knownValues = []

    if(changeIndex != -1):
        print(changeIndex)
        info[changeIndex] = changeInfo

    while i < len(info):
        a = info[i].split(" ")
        if(a[0] == "acc"):
            o = re.split(r"\-|\+", a[1])
            if(a[1][0] == "-"):
                acc -= int(o[1])
            else:
                acc += int(o[1])

        if(a[0] == "jmp"):
            o = re.split(r"\-|\+", a[1])

            if(a[1][0] == "-"):
                i -= int(o[1])
            else:
                i += int(o[1])
        else:
            i += 1

        knownValues.append(i)
        for e in knownValues:
            if knownValues.count(e) > 1:
                return acc

    return acc


def PartTwo(info):
    noParsedInfo = info
    info = strToArr(info)

    i = 0
    changeIndex = -1
    knownValues = []
    changedInfo = [*info]
    restarted = False

    while i < len(changedInfo):
        if(restarted == True):
            restarted = False
            changedInfo = [*info]
            knownValues = []
            for j in range(len(changedInfo)):
                if(j > changeIndex):
                    y = changedInfo[j].split(" ")
                    if(y[0] == "nop"):
                        changedInfo[j] = f"jmp {y[1]}"
                        changeIndex = j
                        break
                    if(y[0] == "jmp"):
                        changedInfo[j] = f"nop {y[1]}"
                        changeIndex = j
                        break

        a = changedInfo[i].split(" ")
        if(a[0] == "jmp"):
            o = re.split(r"\-|\+", a[1])

            if(a[1][0] == "-"):
                i -= int(o[1])
            else:
                i += int(o[1])
        else:
            i += 1

        knownValues.append(i)
        for e in knownValues:
            if knownValues.count(e) > 1:
                restarted = True

    return PartOne(noParsedInfo, changeIndex, changedInfo[changeIndex])


# print(i)
print(PartOne(i))
print(PartTwo(i))
