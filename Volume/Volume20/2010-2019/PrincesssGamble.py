#!/usr/bin/env python
# coding:utf-8


def main():
    while True:
        n, m, p = map(int, raw_input().split(" "))
        if n == 0 : break
        x = []
        for d in xrange(n):
            x.append(int(raw_input()))
        m -= 1
        if x[m] == 0:
            print "0"
        else:
            tot = sum(x) * 100
            tot -= tot * (p/100.0)
            print int(tot/x[m])


if __name__ == "__main__":
    main()
