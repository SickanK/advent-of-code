import math
import re
from tools.input import Input, strToArr, strToInt, intToStr, arrToStr

i = Input(2020, 4).getData()


def PartOne(info):
    info = strToArr(info)

    arr = []
    tempArr = []
    for a in info:
        if(a == ""):
            arr.append(tempArr)
            tempArr = []
        else:
            tempArr.append(a)
    info = arr

    valid = 0
    for i in info:
        c = 0
        j = " ".join(i)
        j = j.split(":")
        for x in j:
            l = re.findall(r"ecl|iyr|eyr|hgt|hcl|byr|pid", x)
            if(len(l) > 0):
                c += 1
        if(c >= 7):
            print("Valid")
            valid += 1
        c = 0

    return valid + 1


def PartTwo(info):
    info = strToArr(info)

    arr = []
    tempArr = []
    for a in info:
        if(a == ""):
            arr.append(tempArr)
            tempArr = []
        else:
            tempArr.append(a)
    info = arr

    count = 0
    valid = 0
    for x in info:
        for l in x:
            l = l.split(" ")
            for w in l:
                u = w.split(":")
                if(u[0] == "byr"):
                    if(int(u[1]) >= 1920 and int(u[1]) <= 2002):
                        count += 1
                if(u[0] == "iyr"):
                    if(int(u[1]) >= 2010 and int(u[1]) <= 2020): 
                        count += 1
                if(u[0] == "eyr"):
                    if(int(u[1]) >= 2020 and int(u[1]) <= 2030): 
                        count += 1
                if(u[0] == "hgt"):
                    s= re.findall(r"cm", u[1])
                    b = int(re.split(r"cm|in", u[1])[0])
                    if(len(s) > 0):
                        if(b >= 150 and b <= 193):
                            count += 1
                    else:
                        if(b >= 59 and b <= 76):
                            count += 1
                if(u[0] == "hcl"):
                    o = re.match(r"#([A-Fa-f0-9]{6})", u[1])
                    if(o != None):
                        count += 1
                if(u[0] == "ecl"):
                    o = re.findall(r"amb|blu|brn|gry|grn|hzl|oth", u[1])
                    if(len(o) > 0):
                        count += 1
                if(u[0] == "pid"):
                    o = str(u[1])
                    if(len(o) == 9):
                        count += 1
        if(count >= 7):
            valid += 1
        count = 0

    return valid


# print(i)
print(PartOne(i))
print(PartTwo(i))
