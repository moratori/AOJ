

def isrectangle(a,b,c):
    return (a**2 == b**2 + c**2) or (b**2 == a**2 + c**2) or (c**2 == b**2 + a**2)

for dummy in xrange(int(raw_input())):
    print "YES" if apply(isrectangle , map(int,raw_input().split(" "))) else "NO"
