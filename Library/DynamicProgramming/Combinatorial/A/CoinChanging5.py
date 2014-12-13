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
                return min(solver(money,index-1) , solver(money % coin,index-1) + (money/coin))
    return solver(n,len(coins)-1)
 
 
 
 
if __name__ == "__main__":
    (n,_) = read()
    coins = read()
    print least1(n,coins)
