#!/usr/bin/env python
#coding:utf-8
 
 
def read():
    return map(int,raw_input().strip().split(" "))
 
def least1(n,coins):
    def solver(money,index):
        if (money == 0):
            return 0
        elif (0 > index):
            return float("inf")
        elif (money == 1):
            return 1
        else:
            coin = coins[index]
            if (coin > money):
                return solver(money,index-1)
            else:
                return min([num + solver(money - num * coin , index - 1) for num in xrange(0,(money/coin)+1,1)])
    return solver(n,len(coins)-1)
 
 
 
 
if __name__ == "__main__":
    (n,_) = read()
    coins = read()
    print least1(n,coins)
