#!/usr/bin/env python
#coding:utf-8

def read():
    return map(int,raw_input().strip().split(" "))



#
# T[x] = y  x円払うときにy枚かかる
# 

def least3(n,m,coins):
    T = [float("inf") for j in xrange(0,n+1)]
    T[0] = 0

    for i in xrange(0,m):
        for j in xrange(coins[i],n+1):
            T[j] = min(T[j],T[j-coins[i]]+1)
    return T[n]


if __name__ == "__main__":
    (n,m) = read()
    coins = read()
    print least3(n,m,coins)
