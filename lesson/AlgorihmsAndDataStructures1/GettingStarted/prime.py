
import math

def isprime(n):
    if n < 2:return False
    if n == 2: return True
    if (n % 2) == 0 : return False
    print range(3,int(math.ceil(math.sqrt(n)))+1,2)
    for acc in xrange(3,int(math.ceil(math.sqrt(n)))+1,2):
        if (n % acc == 0) : return False
    return True

"""
cnt = 0
for dummy in xrange(int(raw_input())):
    if isprime(int(raw_input())):cnt += 1
print cnt
"""

print isprime(3)
