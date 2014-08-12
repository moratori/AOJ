
import sys


l = []
for d in xrange(int(raw_input())):
    line = raw_input().split(" ")
    command = line[0]
    if command == "insert":
        l.insert(0,line[1])
    elif command == "deleteFirst":
        notNone = None
        for ind,each in enumerate(l):
            if not (each is None):
                notNone = ind
                break
        if not (notNone is None):
            l[notNone] = None
    elif command == "deleteLast":
        notNone = None
        for index in xrange(len(l)-1,0,-1):
            if not (l[index] is None):
                notNone = index
                break
        if not (notNone is None):
            l[notNone] = None
    else:
        try:
            l.remove(line[1])
        except:pass 


flag = False
for each in l:
    if not (each is None):
        if flag: sys.stdout.write(" ")
        sys.stdout.write(each)
        flag = True

print ""


