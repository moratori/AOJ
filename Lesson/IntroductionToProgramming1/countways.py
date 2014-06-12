

def ways(n,x):
    cnt = 0
    for a in xrange(1,n+1):
        for b in xrange(a+1,n+1):
            for c in xrange(b+1,n+1):
                if (a == b) or (b == c) or (a == c): break
                if (a + b + c) == x:cnt += 1
    return cnt
  
(n,x) = map(int,raw_input().split(" "))
while True:
    if (n == 0) and (x == 0):break
    print ways(n,x)
    (n,x) = map(int,raw_input().split(" "))
