#!/usr/vin/env python
#coding:utf-8




def main():
    print solve(int(raw_input()))


def solve(s):
    h = s / 3600
    s -= h * 3600
    m = s/60
    s -= m * 60
    return "%s:%s:%s" %(h,m,s)

if __name__ == "__main__": main()
