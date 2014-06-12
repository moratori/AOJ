
n = int(raw_input())
d = {}
for each in xrange(n):
    (command,operand) = raw_input().strip().split()
    if command == "insert":
        d[operand] = True
    else:
        print "yes" if d.has_key(operand) else "no"
