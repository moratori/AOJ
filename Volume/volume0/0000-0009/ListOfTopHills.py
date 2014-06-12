
l = [int(raw_input()) for x in xrange(10)]
l.sort(cmp=(lambda x,y: y-x))
print "%s\n%s\n%s" %(l[0],l[1],l[2])
