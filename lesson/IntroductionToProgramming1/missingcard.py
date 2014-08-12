
gara = ["S","H","C","D"]
rank = range(1,14)
d = {}
for each in gara:
    for r in rank:
        d[(each,r)] = False


def mycmp(x,y):
    (g1,r1) = x
    (g2,r2) = y
    g1_i = gara.index(g1)
    g2_i = gara.index(g2)
    if g1_i < g2_i : 
        return -1
    elif g2_i < g1_i :
        return 1
    elif r1 > r2:
        return 1
    else:
        return 1

def show(kind,result):
    tmp = filter(lambda x: x[0] == kind,result)
    tmp.sort(key=lambda x:x[1])
    for each in tmp:
        (a,b) = each
        print "%s %s" %(a ,b)

n = int(raw_input())
for dmy in xrange(n):
    (g,r) = raw_input().split(" ")
    r = int(r)
    d[(g,r)] = True
result = [key for key in d.keys() if not d[key]]


show("S",result)
show("H",result)
show("C",result)
show("D",result)
