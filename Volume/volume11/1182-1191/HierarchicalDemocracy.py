

import math

def parse(string):

    contents = string[1:-1]
    if ( contents.isdigit() ): 
        return [int(contents)]

    paren = 0
    acc = ""
    result = []

    for char in contents:
        if (char == "["):
            paren += 1
        elif (char == "]"):
            paren -= 1
        acc += char
        if (paren == 0):
            result.append(parse(acc))
            acc = ""

    return result

def major(n):
    return int(math.floor(n/2.0)) + 1

def least(obj):
    if ( type(obj) == int ):
        return major(obj)
    m = major(len(obj))
    tmp = [least(each) for each in obj]
    tmp.sort()
    return sum(tmp[0:m])


for each in xrange(input()):print least(parse(raw_input()))


