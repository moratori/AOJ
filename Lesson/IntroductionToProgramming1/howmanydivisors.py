#!/usr/bin/env python
#coding:utf-8


def main():
    print solve(map(int,raw_input().split(" ")))



def solve(val):
    (a,b,c) = val
    cnt = 0
    for n in xrange(a,b+1,1):
        if (c % n == 0):cnt += 1
    return cnt


if __name__ == "__main__":
    main()

