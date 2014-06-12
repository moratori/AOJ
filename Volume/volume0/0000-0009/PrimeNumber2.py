
import math

PRIME_CHACHE = {}
COUNT_UNDER_CACHE = {}

GREAT_N = 2
GREAT_R = 1

def isprime(n):
    global PRIME_CHACHE
    if (n < 2) : return False
    if (n == 2) : return True
    if (n % 2 == 0) : return False
    if PRIME_CHACHE.has_key(n):
        return PRIME_CHACHE[n]
    for acc in xrange(3,int(math.ceil(math.sqrt(n)))+1,2):
        if (n % acc == 0):
            PRIME_CHACHE[n] = False
            return False
    PRIME_CHACHE[n] = True
    return True


def count_under(n):
    global COUNT_UNDER_CACHE
    global GREAT_N
    global GREAT_R
    if COUNT_UNDER_CACHE.has_key(n):return COUNT_UNDER_CACHE[n]

    if n > GREAT_N:
        r = 0
        for acc in xrange(GREAT_N+1,n+1,1):
            if isprime(acc) : r += 1
        result = r + GREAT_R
        GREAT_N = n
        GREAT_R = result
    else:
        r = 0
        for acc in xrange(1,n+1,2):
            if isprime(acc):r += 1
        result = r+1 if n >= 2 else r
    
    COUNT_UNDER_CACHE[n] = result
    return result

while True:
    try:
        print count_under(int(raw_input()))
    except (EOFError):break



