import timeit
import math
import re
from tools.input import Input, strToArr, strToInt, intToStr, arrToStr, newlineParse

i = Input(2020, 15).getData()
# i = Input(2020, 15).getFromExample()


def PartOne(info, num=2020):
    # noParseInfo = info
    info = strToArr(info)
    lastTurns = {}
    lastNum = int(info[0])
    firstNum = True

    for i in range(len(info)):
        s = str(info[i])
        lastTurns[s] = [i+1]
        lastNum = str(s)

    for i in range(len(info) + 1, num+1):
        if(firstNum):
            lastNum = "0"
            firstNum = False
            if(lastTurns.get(lastNum) is None):
                lastTurns[lastNum] = [i]
            else:
                turnBeforeLast = lastTurns[lastNum][-1]
                lastTurns[lastNum] = [int(turnBeforeLast), i]
        else:
            turnBeforeLast = lastTurns[lastNum][-2]
            turnLast = lastTurns[lastNum][-1]

            lastNum = str(int(turnLast) - int(turnBeforeLast))

            if(lastTurns.get(lastNum) is None):
                lastTurns[lastNum] = [i]
                firstNum = True
            else:
                turnBeforeLast = lastTurns[lastNum][-1]
                lastTurns[lastNum] = [int(turnBeforeLast), i]

    return lastNum


def PartTwo(info):
    return PartOne(info, 30000000)


print("Input:\n", i)
# print("--------Results--------")
print("Part 1:", PartOne(i))
print("Part 2:", PartTwo(i))

# Runtime
print("\n--------Runtime--------")
print("Part 1:", str((timeit.timeit(
    f"PartOne(i)", globals=locals(), number=100)*10)) + "ms")
print("Part 2:", str((timeit.timeit(
    f"PartTwo(i)", globals=locals(), number=1)*1000)) + "ms")
