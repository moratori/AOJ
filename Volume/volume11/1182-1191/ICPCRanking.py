#!/usr/bin/env python
#coding:utf-8

def parse_line():
    return map(int,raw_input().split(" "))

def main():
    while True:
        (M,T,P,R) = parse_line()
        if M == T == P == R == 0: break
        log = []
        for d in xrange(R):
            log.append(parse_line())
        print solve((M,T,P,R),log)

def icpc_sort(seq,d,flag):
    vals = d.values()
    vals = list(set(vals))
    if flag:
        vals.sort()
    else:
        vals.sort(key=lambda x: -x)
    result = []
    for val in vals:
        tmp = []
        for k,v in d.items():
            if v == val and k in seq:
                tmp.append(k)
        if tmp: result.append(tmp)
    return result

def solve(info,log):
    score = {}
    time = {}

    (_,tn,_,_) = info
    for each in xrange(1,tn+1,1):
        score[each] = 0
        time[each] = 0

    for (m,t,p,j) in log:
        if j == 0:
            score[t] +=  1
            for (m2,t2,p2,j2) in log:
                if (j2 != 0) and (t2 == t) and (p2 == p):
                    time[t] += 20
            time[t] += m
    teams = score.keys()

    result = []
    for scored_team in icpc_sort(teams,score,False):
        for timed_team in icpc_sort(scored_team , time , True):
            timed_team.sort(key=lambda x: -x)
            result.append("=".join(map(str,timed_team)))
    return ",".join(result)

if __name__ == "__main__": main()
