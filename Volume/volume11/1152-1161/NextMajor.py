

def iswin(index,lst):
    for k,cand in enumerate(lst):
        if (k != index) and (cand != 0) : return False 
    return True


def proc(n,p):
    bowl  = p
    #cands = init_candidate(n)
    cands  = [0 for x in xrange(n)]
    while True:
        #for cand in cands:
        for k,cand in enumerate(cands):
            if (bowl == 1) and (iswin(k,cands)):
                return k
            elif not (bowl == 0):
                cands[k] += 1
                bowl -= 1
            else:
                if not (cand == 0):
                    bowl  += cand
                    cands[k] = 0

while True:
    (n,p) = map(int,raw_input().split())
    if (n == 0) and (p == 0) : break
    print proc(n,p)

