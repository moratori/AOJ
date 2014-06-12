
import sys

house = [[[0 for c in xrange(10)] for b in xrange(3)] for a in xrange(4)]
for dummy in xrange(int(raw_input())):
    (b,f,r,v) = map(int,raw_input().split(" "))
    house[b-1][f-1][r-1] += v
for i,tou in enumerate(house):
    for floor in tou:
        for room in floor:
            sys.stdout.write(" " + str(room))
        print ""
    if (i < 3) :print "#"*20

