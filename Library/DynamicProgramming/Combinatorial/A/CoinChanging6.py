#!/usr/bin/env python
#coding:utf-8

 
def read():
    return map(int,raw_input().strip().split(" "))
 


def least(money,coins):
    memo = [float("inf") for i in xrange(money+1)]
    done = [False for i in xrange(money+1)]
    memo[0] = 0
    memo[1] = 1
    done[0] = done[1] = True
    def main(money):
        if done[money]:
            return memo[money]
        else:
            l = [main(money - coin) + 1 for coin in coins if money >= coin]
            memo[money] = min(l) if l else float("inf")
            done[money] = True
            return memo[money]
    return main(money)


if __name__ == "__main__":
    (money,_) = read()
    coins = read()
    print least(money,coins)
