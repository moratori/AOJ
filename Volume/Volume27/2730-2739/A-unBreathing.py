#!/usr/bin/env python
#coding:utf-8



def main():
    n = int(raw_input())
    cnt = 0
    flag = True
    for dummy in xrange(n):
        val = raw_input()
        if val == "A": 
            cnt += 1
        else:
            if cnt == 0:
                flag = False
                break
            else:
                cnt -= 1
    if flag and cnt == 0:
        print "YES"
    else:
        print "NO"



if __name__ == "__main__":
    main()
