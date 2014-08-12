#!/usr/bin/env python
#coding:utf-8


class Seed:
    def __init__(self,name,price,a,b,c,d,e,number,unit,loop):
        self.name = name
        self.price = int(price)
        self.a     = int(a)
        self.b     = int(b)
        self.c     = int(c)
        self.d     = int(d)
        self.e     = int(e)
        self.number = int(number)
        self.unit  = int(unit)
        self.loop  = int(loop)

    def getscore(self):
        pass

    def getime(self):
        pass


def getscore(seed):
    pass


def show(seed):
    pass

def main():
    n = input()
    while (n != 0):
        show([getscore(apply(Seed , raw_input().split(" "))) for dummy in xrange(n)])
        n = input()
        print "#"
    return


main()

















