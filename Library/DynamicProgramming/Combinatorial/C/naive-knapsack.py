#!/usr/bin/env python
#coding:utf-8


def read():
    return map(int,raw_input().strip().split(" "))


def knapsack(number,weight,items):
    def solver(index,now_weight):
        if (index >= number) or (now_weight == 0):
            return 0
        else:
            (value , w) = items[index]
            if (w > now_weight):
                tmp = solver(index+1,now_weight)
                return tmp
            else:
                maxval = float("-inf")
                for num in xrange(0,(now_weight/w)+1,1):
                    val = solver(index+1,now_weight - w * num) + (value * num if num != 0 else 0)
                    if (val > maxval) : maxval = val
                return maxval
    return solver(0,weight)


if __name__ == "__main__":
    (n,w) = read()
    print knapsack(n,w,[read() for d in xrange(n)])
