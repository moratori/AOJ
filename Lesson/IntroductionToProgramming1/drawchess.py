import sys


def draw(height,width):
    if (height == 0) and (width == 0) : return
    for y in xrange(height):
        for x in xrange(width):
            sys.stdout.write("#" if ((x+y)%2 == 0) else ".")
        print ""
    print ""


while True:
    try:
        (height,width) = map(int,raw_input().split(" "))
        draw(height,width)
    except (EOFError):
        break
