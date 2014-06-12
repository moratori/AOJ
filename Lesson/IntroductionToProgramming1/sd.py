

import math

while True:
    n = int(raw_input())
    if n == 0:break
    l = map(int,raw_input().split(" "))
    m = sum(l)/float(n)
    print "%f "%(math.sqrt(sum(map((lambda si: (si - m) ** 2),l))/n))

