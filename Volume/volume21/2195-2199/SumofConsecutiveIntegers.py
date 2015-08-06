#!/usr/bin/env python
#coding:utf-8



def solve_(start,n):
    total = start
    while True:
        total += (start + 1)
        if total == n:
            return True
        if total > n:
            return False
        start += 1

# 1 0
def solve(n):
    result = 0
    for start in xrange(1,n+1,1):
        if start > (n - start):
            break
        if solve_(start,n):
            result += 1
    return result


def main():
    while True:
        n= int(raw_input())
        if n == 0: break
        print solve(n)


if __name__ == "__main__":
    main()
