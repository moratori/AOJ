#!/usr/bin/env python
#coding:utf-8

MAXIMUM_FRAME = 10000

def main():
    while True:
        n, a, b, c, x = map(int, raw_input().split(" "))
        if n == 0 and a == 0 and b == 0 and c == 0 and x ==0: break
        reels = map(int,raw_input().split(" "))
        frame = 0
        while (frame <= MAXIMUM_FRAME):
            if x == reels[0]:
                del reels[0]
                if len(reels) == 0 : break
            x = (a * x + b) % c
            frame += 1
        if len(reels) == 0:
            print frame
        else:
            print -1
if __name__ == "__main__":
    main()
