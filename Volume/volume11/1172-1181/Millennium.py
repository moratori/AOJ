#!/usr/bin/env python
#coding:utf-8


def solve(birth):
    (y,m,d) = birth
    ans = 0

    if (y % 3 == 0):
        ans += 20 - d
    elif (m % 2 == 0):
        ans += 19 - d
    else:
        ans += 20 - d

    ans += 1

    for em in xrange(m+1,10+1):
        if (y % 3 == 0):
            ans += 20
        elif (em % 2 == 0):
            ans += 19
        else:
            ans += 20

    for ey in xrange(y+1,1000):
        for em in xrange(1,10+1):
            if (ey % 3 == 0):
                ans += 20
            elif (em % 2 == 0):
                ans += 19
            else:
                ans += 20

    return ans

def main():
    for d in xrange(int(raw_input())):
        print solve(map(int,raw_input().split(" ")))

if __name__ == "__main__": main()
