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

    return len(arr1)


def PartTwo(info):
    return 0


# print(i)
print(PartOne(i))
print(PartTwo(i))
