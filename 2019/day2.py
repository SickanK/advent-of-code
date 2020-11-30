import math
from tools.input import Input, strToArr, strToInt, intToStr, arrToStr

i = Input(2019, 2).getData()


def PartOne(info, first, second):
    info = strToArr(info)
    info = strToInt(info)
    info[1] = first
    info[2] = second
    i = 0
    while(i < len(info)):
        if(info[i] == 1):
            info[info[i+3]] = info[info[i+1]] + info[info[i+2]]
            i += 4
        elif(info[i] == 2):
            info[info[i+3]] = info[info[i+1]] * info[info[i+2]]
            i += 4
        elif(info[i] == 99):
            break

    return info[0]


def PartTwo(info):
    for x in range(0, 100):
        for y in range(0, 50):
            if(PartOne(i, x, y) == 19690720):
                return 100 * x + y
    return 0


print(PartOne(i, 12, 2))
print(PartTwo(i))
