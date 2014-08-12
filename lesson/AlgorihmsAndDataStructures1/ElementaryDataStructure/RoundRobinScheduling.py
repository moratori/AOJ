
from Queue import Queue

TIME = 0
q = Queue()
(N,QUANTUM) = map(int,raw_input().split(" "))
for dummy in xrange(N):
    (name,length) = raw_input().split(" ")
    q.put((name,int(length)))

while (q.qsize() > 0):
    (name,length) = q.get()
    if QUANTUM >= length:
        TIME += length
        print "%s %s" %(name , TIME)
    else:
        TIME += QUANTUM
        q.put((name,length-QUANTUM))

