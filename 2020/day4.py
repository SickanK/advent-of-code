import math
import re
from tools.input import Input, strToArr, strToInt, intToStr, arrToStr

i = Input(2020, 4).getData()


def PartOne(info):
    info = strToArr(info)

    print(info)
    arr = []
    tempArr = []
    for a in info:
        if(a == ""):
            arr.append(tempArr)
            tempArr = []
        else:
            tempArr.append(a)
    info = arr

    valid = 0
    for i in info:
        c = 0
        print(i)
        j = " ".join(i)
        j = j.split(":")
        for x in j:
            l = re.findall(r"ecl|iyr|eyr|hgt|hcl|byr|pid", x)
            print(l)
            if(len(l) > 0):
                c += 1
        if(c >= 7):
            print("Valid")
            valid += 1
        c = 0

    return valid + 1


def PartTwo(info):
    info = strToArr(info)

    print(info)
    arr = []
    tempArr = []
    for a in info:
        if(a == ""):
            arr.append(tempArr)
            tempArr = []
        else:
            tempArr.append(a)
    info = arr

    return info


# print(i)
print(PartOne(i))
print(PartTwo(i))
