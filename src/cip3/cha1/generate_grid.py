#
# generate a table with random data
#

import random

def getInt(msg, min, default = None):
    while True:
        try:
            num = input(msg)
            if num:
                num = int(num)
                if (num > min):
                    return num
                else:
                    print('The input number {} is should be greater than {} !'.format(num, min))
            elif default is not None:
                return default
        except ValueError:
            print('Please input valid number!')
            continue

rows = 0
columns = 0
min = -100
max = 1000

rows = getInt('Input rows of table(or ENTER to use 5):', 0, 5)
columns = getInt('Input columns of table(or ENTER to use 5):', 0, 5)
min = getInt('Input min number(or ENTER to use -100):', -10000, -100)
max = getInt('Input min number(or ENTER to use 1000):', min, 1000)

for row in range(0, rows):
    line = ""
    for column in range(0, columns):
        line += str(random.randint(min, max)) + '\t\t'
    print(line)
