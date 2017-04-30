#!/usr/bin/env python
#coding:utf-8


def calc(v):
    p,a,b,c,d,e,f,s,m = v
    income = -1 * p
    time = float(a + b + c)
    for dummy in xrange(m):
        time += d + e
        income += f * s
    return income/time

def solve(world):
    vs = sorted([(name,calc(v)) for (name,v) in world],key=lambda x: -x[1])
    result =[]
    m = {each:[] for each in list(set([b for (a,b) in vs]))}
    rs = sorted(m.keys(),key=lambda x: -x)

    for r in rs:
        for (a,b) in vs:
            if b == r: m[r].append(a)
    for each in rs:
        for x in sorted(m[each]):
            print x

    return 

def main():
    while True:
        n = int(raw_input())
        if n == 0 : break
        world = []
        for d in xrange(n):
            sp = raw_input().split(" ")
            world.append((sp[0],map(int,sp[1:])))
        solve(world)
        print "#"



if __name__ == "__main__":
    main()
