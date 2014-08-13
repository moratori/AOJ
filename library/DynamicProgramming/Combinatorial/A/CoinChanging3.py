#!/usr/bin/env python
#coding:utf-8


def read():
    return map(int , raw_input().strip().split(" "))



def least(money,kind,coins):
    dp = [[(0 if i == 0 else None) for i in xrange(money+1)] for j in xrange(kind)]
    # dp[index][money]
    for _index in xrange(0,kind,1):
        for _money in xrange(0,money+1,1):
            dp[_index][_money] = min(dp[_index-1][_money] , dp[_index-1][_money-coins[_index]])


if __name__  == "__main__" :
    (n,m) = read()
    coins = read()
    print least(n,m,coins)
