import math
from tools.input import Input, strToArr, strToInt, intToStr, arrToStr

i = Input(2019, 3).getData()


def PartOne(info):
    info = strToArr(info)
    """
        Create whole path with vectors for one
        Do the same with other path, comparing if any value goes over or under the other
        Compare the vector with highest sum
    """
    l = int(len(info))

    arr1 = info[0:int(l/2)]
    path1 = [0, 0]
    path1Snapshots = []

    arr2 = info[int(l/2):int(l)]
    path2 = [0, 0]
    path2Snapshots = []

    intersections = []

    for i in arr1:
        num = int(i[1:])
        if(i[:1] == "U"):
            path1[0] += num
        if(i[:1] == "D"):
            path1[0] -= num
        if(i[:1] == "R"):
            path1[1] += num
        if(i[:1] == "L"):
            path1[1] -= num
        path1Snapshots.append([path1[0], path1[1]])

    for i in arr2:
        num = int(i[1:])
        if(i[:1] == "U"):
            path2[0] += num
        if(i[:1] == "D"):
            path2[0] -= num
        if(i[:1] == "R"):
            path2[1] += num
        if(i[:1] == "L"):
            path2[1] -= num
        path2Snapshots.append([path2[0], path2[1]])

    


    return intersections


def PartTwo(info):
    return 0


# print(i)
print(PartOne(i))
print(PartTwo(i))
