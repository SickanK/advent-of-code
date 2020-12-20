import timeit
import math
import re
from tools.input import Input, strToArr, strToInt, intToStr, arrToStr, newlineParse

i = Input(2020, 20).getData()[::-1][1::][::-1]
# i = Input(2020, 20).getFromExample()


def rotateX(block):
    return block[::-1]


def rotateY(block):
    flipped = []
    for i in block:
        flipped.append(i[::-1])
    return flipped


def rotate(matrix, degree):
    if abs(degree) not in [0, 90, 180, 270, 360]:
        return matrix
    if degree == 0:
        return matrix
    elif degree > 0:
        return rotate(zip(*matrix[::-1]), degree-90)
    else:
        return rotate(zip(*matrix[::-1]), degree+90)


def PartOne(info):
    # noParseInfo = info
    info = strToArr(info)
    info = newlineParse(info)
    edges = []
    listedIds = []
    for i in info:
        tileId = re.split(r":| ", i[0])[1]
        listedIds.append(tileId)
        top = (i[1], i[1][::-1])
        bottom = (i[-1], i[-1][::-1])
        l = []
        r = []
        for j in i[1::]:
            l.append(j[0])
            r.append(j[-1])
        left = ("".join(l), "".join(l[::-1]))
        right = ("".join(r), "".join(r[::-1]))
        print(tileId)
        print(right)
        edges.append({"tid": tileId, "top": top, "bottom": bottom,
                      "left": left, "right": right})

    ids = {}
    objids = ["top", "left", "bottom", "right"]
    rotdeg = {"top": 0, "left": 90, "bottom": 180, "right": 270}
    reversedeg = {"0": "top", "1": "left", "2": "bottom",  "3": "right"}
    present = []
    present2 = []

    for i in edges:
        ids[i["tid"]] = []
        toAppend = []
        for j in edges:
            if(j == i):
                continue
            for o in objids:
                for p in objids:
                    if(i[o][0] == j[p][0]):
                        if(j["tid"] not in toAppend):
                            e = 0
                            if(o == p and o not in present2):
                                present2.append(o)
                                e = 180

                            rotdeggeg = rotdeg[p]-rotdeg[o]+e
                            if(rotdeggeg < 0):
                                rotdeggeg = 360 - rotdeggeg
                            d = (int((rotdeggeg/90))+4) % 4
                            d = int(((d+(rotdeg[p]/90)))+4) % 4
                            toAppend.append(
                                (j["tid"], reversedeg[str(d)], rotdeg[p]-rotdeg[o]))
                    elif(i[o][0] == j[p][1]):
                        if(j["tid"] not in toAppend):
                            e = 0
                            if(o == p and o not in present):
                                present.append(o)
                                e = 180

                            rotdeggeg = rotdeg[o]-rotdeg[p]+e
                            if(rotdeggeg < 0):
                                rotdeggeg = 360 - rotdeggeg
                            d = (int((rotdeggeg/90))+4) % 4
                            d = int(((d+(rotdeg[p]/90)))+4) % 4
                            toAppend.append(
                                (j["tid"], reversedeg[str(d)], rotdeg[p]-rotdeg[o]+e))

        for t in toAppend:
            ids[i["tid"]].append(t)

    corners = []
    total = 1
    for i in listedIds:
        if(len(ids[i]) == 2):
            corners.append(i)
            total *= int(i)

    return total,  ids, corners


def getLengthInDir(info, total, ids, start, direction):
    nextBlock = ""
    t = total
    for i in ids[start]:
        if(i[1] == direction):
            nextBlock = i[0]

    if(len(nextBlock) > 0):
        t += 1
        return getLengthInDir(info, t, ids, nextBlock, direction)
    return t


def PartTwo(info):
    noParseInfo = info
    info = strToArr(info)
    info = newlineParse(info)
    print(PartOne(noParseInfo)[0])
    ids = PartOne(noParseInfo)[1]
    print(ids)
    corners = PartOne(noParseInfo)[2]

    leftUpCorner = ""
    for i in corners:
        presentCorners = []
        print(i)
        for j in ids[i]:
            print(j)
            presentCorners.append(j[1])
        if("top" in presentCorners and "right" in presentCorners):
            leftUpCorner = i

    sortedInfo = []
    height = getLengthInDir(info, 1, ids, leftUpCorner, "top")
    width = getLengthInDir(info, 1, ids, leftUpCorner, "right")
    print(width)

    for s in range(height):
        sortedInfo.append([])
    print(sortedInfo)

    stripped = []
    for i in info:
        r = i[1::]

        ts = []
        for j in r[1::][:: -1][1::][:: -1]:
            s = j[1::][:: -1][1::][:: -1]
            ts.append(s)
        stripped.append(ts)
    info = stripped

    # for i in info:
    #     for j in i:
    #         print(j)

    return 0


# print("Input:\n", i)
# print("--------Results--------")
# print("Part 1:", PartOne(i))
print("Part 2:", PartTwo(i))

# Runtime
# print("\n--------Runtime--------")
# print("Part 1:", str((timeit.timeit(
#     f"PartOne(i)", globals=locals(), number=1000))) + "ms")
# print("Part 2:", str((timeit.timeit(
#     f"PartTwo(i)", globals=locals(), number=1000))) + "ms")
