#!/usr/bin/env python
#coding:utf-8


def read():
    return map(int,raw_input().strip().split(" "))

def least1(n,m,coins):
    cache = [[None for di in xrange(m)] for dj in xrange(n+1)]
    def solver(index,money):
        if not (cache[money][index] is None):
            return cache[money][index]
        elif (money == 0):
            return 0
        elif (0 > index):
            return float("inf")
        elif (money == 1):
            return 1
        else:
            coin = coins[index]
            if (coin > money):
                return solver(index-1,money)
            else:
                minval = float("inf")
                for num in xrange(0,(money/coin)+1,1):
                    (new_money,new_index) = (money - num * coin , index - 1)
                    tmp = solver(new_index,new_money) 
                    cache[new_money][new_index] = tmp
                    if (minval > tmp + num):minval = tmp + num
                return minval
    return solver(m-1,n)



def least2(n,m,coins):
    cache = [[None for di in xrange(m)] for dj in xrange(n+1)]
    cache[0] = [0 for di in xrange(m)]
    def solver(index,money):
        if (0 > index):
            return float("inf")
        elif not (cache[money][index] is None):
            return cache[money][index]
        else:
            coin = coins[index]
            if (coin > money):
                (new_money , new_index) = (money , index-1)
                tmp = solver(new_index , new_money)
                cache[new_money][new_index] = tmp
                return tmp
            else:
                minval = float("inf")
                for num in xrange(0,(money/coin)+1,1):
                    (new_money,new_index) = (money - num * coin , index - 1)
                    tmp = solver(new_index,new_money) 
                    cache[new_money][new_index] = tmp
                    if (minval > tmp + num):minval = tmp + num
                return minval
    return solver(m-1,n)


#
# T[x] は x円を払う時のコインの枚数を表す
#
# m = 3
# m+2 = 5
# xrange(5) = [0,1,2,3,4]

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
