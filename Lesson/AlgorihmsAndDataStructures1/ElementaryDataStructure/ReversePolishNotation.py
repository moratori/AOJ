

import operator

ops = {"+": operator.__add__,
       "-": operator.__sub__,
       "*": operator.__mul__,
       "/": (lambda x,y: float(x)/float(y))}

token = raw_input().split(" ")
stack = []
for each in token:
    if each.isdigit():
        stack.append(int(each))
    else:
        right = stack.pop()
        left  = stack.pop()
        stack.append(ops[each](left,right))
print "%.5f" %(stack[0])
