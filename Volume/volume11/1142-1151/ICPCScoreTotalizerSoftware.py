
import math

def average(lst):
    lst.remove(max(lst))
    lst.remove(min(lst))
    return int(math.floor(sum(lst)/float(len(lst))))


while True:
    line_n = input()
    if (line_n == 0):break
    print average([input() for dummy in xrange(line_n)])
