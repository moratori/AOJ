#!/usr/bin/env python
#coding:utf-8


def read():
    return map(int,raw_input().strip().split(" "))



def solve(n,weight,items):
    memo = [[None for i in xrange(weight+1)] for j in xrange(0,n)]
    def main(index,w):
        if (index >= n):
            return 0
        elif not (memo[index][w] is None):
            return memo[index][w]
        else:
            (value,weight) = items[index]
            if (weight > w):
                tmp = main(index+1,w)
                memo[index][w] = tmp
                return tmp
            else:
                tmp = max(main(index+1,w-weight)+value,main(index+1,w))
                memo[index][w] = tmp
                return tmp
    return main(0,weight)


if __name__ == "__main__":
    (n,m) = read()
    print solve(n,m,[read() for dummy in xrange(n)])
