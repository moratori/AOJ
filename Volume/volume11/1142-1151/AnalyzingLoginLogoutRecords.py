#!/usr/bin/env python
#coding:utf-8

def contain(int1,int2):
    (s1,e1) = int1
    (s2,e2) = int2 
    if (s1 < e1 <= s2 < e2) or (s2 < e2 <= s1 < e1):return False 
    return True

def merge(int1,int2):
    (s1,e1) = int1
    (s2,e2) = int2 
    return (min(s1,s2),max(e1,e2))

def insert_interval(interval,intseq):
    cand = []
    for each in intseq:
        if contain(each,interval):
            cand.append(merge(each,interval))
    if len(cand) > 1:
        left = map(lambda x: x[0] , cand)
        right = map(lambda x: x[1] , cand)
        largest = (apply(min,left),apply(max,right))
    elif len(cand) == 1:
        largest = cand[0]
    elif not cand:
        intseq.append(interval)
        return intseq
    result = []
    for each in intseq:
        if not contain(largest,each):
            result.append(each)
    result.append(largest)
    return result

def join(sequences):
    length = len(sequences)
    if length == 0:
        return sequences
    elif length == 1:
        return sequences[0]
    result = sequences[0]
    for each in sequences[1:]:
        for interval in each:
            result = insert_interval(interval,result)
    result.sort(key=lambda x: x[0])
    return result

def filter_around_interval(ts,te,table):
    around = {}
    for pc,time in table.items():
        tmp = []
        for (login,logout) in time:
            if ts < logout and login < te:
                tmp.append((login,logout))
        if tmp:
            around[pc] = tmp
    return around

def calculate(ts,te,table):
    total = 0
    for (login,logout) in table:
        (ns,ne) = (login,logout)
        if login < ts:
            ns = ts
        if te < logout:
            ne = te 
        total += ne - ns
    return total

def solve(log,question):
    (ts,te,m) = question
    tmp = {}
    table = {}
    for (time,pc,student,flag) in log:
        if m == student:
            if tmp.has_key(pc):
                tmp[pc].append(time)
            else:
                tmp[pc] = [time]
            if len(tmp[pc]) == 2:
                if table.has_key(pc):
                    table[pc].append(tuple(tmp[pc]))
                else:
                    table[pc] = [tuple(tmp[pc])]
                tmp[pc] = []
    around_dead_line = filter_around_interval(ts,te,table)
    return calculate(ts,te,join(around_dead_line.values()))

def parse_line():return map(int,raw_input().split(" "))

def main():
    while True:
        (n,m) = parse_line()
        if n == 0 and m == 0:break
        log = []
        for d in xrange(int(raw_input())):
            log.append(parse_line())
        for d in xrange(int(raw_input())):
            print solve(log,parse_line())

if __name__ == "__main__":main()

