import math

prime_cache = {2:True}


while True:
    try:
        n = int(raw_input())
        r = 0
        for target in xrange(1,n+1,2):
            if target == 1:continue
            flag = False
            if prime_cache.has_key(target):
                if prime_cache[target]: r += 1
                continue
            for acc in xrange(3,int(math.ceil(math.sqrt(target)))+1,2):
                if (target % acc == 0):
                    flag = True
                    prime_cache[target] = False
                    break
            if flag: continue
            flag = False
            r += 1
            prime_cache[target] = True
        print r+1 if 2 <= n else r
    except (EOFError):break
