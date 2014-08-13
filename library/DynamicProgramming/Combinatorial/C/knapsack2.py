#!/usr/bin/env python
#coding:utf-8


def read():
    return map(int,raw_input().strip().split(" "))


def knapsack(number,weight,items):
    memo = [None for i in range(weight+1)]
    memo[0] = 0
    def solver(now_weight):

        if not (memo[now_weight] is None):
            return memo[now_weight]
        else:
            light = [solver(now_weight - i_w) + i_v for (i_v,i_w) in items if now_weight >= i_w]
            memo[now_weight] = (0 if not light else max(light))
            return memo[now_weight]
    return solver(weight)


if __name__ == "__main__":
    (n,w) = read()
    print knapsack(n,w,[read() for d in xrange(n)])
