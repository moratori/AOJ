
for d in xrange(int(raw_input())):
    a = int(raw_input())
    b = int(raw_input())
    r = a+b
    if len(str(r)) > 80:
        print "overflow"
    else:
        print r
