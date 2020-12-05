import math
from tools.input import Input, strToArr, strToInt, intToStr, arrToStr

i = Input(2019, 6).getData()

# Create 2 of this recursive function


def recursiveP1(argument, obj, total):
    try:
        for x in obj[argument]:
            total["p"] += 1
            recursiveP1(x, obj, total)
    except:
        return 0

    return 0


def recursiveP2(argument, obj, total, SAN, YOU):
    try:
        if(SAN != None):
            SAN.append(argument)

        if(YOU != None):
            YOU.append(argument)

        for x in obj[argument]:
            total["p"] += 1
            recursiveP2(x, obj, total, SAN, YOU)
    except:
        return 0

    return 0


def PartOne(info):
    info = strToArr(info)
    obj = {}
    tempArr = []
    total = {"p": 0}

    for i in info:
        s = i.split(")")
        for j in info:
            c = j.split(")")
            if(c[1] == s[1]):
                tempArr.append(c[0])
        obj[s[1]] = tempArr
        tempArr = []

    for i in info:
        s = i.split(")")[1]
        recursiveP1(s, obj, total)

    return total["p"]


def PartTwo(info):
    info = strToArr(info)
    obj = {}
    tempArr = []
    total = {"p": 0, "SAN": [], "YOU": []}

    for i in info:
        s = i.split(")")
        for j in info:
            c = j.split(")")
            if(c[1] == s[1]):
                tempArr.append(c[0])
        obj[s[1]] = tempArr
        tempArr = []
    SAN = []
    YOU = []
    a = []
    recursiveP2("YOU", obj, total, None, YOU)
    recursiveP2("SAN", obj, total, SAN, None)

    for i in range(0, len(SAN)):
        for j in range(0, len(YOU)):
            if(SAN[i] == YOU[j]):
                a.append([SAN[i], YOU[j], [i, j]])

    return SAN, YOU

# COMPLETE PART 2!!
# COMPLETE PART 2!!
# COMPLETE PART 2!!
# COMPLETE PART 2!!


# print(i)
# print(PartOne(i))
print(PartTwo(i))
