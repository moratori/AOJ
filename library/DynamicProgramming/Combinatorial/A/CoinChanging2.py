#!/usr/bin/env python
#coding:utf-8


def read():
    return map(int , raw_input().strip().split(" "))



def least(money,kind,coins):
    memo = [[None for i in xrange(0,money+1,1)] for j in xrange(0,kind)]
    def solver(index,money):
        if not (memo[index][money] is None):
            return memo[index][money]
        elif money == 0:
            return 0
        elif (0 > index):
            return float("inf")
        else:
            coin = coins[index]
            if (coin > money):
                tmp = solver(index-1,money)
                memo[index][money] = tmp
                return tmp
            else:
                minval = float("inf")
                for num in xrange(0,(money/coin)+1,1):
                    tmp = solver(index - 1 , money - coin * num) + num
                    if tmp < minval: minval = tmp
                memo[index][money] = minval
                return minval
    return solver(kind-1,money)




if __name__  == "__main__" :
    (n,m) = read()
    coins = read()
    print least(n,m,coins)
