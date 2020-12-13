
# NO SOLUTION YET


import timeit
from sympy.ntheory.modular import crt
import re
from tools.input import Input, strToArr, strToInt, intToStr, arrToStr, newlineParse

i = Input(2020, 13).getData()
i = Input(2020, 13).getFromExample()


def PartOne(info):
    info = strToArr(info)

    fInfo = []
    for i in info:
        if(i != "x"):
            fInfo.append(int(i))
    info = fInfo
    earlyDep = fInfo[0]
    margin = [0, 0]
    tMargin = 0

    for i in info[1::]:
        while tMargin < earlyDep:
            tMargin += i
        if(tMargin - earlyDep < margin[1] or margin[1] == 0):
            margin[0] = i
            margin[1] = tMargin - earlyDep
        tMargin = 0
    return margin[0] * margin[1]


def PartTwo(info):
    # noParseInfo = info
    info = strToArr(info)
    tInfo = []
    a = 0
    for i in info:
        if(i != "x"):
            tInfo.append([int(i), int(i) - a])
        a += 1
    info = tInfo

    modulo = 1
    for i in range(len(info)):
        for j in range(len(info)):
            if(j != i):
                modulo *= info[j][1]
        info[i].append(modulo)
        modulo = 1

    for i in info:
        x = 1
        m = i[2] % i[1]
        print(i)
        while True:
            if((m*x) % i[1] == 1):
                i.append(x)
                break
            x += 1

    total = 0
    for i in info:
        print(i)
        total += (i[1] * i[2] * i[3])
        modulo *= i[0]

    print(total)
    print(modulo)
    print(total % modulo)


print("Input:\n", i)
print("--------Results--------")
print("Part 1:", PartOne(i))
print("Part 2:", PartTwo(i))

# Runtime
# print("\n--------Runtime--------")
# print("Part 1:", str((timeit.timeit(
#     f"PartOne(i)", globals=locals(), number=1000))) + "ms")
# print("Part 2:", str((timeit.timeit(
#     f"PartTwo(i)", globals=locals(), number=1000))) + "ms")
