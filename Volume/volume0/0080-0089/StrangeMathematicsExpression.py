

import operator

ops = {"+": operator.__add__,
       "-": operator.__sub__,
       "*": operator.__mul__,
       "/": (lambda x,y: float(x)/float(y))}

while True:
    try:
        token = raw_input().strip().split()
    except (EOFError):break
    stack = []
    for each in token:
        try:
            num = float(each)
            stack.append(num)
        except:
            right = stack.pop()
            left  = stack.pop()
            stack.append(ops[each](left,right))
    print "%.5f" %(stack[0])
