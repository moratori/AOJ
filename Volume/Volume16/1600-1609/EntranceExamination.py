#!/usr/bin/env python
#coding:utf-8


def main():
    while True:
        m,n_min,n_max = map(int,raw_input().split(" "))
        if m == 0 and n_min == 0 and n_max == 0:
            break

        seq = []
        for cnt in xrange(m):
            p = int(raw_input())
            seq.append(p)

        max_gap = -1
        res = None

        for n in xrange(n_min,n_max+1,1):
            pass_min = seq[0:n][-1]
            fail_max = seq[n]
            diff = abs(pass_min - fail_max)
            if diff > max_gap: 
                max_gap = diff
                res = n
            elif diff == max_gap:
                if n > res: res = n
        print res



if __name__ == "__main__":
    main()
