#
# display a given number in console
# usage: bigdigits <number>
#
import sys


digits = [
    ["*****", "*   *", "*   *", "*   *", "*****"],  # 0
    ["  *  ", "  *  ", "  *  ", "  *  ", "*****"],  # 1
    ["*****", "    *", "*****", "*    ", "*****"],  # 2
    ["*****", "    *", "*****", "    *", "*****"],  # 3
    ["* *  ", "* *  ", "*****", "  *  ", "  *  "],  # 4
    ["*****", "*    ", "*****", "    *", "*****"],  # 5
    ["*****", "*    ", "*****", "*   *", "*****"],  # 6
    ["*****", "    *", "    *", "    *", "    *"],  # 7
    ["*****", "*   *", "*****", "*   *", "*****"],  # 8
    ["*****", "*   *", "*****", "    *", "*****"]   # 9
]

def printInt(num):
    num = str(num)
    # generate number sequence
    numSequence = []
    for ch in num:
        ch = int(ch)
        numSequence.append(digits[ch])
    # print big digits
    line = 1
    while line <= 5:
        lineStr = ""
        for n in numSequence:
            lineStr += n[line - 1] + "  "
        print(lineStr)
        line += 1

try:
    # receive input args from command line
    inputNum = sys.argv[1]
    inputNum = int(inputNum)
    printInt(inputNum)
except IndexError:
    print("usage: bigdigits <number>")
except ValueError:
    print("usage: bigdigits <number>")
