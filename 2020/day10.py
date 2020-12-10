import math
import re
from tools.input import Input, strToArr, strToInt, intToStr, arrToStr, newlineParse

i = Input(2020, 10).getData()
# i = Input(2020, 10).getFromExample()


def PartOne(info):
    info = strToArr(info)
    info = strToInt(info)
    info.append(0)
    info = sorted(info)
    info.append(info[len(info)-1]+3)

    one = 0
    three = 0
    last = 0

    for i in info:
        if(i-last == 3):
            three += 1
        if(i-last == 1):
            one += 1
        last = i

    return one * three

def PartTwo(info):
    info = strToArr(info)
    info = strToInt(info)
    info = sorted(info)

    arr = []

    for i in range(0, len(info)-1):
        if(info[i] - info[i-1] < 3 and info[i+1] - info[i] < 3):
            arr.append(info[i])

    subArrays = []
    tempSubArrays = []

    for i in range(0, len(arr)):
        if(arr[i-1]+1 == arr[i]):
            tempSubArrays.append(arr[i])
        else:
            subArrays.append(tempSubArrays)
            tempSubArrays = []
            tempSubArrays.append(arr[i])

    subArrays.append(tempSubArrays)
    subArrays = subArrays[1::]
    numArr = []

    for i in subArrays:
        if(len(i) == 3):
            numArr.append(7)
        elif(len(i) == 2):
            numArr.append(4)
        elif(len(i) == 1):
            numArr.append(2)

    total = 1

    for i in numArr:
        total *= i

    return total


print(PartOne(i))
print(PartTwo(i))
