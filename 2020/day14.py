import timeit
import math
import re
from tools.input import Input, strToArr, strToInt, intToStr, arrToStr, newlineParse

i = Input(2020, 14).getData()
# i = Input(2020, 14).getFromExample()


def convertToBinary(val):
    valueLeft = val
    newVal = []
    for i in range(35, -1, -1):
        c = math.floor(valueLeft/(2 ** i))
        if(c == 1):
            valueLeft -= 2 ** i
        newVal.append(str(c))
    return "".join(newVal)


def convertToDecimal(val):
    total = 0
    newVal = list(val)[::-1]
    for i in range(0, 36):
        total += int(newVal[i]) * (2 ** i)

    return total


def maskBinary(val, mask):
    newVal = list(val)
    aMask = list(mask)
    for i in range(len(aMask)):
        if(aMask[i] != "X"):
            newVal[i] = aMask[i]
    return "".join(newVal)


def PartOne(info):
    # noParseInfo = info
    info = strToArr(info)

    total = {}
    total2 = 0
    mask = info[0].split(" = ")[1]
    for i in info:
        s = i.split(" = ")
        if(s[0] == "mask"):
            mask = s[1]
        else:
            mem = s[0].split("[")[1].split("]")[0]
            t = int(i.split(" = ")[1])
            b = convertToBinary(t)
            m = maskBinary(b, mask)
            d = convertToDecimal(m)
            if(total.get(mem) is not None):
                total2 -= total[mem]
            total[mem] = d
            total2 += d

    return total2


def getAllPossibleValues(val):
    newVal = list(val)[::-1]
    c = newVal.count("X")
    l = 2 ** c
    binArr = []
    values = []

    for i in range(0, l):
        b = bin(int(i))[2::]
        binArr.append(list('0'*(c-len(b))+b))

    for y in range(l):
        total = []
        x = 0
        for i in range(0, 36):
            if(newVal[i] == "X"):
                total.append(binArr[y][x])
                x += 1
            else:
                total.append(newVal[i])

        values.append("".join(total[::-1]))

    return values


def maskBinaryV2(val, mask):
    newVal = list(val)
    aMask = list(mask)
    for i in range(len(aMask)):
        if(aMask[i] != "0"):
            newVal[i] = aMask[i]
    return "".join(newVal)


def PartTwo(info):
    # noParseInfo = info
    info = strToArr(info)

    total = {}
    total2 = 0
    mask = info[0].split(" = ")[1]
    for i in info:
        s = i.split(" = ")
        if(s[0] == "mask"):
            mask = s[1]
        else:
            mem = s[0].split("[")[1].split("]")[0]
            t = int(i.split(" = ")[1])
            b = convertToBinary(int(mem))
            m = maskBinaryV2(b, mask)
            ac = getAllPossibleValues(m)
            for a in ac:
                if(total.get(a) is not None):
                    total2 -= total[a]
                total[a] = t
                total2 += t

    return total2


print("Input:\n", i)
print("--------Results--------")
print("Part 1:", PartOne(i))
print("Part 2:", PartTwo(i))

# Runtime
print("\n--------Runtime--------")
print("Part 1:", str((timeit.timeit(
    f"PartOne(i)", globals=locals(), number=100)*10)) + "ms")
print("Part 2:", str((timeit.timeit(
    f"PartTwo(i)", globals=locals(), number=100)*10)) + "ms")
