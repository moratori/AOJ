

import math


def show_point(p):
    print "%.4f %.4f" %(p[0],p[1])

def distance(p1,p2):
    (x1,y1) = p1
    (x2,y2) = p2
    return math.sqrt((x1-x2) ** 2 + (y1-y2) ** 2)


def kock_curve(deepth,p1,p2):
    if deepth == 0 : return
    show_point(p1)
    pass


kock_curve(int(raw_input()),(0,0),(100,0))

