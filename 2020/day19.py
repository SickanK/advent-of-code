import timeit
import math
import re
from tools.input import Input, strToArr, strToInt, intToStr, arrToStr, newlineParse

i = Input(2020, 19).getData()
i = Input(2020, 19).getFromExample()


def recursive(rules, zero, count):
    if(len(re.findall(r"[0-9]", " ".join(zero))) == 0):
        return "".join(zero)

    if(count == 14):
        return "".join(zero)

    for (i, s) in enumerate(zero):
        if(re.match(r"[0-9]", s)):
            if(rules[s].split(" ").count("|") > 0):
                zero[i] = f"( {rules[s]} )"
            else:
                zero[i] = rules[s]
    zero = " ".join(zero)
    zero = zero.split(" ")
    c = count + 1
    return recursive(rules, zero, c)


def PartOne(info):
    # noParseInfo = info
    info = strToArr(info)

    sp = 0
    for (i, a) in enumerate(info):
        if(a == ""):
            sp = i
            break
    messages = info[sp+1::]

    rules = {}
    for i in info:
        if(i == ""):
            break
        s = i.split(": ")
        f = s[1].split(" ")
        letter = re.findall(r"[a-zA-Z]", s[1])
        if(len(letter) > 0):
            f = letter
        rules[s[0]] = " ".join(f)

    zero = rules["0"].split(" ")
    for (i, z) in enumerate(zero):
        if(i > 0 and i < len(zero)-1):
            if(re.match(r"[0-9]", z)):
                if(i == 0):
                    zero = [*zero[::i-1], z, "(", *zero[i+1::]]
                else:
                    zero = [*zero[i-1], f"({z})", *zero[i+1::]]
    zero = recursive(rules, zero, 0)
    print(zero)

    total = 0
    for m in messages:
        if(re.match(f"^{zero}$", m)):
            total += 1

    return total


def PartTwo(info):
    # noParseInfo = info
    info = strToArr(info)
    # Same as PartOne but with count 14

    return 0


# print("Input:\n", i)
# print("--------Results--------")
print("Part 1:", PartOne(i))
# print("Part 2:", PartTwo(i))

# Runtime
# print("\n--------Runtime--------")
# print("Part 1:", str((timeit.timeit(
#     f"PartOne(i)", globals=locals(), number=1000))) + "ms")
# print("Part 2:", str((timeit.timeit(
#     f"PartTwo(i)", globals=locals(), number=1000))) + "ms")
