import timeit
import math
import re
from tools.input import Input, strToArr, strToInt, intToStr, arrToStr, newlineParse

i = Input(2020, 16).getData()
# i = Input(2020, 16).getFromExample()


def PartOne(info):
    # noParseInfo = info
    info = strToArr(info)
    info = newlineParse(info)
    validRange = {}

    for i in info[0]:
        ranges = re.findall(r"\d*\-\d*", i)
        if(ranges):
            for r in ranges:
                o = r.split("-")
                for i in range(int(o[0]), int(o[1])+1):
                    validRange[str(i)] = ""

    errorRate = 0

    for i in info[2][1::]:
        n = int(i)
        if(validRange.get(i) is None):
            errorRate += n

    return errorRate


def PartTwo(info):
    info = strToArr(info)
    info = newlineParse(info)
    validRange = {}

    for i in info[0]:
        ranges = re.findall(r"\d*\-\d*", i)
        if(ranges):
            for r in ranges:
                o = r.split("-")
                for i in range(int(o[0]), int(o[1])+1):
                    validRange[str(i)] = ""

    nearbyTickets = []
    tempNearbyTickets = []
    ticketLength = len(info[1][1::])
    for i in enumerate(info[2][1::]):
        tempNearbyTickets.append(i[1])
        if((i[0]+1) % ticketLength == 0):
            nearbyTickets.append(tempNearbyTickets)
            tempNearbyTickets = []

    for i in enumerate(nearbyTickets):
        for j in i[1]:
            if(validRange.get(j) is None):
                nearbyTickets[i[0]] = None
                continue

    validTickets = []
    for i in nearbyTickets:
        if(i != None):
            validTickets.append(i)

    departureRanges = []
    for i in info[0]:
        ranges = re.findall(r"\d*\-\d*", i)
        tempValidRange = {}
        for r in ranges:
            o = r.split("-")
            for i in range(int(o[0]), int(o[1])+1):
                tempValidRange[str(i)] = ""
        departureRanges.append(tempValidRange)

    validFields = []
    for d in departureRanges:
        valid = [True for m in range(len(departureRanges))]
        for i in validTickets:
            for j in enumerate(i):
                if(d.get(j[1]) is None):
                    valid[j[0]] = False
        validFields.append(valid)

    for _ in range(len(info)*10):
        for i in enumerate(validFields):
            if(i[1].count(True) == 1):
                index = i[1].index(True)
                for j in enumerate(validFields):
                    if(i[0] == j[0]):
                        continue
                    j[1][index] = False

    total = 1
    for i in validFields[0:6]:
        t = info[1][1::]
        total *= int(t[i.index(True)])

    return total


# print("Input:\n", i)
# print("--------Results--------")
print("Part 1:", PartOne(i))
print("Part 2:", PartTwo(i))

# Runtime
print("\n--------Runtime--------")
print("Part 1:", str((timeit.timeit(
    f"PartOne(i)", globals=locals(), number=1000))) + "ms")
print("Part 2:", str((timeit.timeit(
    f"PartTwo(i)", globals=locals(), number=1000))) + "ms")
