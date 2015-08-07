#!/usr/bin/env python
#coding:utf-8



def join(prefix,s):
    if prefix == 0:return ""
    if prefix == 1: return s
    return "%s%s" %(prefix,s)



def encode(n):
    th = n / 1000
    hu = (n - th * 1000) / 100
    te = (n - th * 1000 - hu * 100) / 10
    on = (n - th * 1000 - hu * 100 - te * 10)
    result = ""
    result += join(th,"m")
    result += join(hu,"c")
    result += join(te,"x")
    result += join(on,"i")
    return result


def rad(c):
    if c == "m":
        return 1000
    elif c == "c":
        return 100
    elif c == "x":
        return 10
    elif c == "i":
        return 1

def israd(c):
    return (c == "m") or (c == "c") or (c == "x") or (c == "i")

def decode(mcxi):
    result = 0
    s = 1
    for ch in mcxi:
        if israd(ch):
            result += rad(ch) * s
            s = 1
        else:
            s = int(ch)
    return result


def solve(left,right):
    return encode(decode(left)+decode(right))


def main():
    for d in xrange(int(raw_input())):
        (left,right) = raw_input().split(" ")
        print solve(left,right)

if __name__ == "__main__":
    main()


