


lock = True
registered = [raw_input() for each in xrange(input())]
for op in xrange(input()):
    user = raw_input()
    if not (user in registered):
        print "Unknown %s" %(user)
    else:
        if ( lock ):
            print "Opened by %s" %(user)
        else:
            print "Closed by %s" %(user)
        lock = not lock
