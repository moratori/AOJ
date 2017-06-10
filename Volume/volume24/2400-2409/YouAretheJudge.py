#!/usr/bin/env python
#coding:utf-8



def main():
    while True:
        t,p,r = map(int,raw_input().split(" "))
        if (t,p,r) == (0,0,0): break
        team_result = [{"tid"    : cnt,\
                        "correct": 0,\
                        "penalty": 0,\
                        "wrongs" : {pid:0 for pid in xrange(p)}} for cnt in xrange(t)]
        for d in xrange(r):
            tid,pid,time,mes = raw_input().split(" ")
            tid,pid,time = int(tid),int(pid),int(time)
            tid -= 1
            pid -= 1
            if   mes == "CORRECT":
                team_result[tid]["correct"] += 1
                team_result[tid]["penalty"] += time + team_result[tid]["wrongs"][pid] * 1200
            elif mes == "WRONG":
                team_result[tid]["wrongs"][pid] += 1

        team_result.sort(key=lambda x:
                (-x["correct"],x["penalty"],x["tid"]))

        for team in team_result:
            print "%d %d %d" %(team["tid"]+1, team["correct"], team["penalty"])




if __name__ == "__main__":
    main()
