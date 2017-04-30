#!/usr/bin/env python
#coding:utf-8


LEFT = "qazwsxedcrfvtgb"

def count(line):
    flag = None
    cnt = 0
    for c in line:
        if flag is None:
            if c in LEFT: 
                flag = True
            else:
                flag = False
        if c in LEFT:
            if not flag: 
                cnt += 1
                flag = True
        else:
            if flag: 
                cnt += 1
                flag = False

    return cnt


def main():
    while True:
        line = raw_input()
        if line == "#": break
        print count(line)


if __name__ == "__main__":
    main()
