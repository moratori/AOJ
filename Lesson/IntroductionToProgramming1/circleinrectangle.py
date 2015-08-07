#!/usr/bin/env python
#coding:utf-8


def main():
    print solve(map(int,raw_input().split(" ")))



def solve(a):
    (W,H,x,y,r) = a
    return "Yes" if ((r <= x <= W-r) and (r <= y <= H-r)) else "No"


if __name__ == "__main__": main()
