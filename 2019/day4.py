import math
import re
from tools.input import Input, strToArr, strToInt, intToStr, arrToStr

i = [372304, 847060]


def PartOne(info):
    total = 0
    for i in range(info[0], info[1]):
        arr = list(str(i))
        yes = 0
        yes2 = 0

        for l in range(1, len(arr)):
            l = int(l)
            if(int(arr[l-1]) <= int(arr[l]) and yes2 != -1):
                yes2 += 1
            else:
                yes2 = -1

            if(int(arr[l-1]) == int(arr[l])):
                yes += 1

        if(yes > 0 and yes2 > 0):
            total += 1

        yes = 0
        yes2 = 0
        arr = []

    return total


def PartTwo(info):
    total = 0
    for i in range(info[0], info[1]):
        arr = list(str(i))
        yes2 = 0

        for l in range(1, len(arr)):
            l = int(l)
            if(int(arr[l-1]) <= int(arr[l]) and yes2 != -1):
                yes2 += 1
            else:
                yes2 = -1

        test = re.findall(r"((^)|(.))((?(3)(?!\1).|.))\4(?!\4)", str(i))

        if(test and yes2 > 0):
            print(i)
            print(test)
            total += 1

        yes2 = 0
        arr = []

    return total


print(i)
print(PartOne(i))
print(PartTwo(i))
