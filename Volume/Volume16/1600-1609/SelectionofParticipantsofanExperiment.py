#!/usr/bin/env python
#coding:utf-8


def main():
    while True:
        n = int(raw_input())
        if n == 0 : break
        seq = sorted(map(int,raw_input().split(" ")))
        diff = 1000001
        for i in xrange(len(seq)-1):
            ldiff = abs(seq[i]-seq[i+1])
            if ldiff < diff: diff = ldiff
        print diff


if __name__ == "__main__":
    main()
