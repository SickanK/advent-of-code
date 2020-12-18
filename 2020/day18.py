import timeit
import math
import re
from tools.input import Input, strToArr, strToInt, intToStr, arrToStr, newlineParse

i = Input(2020, 18).getData()
# i = Input(2020, 18).getFromExample()


def PartOne(info):
    # noParseInfo = info
    info = strToArr(info)

    total = 0
    for i in info:
        sumArr = []
        for _ in range(200):
            tempSumArr = []
            if(sumArr == []):
                inside = re.split(r"(\([0-9*+ ]*\))", i)
            else:
                inside = re.split(r"(\([0-9*+ ]*\))", "".join(sumArr))

            toFind = re.findall(r"(\([0-9*+ ]*\))", "".join(inside))
            for s in inside:
                if(s in toFind):
                    nums = re.split(r"\s|[()]", s)[1::][::-1][1::][::-1]
                    totali = 0
                    for n in enumerate(nums):
                        sign = n[1]
                        if(sign == "*"):
                            if(n[0] == 1):
                                res = int(nums[n[0]-1]) * int(nums[n[0]+1])
                            else:
                                res = totali * int(nums[n[0]+1])
                            totali = res
                        elif(sign == "+"):
                            if(n[0] == 1):
                                res = int(nums[n[0]-1]) + int(nums[n[0]+1])
                            else:
                                res = totali + int(nums[n[0]+1])
                            totali = res

                    if(totali > 0):
                        tempSumArr.append(str(totali))
                else:
                    tempSumArr.append(s)

            sumArr = tempSumArr

        sumArr = "".join(sumArr)
        sumArr = sumArr.split(" ")
        t = 0
        for n in enumerate(sumArr):
            sign = n[1]
            if(sign == "*"):
                if(n[0] == 1):
                    res = int(sumArr[n[0]-1]) * int(sumArr[n[0]+1])
                else:
                    res = t * int(sumArr[n[0]+1])
                t = res
            elif(sign == "+"):
                if(n[0] == 1):
                    res = int(sumArr[n[0]-1]) + int(sumArr[n[0]+1])
                else:
                    res = t + int(sumArr[n[0]+1])
                t = res
        total += t
        t = 0

    return total


def sum(arr):
    tot = 0
    for a in arr:
        tot += int(a)
    return tot


def mult(arr):
    tot = 1
    for a in arr:
        tot *= int(a)
    return tot


def PartTwo(info):
    # noParseInfo = info
    info = strToArr(info)

    total = 0
    for i in info:
        sumArr = []
        for _ in range(200):
            tempSumArr = []
            if(sumArr == []):
                inside = re.split(r"(\([0-9*+ ]*\))", i)
            else:
                inside = re.split(r"(\([0-9*+ ]*\))", "".join(sumArr))

            toFind = re.findall(r"(\([0-9*+ ]*\))", "".join(inside))
            for s in inside:
                if(s in toFind):
                    nums = re.split(r"\s|[()]", s)[1::][::-1][1::][::-1]
                    nu = "".join(nums)
                    noadd = re.split(r"[^\d^\+^\d]", nu)
                    toMult = []
                    for a in noadd:
                        toMult.append(sum(a.split("+")))

                    tempSumArr.append(str(mult(toMult)))
                else:
                    tempSumArr.append(s)

            sumArr = tempSumArr

        sumArr = "".join(sumArr)
        sumArr = sumArr.split(" ")
        nu = "".join(sumArr)
        noadd = re.split(r"[^\d^\+^\d]", nu)
        toMult = []
        for a in noadd:
            toMult.append(sum(a.split("+")))

        total += mult(toMult)

    return total


# print("Input:\n", i)
print("--------Results--------")
print("Part 1:", PartOne(i))
print("Part 2:", PartTwo(i))

# Runtime
print("\n--------Runtime--------")
print("Part 1:", str((timeit.timeit(
    f"PartOne(i)", globals=locals(), number=1000))) + "ms")
print("Part 2:", str((timeit.timeit(
    f"PartTwo(i)", globals=locals(), number=1000))) + "ms")
