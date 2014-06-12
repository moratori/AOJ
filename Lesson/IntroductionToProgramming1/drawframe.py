
import sys

def draw(h,w):
    if (h == 0) and (w == 0) : return
    for y in xrange(h):
        for x in xrange(w):
            if (y == 0) or (y == h -1):
                sys.stdout.write("#")
            elif (x > 0) and (w-1 > x):
                sys.stdout.write(".")
            else:
                sys.stdout.write("#")
        print ""
    print ""


while (True):
    try:
        apply(draw, map(int,raw_input().split(" ")))
    except:break





